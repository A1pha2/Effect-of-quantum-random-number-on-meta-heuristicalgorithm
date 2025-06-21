/************************************************************************

  PicoQuant Unified TTTR (PTU)    File Access Demo in C/C++

  This is demo code. Use at your own risk. No warranties.

  Tested with MS Visual Studio 2010 and Mingw 4.5

  Marcus Sackrow, PicoQuant GmbH, December 2013
  Michael Wahl, PicoQuant GmbH, revised July 2014


************************************************************************/

#include <algorithm>
#include <windows.h>
#include <direct.h>
#include <stdio.h>
#include <cmath>
#include <conio.h>
#include <stddef.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <chrono>
#include <limits>
using namespace std::chrono;

// some important Tag Idents (TTagHead.Ident) that we will need to read the most common content of a PTU file
// check the output of this program and consult the tag dictionary if you need more
#define TTTRTagTTTRRecType "TTResultFormat_TTTRRecType"
#define TTTRTagNumRecords "TTResult_NumberOfRecords" // Number of TTTR Records in the File;
#define TTTRTagRes "MeasDesc_Resolution"             // Resolution for the Dtime (T3 Only)
#define TTTRTagGlobRes "MeasDesc_GlobalResolution"   // Global Resolution of TimeTag(T2) /NSync (T3)
#define FileTagEnd "Header_End"                      // Always appended as last tag (BLOCKEND)

// TagTypes  (TTagHead.Typ)
#define tyEmpty8 0xFFFF0008
#define tyBool8 0x00000008
#define tyInt8 0x10000008
#define tyBitSet64 0x11000008
#define tyColor8 0x12000008
#define tyFloat8 0x20000008
#define tyTDateTime 0x21000008
#define tyFloat8Array 0x2001FFFF
#define tyAnsiString 0x4001FFFF
#define tyWideString 0x4002FFFF
#define tyBinaryBlob 0xFFFFFFFF

// RecordTypes
#define rtPicoHarpT3 0x00010303     // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $03 (T3), HW: $03 (PicoHarp)
#define rtPicoHarpT2 0x00010203     // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $02 (T2), HW: $03 (PicoHarp)
#define rtHydraHarpT3 0x00010304    // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $03 (T3), HW: $04 (HydraHarp)
#define rtHydraHarpT2 0x00010204    // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $02 (T2), HW: $04 (HydraHarp)
#define rtHydraHarp2T3 0x01010304   // (SubID = $01 ,RecFmt: $01) (V2), T-Mode: $03 (T3), HW: $04 (HydraHarp)
#define rtHydraHarp2T2 0x01010204   // (SubID = $01 ,RecFmt: $01) (V2), T-Mode: $02 (T2), HW: $04 (HydraHarp)
#define rtTimeHarp260NT3 0x00010305 // (SubID = $00 ,RecFmt: $01) (V2), T-Mode: $03 (T3), HW: $05 (TimeHarp260N)
#define rtTimeHarp260NT2 0x00010205 // (SubID = $00 ,RecFmt: $01) (V2), T-Mode: $02 (T2), HW: $05 (TimeHarp260N)
#define rtTimeHarp260PT3 0x00010306 // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $02 (T3), HW: $06 (TimeHarp260P)
#define rtTimeHarp260PT2 0x00010206 // (SubID = $00 ,RecFmt: $01) (V1), T-Mode: $02 (T2), HW: $06 (TimeHarp260P)

#pragma pack(8) // structure alignment to 8 byte boundaries

// A Tag entry
struct TgHd
{
  char Ident[32];     // Identifier of the tag
  int Idx;            // Index for multiple tags or -1
  unsigned int Typ;   // Type of tag ty..... see const section
  long long TagValue; // Value of tag.
} TagHead;

// TDateTime (in file) to time_t (standard C) conversion

const int EpochDiff = 25569; // days between 30/12/1899 and 01/01/1970
const int SecsInDay = 86400; // number of seconds in a day

