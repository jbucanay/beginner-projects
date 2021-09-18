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
    print(sorted)



def sortNumbers():
    userNums = input('how many random numbers do you want to sort').strip()
    numsInt = int(userNums)
    randNums = []
    sortedNums = []
    for nums in range(numsInt):
        randNums.append(random.choice(string.digits))
    print(randNums)
    counter = -1
    while counter <= len(randNums):
        take = min(set(randNums))
        print(take)
        indexIt = randNums.index(take)
        popOff = randNums.pop(indexIt)
        sortedNums.append(popOff)
        print(f'{randNums}randNums')
        counter +=1
    print(sortedNums)











