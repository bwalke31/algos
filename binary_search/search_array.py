
def binarySearch(arr, target):
    L = 0
    R = len(arr) - 1

    while (L <= R):
        mid = (L + R) // 2
        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else: 
            return mid
    return -1


def main():
    arr = [1,2,3,4,5,6,7,8]
    target = 7
    bs = binarySearch(arr, target)
    print(bs)




if __name__ == "__main__":
    main()