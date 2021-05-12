# This app is deprecated
Because this app is CLI based a lot of people are not confortable using it, so I remade this app in a web version, it can be found here: https://github.com/OLoKo64/Multiple-Game-Calculator-Web-App.

This Python version do the exact same operations as the web version, so if you want to use this CLI version, cudos to you :).


# Forza H4 Tunning Calculator

After some time doing the calculations by hand i decided to create this script, it is complete CLI based and don't have any requirements.

The results of this calculator are NOT 100% precise, driving preference, style and car by car variance are not measured. This is a base for you to start at, taking account weight distribution of the car.


# How to use it
Install Python3.6+ 

1. And start the program with:

  Windows:
  "python FH4_Calculator.py"

  Linux:
  "python3 FH4_Calculator.py"

2. Insert the weight of the car.
3. Insert the weight distribution percentage.
4. Insert how much softiness you want for the suspension:

10  - Very soft.

20  - Normal [Default].

30+ - Very stiff.

5. Insert the maximum value of the Rebound Stiffness bar [Default: 20]

If you want to close the program use Ctrl+C to exit.


# Formula used
Suspension = (weight * chosed_stiffness) * weight_distribution

Rebound Stiffness = max_value_bar * weight_distribution

Bump Stiffness = Rebound Stiffness * 0.5


# Version
Calculator version 0.10 (Alpha).
