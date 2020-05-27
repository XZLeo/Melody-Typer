## Inspiration
Some short videos seem funny that YouTubers use dialing keyboard of their mobile phones to play short music. Wouldn't it be a little 
suprise for friends to play a birthday song as a gift? After several attemps, I found the sequence of taping the keyboard must be
remembered, which can take a lot practicing. Fine, let's automate it with ADB and python!
## Equipment
Huawei mate 20 (without root), USB cable or wifi, python3, ADB 
## Basic Idea
- Create a library of music scores in txt files. In each txt file, there are lines of series of numbers and *, #, which represent the 
sequence of tapping;
- Read txt file and interpret it to (x, y), in which x, y represents the (x, y) coordinates on the phone screen;
- Use `OS.system()` to call adb shell;
- Use `adb shellinput tap x y` to create tapping event
- Endless loop fr user to choose different melodies
## Run
1. Use te USB cable to connect the phone and PC;
2. Tap the `Build number` several times to open `Developer options`
3. Enter `Developer options` and turn on `USB debugging`
4. Run the `Faster.py` on the PC.
In the library, there're BirthdaySong, Little Star, He is a Pirate, City of Sky. Piano solos are suitalble to play.
## A possible way to speed up the tapping
After running `faster.py`, most of music snippet sounds fluent. I'm amzeed at how simple it is to creatte beauty, meanwhile, I find the 
rythm is a bit slow for some music, like He is a pirate. After googling, I found that `input tap` is a java application, and that delay
is actually the time required to spawn then run it.

The first thing I did was to change `MelodyGenerator.py` to `Faster.py`. The main difference is reducing the times to use `os.system()`. Because it will start a new subprocess each time. It would save some time to call it once for each snippet, and then pause, then next snippet with a new `os.system()`. But this method wouldn't make an obvious difference.

A possible way is to root the phone and use `dd` to record your taping and then replay the record. [This blog](https://igor.mp/blog/2018/02/23/using-adb-simulate-touch-events.html) inspires me a lot. However, rooting a new phone is risky.
I tried that method and found `permission denied` in ADB shell while replaying the record.

