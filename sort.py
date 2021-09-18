## sort the list of strings
## sort the list of numbers
import string
import random


def sortLetters():
    userIn = input('how many ranom letters would you like to randomize?').strip()
    useNum = int(userIn)
    randlist = []
    sorted = []
    for letter in range(useNum):
        randlist.append(random.choice(string.ascii_letters.lower()))

    count = -1
    print(randlist)
    while count <= len(randlist):

        taken = min(randlist)
        indx = randlist.index(taken)
        popIt = randlist.pop(indx)
        sorted.append(popIt)


        count += 1
    print(string.digits)
    return sorted










