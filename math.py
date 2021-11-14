# generate random integer values
from random import seed
from random import randint

skaViRakna = input("hello there will you learn math?")
if skaViRakna == "yes":
    print('yes so fun')
    whatmath = input("will you learn addition, subtraction or multiplication?")

    if whatmath == 'm':
        mTable = input("what multiplication table? ")
        aNumber = int(mTable)
        i = 1
        while i < 11:
            aNumber2 = randint(2, 10)
            actualAnswer = aNumber * aNumber2
            answer = False
            while answer == False:
                result = input(f'What is {aNumber} * {aNumber2}? ')
                if int(result) == actualAnswer:
                    print("Correct!")
                    answer = True
                    i = i + 1
                else:
                    print("wrong try again")
    elif whatmath == 's':
        i = 1
        while i < 11:  # How many correct answers before we end?
            aNumber = randint(10, 100)
            aNumber2 = randint(2, aNumber)
            actualAnswer = aNumber - aNumber2
            answer = False
            while answer == False:
                result = input(f'What is {aNumber} - {aNumber2}? ')
                if int(result) == actualAnswer:
                    print("Correct!")
                    answer = True
                    i = i + 1
                else:
                    print("wrong try again")
    elif whatmath == 'a':
        i = 1
        while i < 11:  # How many correct answers before we end?
            aNumber = randint(1, 200)
            aNumber2 = randint(1, 200)
            actualAnswer = aNumber + aNumber2
            answer = False
            while answer == False:
                result = input(f'What is {aNumber} + {aNumber2}? ')
                if int(result) == actualAnswer:
                    print("Correct!")
                    answer = True
                    i = i + 1
                else:
                    print("wrong try again")
else:
    print('ok bye')
