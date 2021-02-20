array = [1,34,56,100,-12,87,987,1,3,5,56,67]
shift = 4

def printArray(array):
    for i in range(0, len(array)):
        print(array[i], end=' ')

def leftRotation(array, shift):
    for j in range(0, shift):
        temp = array[0]  # saving First element in temp variable
        for j in range(0, len(array) - 1):  # shift remaining array elements one by one
            array[j] = array[j + 1]

        array[len(array) - 1] = temp
    return array

print("Array Before Rotation: ")
printArray(array)

rotatedArray = leftRotation(array, shift)
print("\nArray after left rotation: ")
printArray(rotatedArray)
