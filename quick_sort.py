

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(arr, start, end):
    '''
        example procedure:
            arr = [ 2 8 7 1 3 5 6 4]
            2 1 3 8 7 5 6 4
        start   i       j end -> j <= end - 1

            2 1 3 4 7 5 6 8
        start   i         end -> arr[i+1] <-> arr[end]
    '''
    val = arr[end]
    i = start - 1

    for j in range(start, end):  # j = start to end - 1
        if arr[j] <= val:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, end)

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)  # Divide
        # Conquer
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def example():
    arr = [None, 2, 8, 7, 1, 3, 5, 6, 4]
    length = len(arr) - 1
    quick_sort(arr, 1, length)
    sorted_array = arr[1:]

    print(sorted_array)


if __name__ == "__main__":
    example()
