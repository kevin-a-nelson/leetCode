import math


def isMonotonic(array):
    isDecreasing = True
    prevNum = math.inf
    for num in array:
        if num > prevNum:
            isDecreasing = False
            break
        prevNum = num

    isIncreasing = True
    prevNum = -math.inf
    for num in array:
        if num < prevNum:
            isIncreasing = False
            break
        prevNum = num

    return isDecreasing or isIncreasing


isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
