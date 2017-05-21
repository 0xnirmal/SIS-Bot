# SIS Bot #

This selenium bot allows you to register for classes on Johns Hopkins SIS portal right at 7:00 AM, to virtually guarantee a spot in all of your classes. 

### WARNING: This has only been tested on Mac OS (and will probably only work on it). ###

## Setup Instructions ##
```
pip install -r requirements.txt
```

## Running Instructions ##
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes. 
```
python bot.py SIS_Username SIS_Password
```