time_t TDateTime_TimeT(double Convertee)
{
  time_t Result((long)(((Convertee)-EpochDiff) * SecsInDay));
  return Result;
}

FILE *fpin, *fpout;
bool IsT2;
long long RecNum;
long long oflcorrection;
long long truensync, truetime;
int m, c, DT, Ctrl;
long long TIME_START, TIME_STOP;
double GlobRes = 0.0;
double Resolution = 0.0;
unsigned int dlen = 0;
unsigned int cnt_0 = 0, cnt_1 = 0;
std::vector<int> collector;
std::vector<double> splitter;

// procedures for Photon, overflow, marker

// Got Photon
//   TimeTag: Raw TimeTag from Record * Globalresolution = Real Time arrival of Photon
//   DTime: Arrival time of Photon after last Sync event (T3 only) DTime * Resolution = Real time arrival of Photon after last Sync event
//   Channel: Channel the Photon arrived (0 = Sync channel for T2 measurements)
void GotPhoton(long long TimeTag)
{
  collector.push_back(TimeTag - TIME_STOP);
  Ctrl = 0;
}

// Got Marker
//   TimeTag: Raw TimeTag from Record * Globalresolution = Real Time arrival of Photon
//   Markers: Bitfield of arrived Markers, different markers can arrive at same time (same record)
void GotMarker(long long TimeTag, int Markers)
{
  fprintf(fpout, "%I64u MAR %2x %I64u\n", RecNum, Markers, TimeTag);
}

// Got Overflow
//   Count: Some TCSPC provide Overflow compression = if no Photons between overflow you get one record for multiple Overflows
void GotOverflow(int Count)
{
  fprintf(fpout, "%I64u OFL * %2x\n", RecNum, Count);
}

void ProcessPHT2(unsigned int TTTRRecord)
{
  const int T2WRAPAROUND = 210698240;
  union
  {
    unsigned int allbits;
    struct
    {
      unsigned time : 28;
      unsigned channel : 4;
    } bits;

  } Record;
  unsigned int markers;
  Record.allbits = TTTRRecord;
  if (Record.bits.channel == 0xF) // this means we have a special record
  {
    // in a special record the lower 4 bits of time are marker bits
    markers = Record.bits.time & 0xF;
    if (markers == 0) // this means we have an overflow record
    {
      oflcorrection += T2WRAPAROUND; // unwrap the time tag overflow
      // GotOverflow(1);
    }
    else // a marker
    {
      // Strictly, in case of a marker, the lower 4 bits of time are invalid
      // because they carry the marker bits. So one could zero them out.
      // However, the marker resolution is only a few tens of nanoseconds anyway,
      // so we can just ignore the few picoseconds of error.
      truetime = oflcorrection + Record.bits.time;
      // GotMarker(truetime, markers);
    }
  }
  else
  {
    if ((int)Record.bits.channel > 4) // Should not occur
    {
      printf(" Illegal Chan: #%I64u %1u\n", RecNum, Record.bits.channel);
      fprintf(fpout, " illegal chan.\n");
    }
    else
    {
      if (Record.bits.channel == 0)
      {
        truetime = oflcorrection + Record.bits.time;
        Ctrl = 1;
      }
      else if ((Record.bits.channel == 1) && (Ctrl == 1))
      {
        TIME_STOP = truetime;
        cnt_1++;
        truetime = oflcorrection + Record.bits.time;
        GotPhoton(truetime);
      }
    }
  }
}

void print_spiltter(int maxIndex, int n_hist){
  int printIndex = n_hist;
  if(n_hist > maxIndex){printIndex = maxIndex;}
  printf("split list: [");
  for (int i = 0; i < printIndex; i++)
  {
    printf("%f, ", splitter[i]);
  }
  if(n_hist > maxIndex){printf("..., ");}
  printf("%f, %f] \n", splitter.end()[-2] ,splitter.back());
}

