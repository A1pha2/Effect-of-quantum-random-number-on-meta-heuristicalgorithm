To run main.cc, you need to build the .exe first by code in terminal:

``` g++ "beam_splitter_rng\code\main.cc" -o "beam_splitter_rng\code\main.exe" ```
(  g++ "<.cc code path>" -o "<.exe destination>"  )

Then, you'll have executable file that can be used by command followed:

``` .\beam_splitter_rng\code\main.exe ".\beam_splitter_rng\experiment\default10.ptu" ".\beam_splitter_rng\random_number_sample\rand10_10_1M.txt" ```     
(  <.exe destination> "<.ptu experiment path>" "<.txt randomnumber>"  )

<br>Note that: 1. Before you call .exe, you should have experiment file in your system (```defaultxx.ptu```).<br>
              We didn't upload large file in Github repository exceeded file size constraint.<br>
              If you don't have any experiment files (.ptu), you can download by this [Link](https://mailkmuttacth-my.sharepoint.com/:f:/g/personal/boonyarit_samr_kmutt_ac_th/EnnsIgXPTWZLiLjlYPj6WXgBTNCSfuMZx_EiAKFgO-SM-Q?e=DB2ysi).<br>
           2. You can change any path or experiment to generate random number.