# SIS Bot #

This selenium bot allows you to register for classes on Johns Hopkins SIS portal right at 7:00 AM, to virtually guarantee a spot in all of your classes. 

### WARNING: This has only been tested on Mac OS (and will probably only work on it). ###

## Setup Instructions ##
```
pip install -r requirements.txt
```

SIS uses the naval observatory clock to determine time. Therefore, your system must be synced to this clock to ensure you do not click too early or too late. On Mac OS, it is easy to change your default. 

1. Navigate to System Preferences and click Date and Time. 
2. Click the lock on the bottom left of your window and enter your password. 
3. Change "Apple Americas/U.S. (time.apple.com.)" to "tick.usno.navy.mil"
4. Click the lock again to save your changes. 

![time instructions](/time_instruc "Logo Title Text 1")


## Running Instructions ##
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes. 
```
python bot.py SIS_Username SIS_Password
```
