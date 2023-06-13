# Hardcoded target value of 10
def isCorrect(n, target):
    if n > target:
        return 1
    elif n < target:
        return -1
    else:
        return 0

def binarySearch(low, high, target):
    while (low <= high):
        mid = (low + high) // 2
        # Guess is too high
        if isCorrect(mid, target) > 0:
            high = mid -1
        # Guess is too low
        elif isCorrect(mid, target) < 0:
            low = mid + 1
        # Guess is correct
        else:
            return mid
    return -1


def main():
    bs = binarySearch(0, 100, 14)
    print(bs)




if __name__ == "__main__":
    main()