double find_lambda(int choice, int trainSetAmount, int testSetAmount)
{
  double trainLambda = 0.0;
  if (choice < 1 || choice > 4)
  {
    printf("skip\n");
  }
  else
  {
    unsigned long long int x_train_sum = 0;
    unsigned long long int x_test_sum = 0;
    if (choice != 2)
    {
      for (int i = 0; i < trainSetAmount; i++)
      {
        x_train_sum += collector[i];
      }
    }
    if (choice != 1)
    {
      for (int i = trainSetAmount; i < collector.size(); i++)
      {
        x_test_sum += collector[i];
      }
    }
    if (choice == 1 || choice == 4)
    {
      trainLambda = (double)trainSetAmount / x_train_sum;
      printf("histogram splitter lambda : %e\n", trainLambda);
    }
    if (choice == 2 || choice == 4)
    {
      printf("data generator lambda : %e\n", (double)testSetAmount / x_test_sum);
    }
    if (choice == 3 || choice == 4)
    {
      printf("all data lambda : %e\n", (double)(trainSetAmount + testSetAmount) / (x_train_sum + x_test_sum));
    }
    printf("\n");
  }
  return trainLambda;
}

void sort_split(int n_seq, int trainSetAmount)
{
  int n_hist = pow(2, n_seq);
  std::partial_sort(collector.begin(), collector.begin() + trainSetAmount, collector.begin() + trainSetAmount);
  double chunck_size = (double)trainSetAmount / n_hist;
  splitter.push_back(collector[0]);
  for (int i = 1; i < n_hist; i++)
  {
    splitter.push_back(collector[ceil(chunck_size * i)]);
  }
  splitter.push_back(collector[trainSetAmount - 1]);
  for (int i = 1; i < n_hist-1; i++)
  {
    double currentDT = splitter[i];
    if (currentDT == splitter[i+1]){
      splitter[i+1] = (splitter[i+2] + currentDT)/2;
    }
  }
  print_spiltter(16, n_hist);
}

void count_split(int n_seq, int trainSetAmount)
{
  int n_hist = pow(2, n_seq);
  int max_DT = *std::max_element(collector.begin(), collector.begin() + trainSetAmount);
  std::vector<int> tempList(max_DT + 1, 0);
  for (int i = 0; i < trainSetAmount; i++)
  {
    tempList[collector[i]]++;
  }
  double chunk_size = (double)trainSetAmount / n_hist;

  double counter = 0.0;
  int min_DT = 1;
  while (tempList[min_DT] == 0)
  {
    min_DT++;
  }
  splitter.push_back(min_DT);

  for (int i = 0; i < max_DT; i++)
  {
    counter += tempList[i];
    if (counter >= chunk_size)
    {
      counter -= chunk_size;
      splitter.push_back(i);
    }
  }

  splitter.push_back(max_DT);
  print_spiltter(16, n_hist);
}

uint16_t bin_search(int DT){
  int low = 0;
  int high = splitter.size() - 2; //
  while(high >= low){
    int mid = (high + low)/2;
    if(DT < splitter[mid]){ high = mid - 1;}
    else{ low = mid + 1;}
  }
  return (uint16_t) (low - 1);
}

