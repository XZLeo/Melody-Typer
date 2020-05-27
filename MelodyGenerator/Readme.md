## Inspiration
Some short videos seem funny that YouTubers use dialing keyboard of their mobile phones to play short music. Wouldn't it be a little 
suprise for friends to play a birthday song as a gift? After several attemps, I found the sequence of taping the keyboard must be
remembered, which can take a lot practicing. Fine, let's automate it with ADB and python!
## Equipment
Huawei mate 20 (without root), USB cable or wifi, python3, ADB 
## Basic Idea
## Run
## A possible way to speed up the tapping
After running `faster.py`, most of music snippet sounds fluent. I'm amzeed at how simple it is to creatte beauty, meanwhile, I find the 
rythm is a bit slow for some music, like He is a pirate. After googling, I found that `input tap` is a java application, and that delay
is actually the time required to spawn then run it.

The first thing I did was to 

A possible way is to root the phone and use `dd` to record your taping and then replay the record. However, rooting a new phone is risky.
I tried that method and found `permission denied` 

