# arrays.py
# Author: Michael Reeve
# Date: 7/16/19

def sortArray(arr):
    n = len(arr)-1
    for i in range(0, n):
        for j in range(0, n):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
    return arr

def binarySearch(arr,search):
    left = 0
    right = len(arr)-1
    while (left <= right):
        mid = (left + right) / 2
        if(arr[mid] == search):
            return True
        elif (search < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return False


def findIndexes(arr, num):
    if(not binarySearch(arr,num)): return [-1]
    
    index = arr.index(num)
    count = 1
    indexes = [count]
    current = arr[index]
    indexes.append(index)
    while (current == num):
        if(index+1 > len(arr)-1): break
        if(arr[index + 1] != num): break
        index += 1
        current = arr[index]
        indexes.append(index)
        count+=1
    indexes[0] = count
    return indexes


inputArr = []

sentinal = True

print("Enter numbers, followed by return, to add to an array, stop by entering '*'")

while sentinal:
    inputted = raw_input()
    if(inputted == "*"):
        sentinal = False
        break
    numTest = True
    isNum = False
    try:
        inputted = int(inputted)
        isNum = True
    except ValueError:
        numTest = False
    if isNum and int(inputted) != inputted: numTest = False
    if not numTest:
        print("Please only enter whole numbers...")
    if(numTest):
        inputArr.append(inputted)

sorted = sortArray(inputArr)

print("Sorted Array: ")

for i in range(0,len(sorted)):
    print(sorted[i])

searchBool = raw_input("Would you like to search for a number in the array and get it's index?(Y/N): ")
while(searchBool == "Y" or searchBool == "y"):
    search = raw_input("What number are you trying to find the index of? ")  
    isNum = False
    while not isNum:
        isNum = True
        try:
            search = int(search)
        except ValueError:
            isNum = False
            print("Please only enter numbers...")
    
    output = findIndexes(sorted,search)
    if(output[0] <= 0):
        print(str(search)+ " does not exist in the array...")
    else:
        result = str(search) + " appeared " + str(output[0]) + " time(s) at position(s): "
        for i in range(1,len(output)):
            result += str(output[i]) + ", "
        result = result[:-2]
        print(result)
    searchBool = raw_input("Would you like to search for another number?(Y/N): ")
