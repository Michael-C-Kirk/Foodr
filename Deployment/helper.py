import datetime
from random import randrange

def time_parse() -> int:
    currentDT = datetime.datetime.now()
    #print("current Hour is: %d" % currentDT.hour)
    #print("current Minute is: %d" % currentDT.minute)
    hour = currentDT.hour
    minutes = currentDT.minute

    if hour >= 16 or hour <= 2:
        return 1
    else:
        return 0

def age_paser(age: int) -> int:
    if age >= 21:
        return 1
    else:
        return 0

def age_generator() -> int:
    randomNum = randrange(1, 11)
    if randomNum > 7:
        return 23
    else:
        return 16
