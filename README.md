# Forza-H4-Tunning-Calculator

After some time doing the calculations by hand i decided to create this script, it is complete CLI based and don't have any requirements.

The results of this calculator are NOT 100% precise, driving preference, style and car by car variance are not measured. This is a base for you to start at, taking account weight distribution of the car.

Formula used by HokiHoshi.

For more information on how this formula works this is the video in question: https://youtu.be/WM7_3NGGUoQ

 I have no association with him, its just a script that i created for personal use and decided to share.

# How to use it
Install Python3.6+ 

1. And start the program with:

  Windows:
  "python FH4_Calculator.py"

  Linux:
  "python3 FH4_Calculator.py"

2. Insert the percentage of weight distribution.
3. Insert the maximum and minimum values of which bar.

# Formula used
(max - min) * W% + min = result

1. max => Max value of the tunning bar
2. min => Min value of the tunning bar
3. W%  => Weight distribution of the car



If you want to close the program use Ctrl+C to exit.


# To do
The code needs a top to botton rewrite for performance and usability reasons as i write it on my launch time without planning. All the calculations are correctly working.

# Version
Calculator version 0.01 (Alpha).
