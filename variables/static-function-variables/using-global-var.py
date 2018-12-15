#!/usr/bin/python3

sumNow = 0
def summingUp(num):
    global sumNow

    print(str(sumNow) + ' + ' + str(num) + ' = ' + str(sumNow + num))
    sumNow += num

summingUp( 7)
summingUp(22)
summingUp(18)