void write_file_with_cutIdx(char *argv[], int trainSetAmount, double trainLambda, int bitSeq, int cutDecayTime)
{
  printf("\ngenerate random number to %s ...\n", argv[2]);
  // Get starting timepoint
  auto start = high_resolution_clock::now();
  int max_DT = splitter.back();
  int cutNum = ceil(pow(2, bitSeq)*(1- exp(-trainLambda*cutDecayTime)));  
  printf("amount of dropped number %d \n", cutNum);
  for (int i = trainSetAmount; i < collector.size(); i++)
  {
    int currentDecayTime = collector[i];
    if (currentDecayTime > cutDecayTime){
      int num = bin_search(currentDecayTime) - cutNum;
      fprintf(fpout, "%d\n", num);
    }
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  printf("Finished. Time usage : %d microsecond", duration);
}

uint32_t concat_to_32bit(uint16_t num1, uint16_t num2) {
    // Shift num1 left by 16 bits and OR with num2
    return ((uint32_t)num1 << 16) | (uint32_t)num2;
}

void write_file(char *argv[], int trainSetAmount)
{
  printf("\ngenerate random number to %s ...\n", argv[2]);
  // Get starting timepoint
  auto start = high_resolution_clock::now();
  int DT = 0;
  int max_DT = splitter.back();
  for (int i = trainSetAmount; i < collector.size(); i+=2)
  {
    uint16_t num1 = bin_search(collector[i]);
    uint16_t num2 = bin_search(collector[i+1]);
    if (num1 >= 0 && num2 >= 0){fprintf(fpout, "%u\n", concat_to_32bit(num1, num2));}
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  printf("Finished. Time usage : %d microsecond", duration);
}


int is_write()
{
  char isWrite;
  printf(">> generate random number [Y/n] : ");
  scanf(" %c", &isWrite);
  if (isWrite == 'Y')
  {
    return true;
  }
  else
  {
    printf("skip\n");
    return false;
  }
}

int cut_decay(){
  double deadTimeCoef = 0.0;
  double deadTimeExpo = 0.0;
  double decayTimeCoef = 4.0;
  double cutDecayTime = 0.0;
  printf(">> hardware deadtime coefficient : ");
  scanf(" %lf", &deadTimeCoef);
  printf(">> hardware deadtime exponent (base 10) : ");
  scanf(" %lf", &deadTimeExpo);
  printf(">> decay time precision (ps scaled) : ");
  scanf(" %lf", &decayTimeCoef);
  double deadTime = deadTimeCoef * pow(10, deadTimeExpo);
  double precision = decayTimeCoef * pow(10, -12);
  cutDecayTime = deadTime/precision;  
  printf("lower bound of dacay time : %lf ", cutDecayTime);
  return cutDecayTime;
}

int is_cut(){
  char isCut;
  printf(">> cut error decaytime due to hardware deadtime [Y/n] : ");
  scanf(" %c", &isCut);
  if (isCut == 'Y')
  {
    return true;
  }
  else
  {
    printf("skip\n");
    return false;
  }
}

void learn_lambda_split(int n_seq, double trainLambda){
   int n_hist = pow(2, n_seq);
   for(int z = 0; z <= n_hist; z++){
    splitter.push_back( (double)( log( (pow(2,n_seq)-z) / pow(2, n_seq) )/ -trainLambda ) );
   }
  //  double inf = std::numeric_limits<double>::infinity();
  //  splitter.push_back(inf);
   print_spiltter(16, n_hist);
}

int main(int argc, char *argv[])
{
  char Magic[8];
  char Version[8];
  char Buffer[40];
  char *AnsiBuffer;
  WCHAR *WideBuffer;
  int Result;

  long long NumRecords = -1;
  long long RecordType = 0;

  printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf(" Generate number from PTU file");
  printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

  if ((argc < 3) || (argc > 3))
  {
    printf("usage: ht2demo infile oufile\n");
    printf("infile is a Unified TTTR ptu file (binary)\n");
    printf("outfile is ASCII\n");
    _getch();
    exit(-1);
  }
  if ((fpin = fopen(argv[1], "rb")) == NULL)
  {
    printf("\n ERROR! Input file cannot be opened, aborting.\n");
    goto ex;
  }

  if ((fpout = fopen(argv[2], "w")) == NULL)
  {
    printf("\n ERROR! Output file cannot be opened, aborting.\n");
    goto ex;
  }

  printf("\nLoading data on .ptu file from %s \n", argv[1]);
  // printf("generate random number to %s \n", argv[2]);

  Result = fread(&Magic, 1, sizeof(Magic), fpin);
  if (Result != sizeof(Magic))
  {
    printf("\nerror reading header, aborted.");
    goto close;
  }
  Result = fread(&Version, 1, sizeof(Version), fpin);
  if (Result != sizeof(Version))
  {
    printf("\nerror reading header, aborted.");
    goto close;
  }
  if (strncmp(Magic, "PQTTTR", 6))
  {
    printf("\nWrong Magic, this is not a PTU file.");
    goto close;
  }
  // fprintf(fpout, "Tag Version: %s \n", Version);

  // read tagged header
  do
  {
    // This loop is very generic. It reads all header items and displays the identifier and the
    // associated value, quite independent of what they mean in detail.
    // Only some selected items are explicitly retrieved and kept in memory because they are
    // needed to subsequently interpret the TTTR record data.

    Result = fread(&TagHead, 1, sizeof(TagHead), fpin);
    if (Result != sizeof(TagHead))
    {
      printf("\nIncomplete File.");
      goto close;
    }

    // strcpy(Buffer, TagHead.Ident);
    // if (TagHead.Idx > -1)
    // {
    //   sprintf(Buffer, "%s(%d)", TagHead.Ident,TagHead.Idx);
    // }
    // fprintf(fpout, "\n%-40s", Buffer);
    switch (TagHead.Typ)
    {
    //   case tyEmpty8:
    //   fprintf(fpout, "<empty Tag>");
    //   break;
    // case tyBool8:
    //   fprintf(fpout, "%s", bool(TagHead.TagValue)?"True":"False");
    //   break;
    case tyInt8:
      // fprintf(fpout, "%lld", TagHead.TagValue);
      // get some Values we need to analyse records
      if (strcmp(TagHead.Ident, TTTRTagNumRecords) == 0) // Number of records
        NumRecords = TagHead.TagValue;
      if (strcmp(TagHead.Ident, TTTRTagTTTRRecType) == 0) // TTTR RecordType
        RecordType = TagHead.TagValue;
      break;
    // case tyBitSet64:
    //   fprintf(fpout, "0x%16.16X", TagHead.TagValue);
    //   break;
    // case tyColor8:
    //   fprintf(fpout, "0x%16.16X", TagHead.TagValue);
    //   break;
    case tyFloat8:
      // fprintf(fpout, "%E", *(double*)&(TagHead.TagValue));
      if (strcmp(TagHead.Ident, TTTRTagRes) == 0) // Resolution for TCSPC-Decay
        Resolution = *(double *)&(TagHead.TagValue);
      if (strcmp(TagHead.Ident, TTTRTagGlobRes) == 0) // Global resolution for timetag
        GlobRes = *(double *)&(TagHead.TagValue);     // in ns
      break;
    case tyFloat8Array:
      // fprintf(fpout, "<Float Array with %d Entries>", TagHead.TagValue / sizeof(double));
      // only seek the Data, if one needs the data, it can be loaded here
      fseek(fpin, (long)TagHead.TagValue, SEEK_CUR);
      break;
    case tyTDateTime:
      time_t CreateTime;
      CreateTime = TDateTime_TimeT(*((double *)&(TagHead.TagValue)));
      // fprintf(fpout, "%s", asctime(gmtime(&CreateTime)), "\0");
      break;
    case tyAnsiString:
      AnsiBuffer = (char *)calloc((size_t)TagHead.TagValue, 1);
      Result = fread(AnsiBuffer, 1, (size_t)TagHead.TagValue, fpin);
      if (Result != TagHead.TagValue)
      {
        printf("\nIncomplete File.");
        free(AnsiBuffer);
        goto close;
      }
      // fprintf(fpout, "%s", AnsiBuffer);
      free(AnsiBuffer);
      break;
    case tyWideString:
      WideBuffer = (WCHAR *)calloc((size_t)TagHead.TagValue, 1);
      Result = fread(WideBuffer, 1, (size_t)TagHead.TagValue, fpin);
      if (Result != TagHead.TagValue)
      {
        printf("\nIncomplete File.");
        free(WideBuffer);
        goto close;
      }
      // fwprintf(fpout, L"%s", WideBuffer);
      free(WideBuffer);
      break;
    case tyBinaryBlob:
      fprintf(fpout, "<Binary Blob contains %d Bytes>", TagHead.TagValue);
      // only seek the Data, if one needs the data, it can be loaded here
      fseek(fpin, (long)TagHead.TagValue, SEEK_CUR);
      break;
    default:
      // printf("Illegal Type identifier found! Broken file?");
      // goto close;
      break;
    }
  } while ((strncmp(TagHead.Ident, FileTagEnd, sizeof(FileTagEnd))));
  // fprintf(fpout, "\n-----------------------\n");
  // End Header loading

  unsigned int TTTRRecord;
  for (RecNum = 0; RecNum < NumRecords; RecNum++)
  {
    Result = fread(&TTTRRecord, 1, sizeof(TTTRRecord), fpin);
    if (Result != sizeof(TTTRRecord))
    {
      printf("\nUnexpected end of input file!");
      break;
    }
    switch (RecordType)
    {
    case rtPicoHarpT2:
      IsT2 = true;
      ProcessPHT2(TTTRRecord);
      break;
    default:
      printf("not PTU file!");
      goto close;
    }
  }

  char isSplit;
  int choice;
  int trainSetAmount, testSetAmount;
  double trainLambda;
  int cutDecayTime;
  printf("\n>> data amount for histogram splitter : ");
  scanf(" %d", &trainSetAmount);
  testSetAmount = cnt_1 - trainSetAmount;
  printf("The amount of all data: %d \nHistogram splitter data: %d\ngenerator data: %d \n\n", cnt_1, trainSetAmount, testSetAmount);
  printf(">> Find rate parameter (lambda) from\n");
  printf(" * [1] histogram splitter data\n * [2] generator data\n * [3] all data\n * [4] show all\n Choice : ");
  scanf(" %d", &choice);
  trainLambda = find_lambda(choice, trainSetAmount, testSetAmount);
  printf(">> Split histogram by giving n_seq [Y/n] : ");
  scanf(" %c", &isSplit);
  if (isSplit == 'Y')
  {
    int bitSeq;
    printf(">> n_seq: ");
    scanf(" %d", &bitSeq);
    int method;
    printf(">> Choose method for splitter\n");
    printf(" * [1] Sorting and split\n * [2] Count cum. freq. and split\n * [3] find lambda and split\n * [4] fix lambda\n Choice : ");
    scanf(" %d", &method);
    if (method == 1)
    {
      sort_split(bitSeq, trainSetAmount);
      if (is_write())
      {
        write_file(argv, trainSetAmount);
      }
    }
    else if (method == 2)
    {
      count_split(bitSeq, trainSetAmount);
      if (is_write())
      {
        write_file(argv, trainSetAmount);
      }
    }
    else if (method == 3)
    {
      learn_lambda_split(bitSeq, trainLambda);
      if (is_write())
      {
        if (is_cut()){cutDecayTime = cut_decay();}
        write_file_with_cutIdx(argv, trainSetAmount, trainLambda, bitSeq, cutDecayTime);
      }
    }
    else if (method == 4)
    {
      double fixLambdaCoef;
      double fixLambdaExpo;
      printf(">> your lambda coefficient : ");
      scanf(" %lf", &fixLambdaCoef);
      printf(">> your lambda exponent (base 10) : ");
      scanf(" %lf", &fixLambdaExpo);
      double fixLambda = fixLambdaCoef*pow(10, fixLambdaExpo);
      learn_lambda_split(bitSeq, fixLambda);
      if (is_write())
      {
         if (is_cut()){cutDecayTime = cut_decay();}
        write_file_with_cutIdx(argv, trainSetAmount, trainLambda, bitSeq, cutDecayTime);
      }
    }
    else
    {
      printf("skip\n");
    }
  }
  else
  {
    printf("skip\n");
  }

close:
  fclose(fpin);
  fclose(fpout);

ex:
  printf("\n any key to terminate program...");
  getch();
  exit(0);
  return (0);
}