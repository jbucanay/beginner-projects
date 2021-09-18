## sort the list of strings
## sort the list of numbers
import string
import random

def sortThis():
    userIn = input('how many ranom letters would you like to randomize?').strip()
    useNum = int(userIn)
    randlist = []
    sorted = []
    for letter in range(useNum):
        randlist.append(random.choice(string.ascii_letters.lower()))

## take every character and compare it with the next character
    n = 0
    while n <= len(randlist):
        print(n)
        n += 1




