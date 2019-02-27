def first_sort(numbers, i, j):
    temp = numbers[i]
    while i != j:
        while i < j and numbers[j] > temp:
            j = j - 1
        numbers[i] = numbers[j]
        while i < j and numbers[i] < temp:
            i = i + 1
        numbers[j] = numbers[i]
    numbers[i] = temp
    return i


def quick_sort(numbers, i, j):
    if i < j:
        middle = first_sort(numbers, i, j)
        quick_sort(numbers, i, middle - 1)
        quick_sort(numbers, middle + 1, j)


if __name__ == '__main__':
    list1 = [2, 7, 9, 3, 8, 5, 6, 54, 1, 42]
    print(list1)
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)
