from sys import maxsize
def findMaximum(arr):
    arr_max = -maxsize-1
    for i in range(0,len(arr)):
        if(arr[i] > arr_max):
            arr_max = arr[i]

    return arr_max

a = [-2,5,-9,-10,10,111111110,-2000000]
print("The Maximum number is:", findMaximum(a))


def linearSearch(arr, val):
    curr_index = 0
    found = False
    while (curr_index < len(arr)):
        if (arr[curr_index] == val):
            found = True
            break

        curr_index = curr_index+1

    if(found):
        return curr_index
    else:
        return -1

a = [1,2,6,19,-20,41,0]
print("The linear search index is:",linearSearch(a,41))



#[2,4,6,8,10,12,13] target = 12

def binarySearch(arr,val):
    arr = sorted(arr)
    right = len(arr)-1
    left = 0

    while(left <= right):
        middle = (right+left)//2
        if(arr[middle]<val):
            left = middle+1
        elif (arr[middle]>val):
            right = middle-1
        else:
            return middle
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 40

print("The binary search index is:",binarySearch(arr,x))


def bubbleSort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


arr = [54, 39, 28, 2, 222, 101, 97]

print("Bubble sort:", bubbleSort(arr))


#[1,-2,5,16]
def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while(j >= 0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp
    return arr



arr = [64, 34, 25, 12, 22, 11, 7]

print("Insertion sort",insertionSort(arr))



#target value = 110
#[50,40,30,20,10]

#[50,50,10]

def changeMakingCoin(arr,val):
    arr = sorted(arr, reverse = True)
    toReturn = []

    for i in range(0,len(arr)):
        while(val>=arr[i]):
            val = val-arr[i]
            toReturn.append(arr[i])
    return toReturn;


a = int(input("How many cents is the change?"))
arr = [25,10,5,1]
print("Coins needed",changeMakingCoin(arr,a))



