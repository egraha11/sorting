import copy;


#selection sort
def selectionSort(array):

    for i in range(len(array)):

        for j in range(i, len(array)):

            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

    printAll(array)


#bubblesort
def bubbleSort(array):

    for i in range(len(array)):
        sorted = True

        for j in range((len(array) - 1 - i)):

            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False

        if sorted == True:
            break

    printAll(array)


#insertionsort
def insertionSort(array):

    for i in range(1, len(array)):

        value = array[i]

        j = i - 1

        while(j >= 0 and array[j] < value):
            array[j + 1] = array[j]

            j-= 1

        array[j + 1] = value

    printAll(array)


def printAll(array):
    print(array)




array = [66, 44, 3, 76, 90, 12, 8, 21, 54]



selectionSort(copy.deepcopy(array))
bubbleSort(copy.deepcopy(array))
insertionSort(copy.deepcopy(array))


