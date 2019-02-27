def bubble_sort(array, tag):
    if array is not None:
        length = len(array)
        if length == 1:
            pass
        else:
            for i in range(length - 1):
                for j in range(length - 1 - i):
                    if tag == "asc":
                        if array[j] > array[j + 1]:
                            array[j], array[j + 1] = array[j + 1], array[j]
                    if tag == "desc":
                        if array[j] < array[j + 1]:
                            array[j], array[j + 1] = array[j + 1], array[j]
    else:
        print("Null list")


def select_sort(array, tag):
    if array is not None:
        length = len(array)
        if length == 1:
            pass
        else:
            if tag == "asc":
                for i in range(length):
                    min_num = i
                    for j in range(i + 1, length - i):
                        if array[j] < array[min_num]:
                            min_num = j
                    if min_num != i:
                        array[min_num], array[i] = array[i], array[min_num]
            if tag == "desc":
                for i in range(length):
                    max_num = i
                    for j in range(i + 1, length - i):
                        if array[j] > array[max_num]:
                            max_num = j
                    if max_num != i:
                        array[max_num], array[i] = array[i], array[max_num]


def insert_sort(array):
    if array is not None:
        length = len(array)
        if length == 1:
            pass
        else:
            for i in range(1, length - 1):
                temp = array[i]
                for j in range(i):
                    if array[j] > array[i]:
                        for k in range(i, j, -1):
                            array[k] = array[k - 1]
                        array[j] = temp


if __name__ == '__main__':
    array = [1, 9, 4, 6, 3, 2, 10]
    print("Before sort array is : % s" % array)
    insert_sort(array)
    print("After sort array is : % s" % array)
