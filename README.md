# The Mystery Calculator

I got a little game from a christmas cracker called "The Mystery Calculator"
which has a bunch of cards with numbers on each. The player selects a number
from any card and through asking whether the number is present on all given
cards, the number can be determined.

The original cards have numbers from 1-63, but this and a few other settings can
be adjusted with command line options. See `-h` or `--help` for more detail.

The mechanism by which it operates is pretty simple to figure out, but can be a
fun exercise. If you don't already know, try to figure it out just by looking at
the output. A sample run is included below for convenience.

The below output is a run in which I chose 12 as my number:
```text
The mystery calculator!!!

Pick a number between 1 and 63 (but don't tell me)

 1  3  5  7  9 11 13 15
17 19 21 23 25 27 29 31
33 35 37 39 41 43 45 47
49 51 53 55 57 59 61 63
Is your number on this card? [y/N]: n


 2  3  6  7 10 11 14 15
18 19 22 23 26 27 30 31
34 35 38 39 42 43 46 47
50 51 54 55 58 59 62 63
Is your number on this card? [y/N]: n


 4  5  6  7 12 13 14 15
20 21 22 23 28 29 30 31
36 37 38 39 44 45 46 47
52 53 54 55 60 61 62 63
Is your number on this card? [y/N]: y


 8  9 10 11 12 13 14 15
24 25 26 27 28 29 30 31
40 41 42 43 44 45 46 47
56 57 58 59 60 61 62 63
Is your number on this card? [y/N]: y


16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63
Is your number on this card? [y/N]: n


32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63
Is your number on this card? [y/N]: n


🪄 Your number was: 12. Magic!
```
