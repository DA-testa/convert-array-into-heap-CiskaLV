# python3
import math


def build_heap(n, data):
    swaps = []

    def swap(child, parent):
        if (data[parent] <= data[child]):
            return None
        data[child], data[parent] = data[parent], data[child]
        return (child, parent)

    for i in range(n - 1, -1, -1):
        parent = math.floor((i - 1) / 2)

        while parent >= 0:
            swap_i = swap(i, parent)
            if swap_i is not None:
                swaps.append(swap_i)
            i = parent
            parent = math.floor((i - 1) / 2)

    return swaps


def main():
    text = input()
    number = 0
    if text[0] == "I":
        print("Enter number of nodes: ")
        number = int(input())
        data = list(map(int, input().split()))

    elif text[0] == "F":
        fileName = input()
        if "a" in fileName:
            print("Invalid file name")
            return
        else:
            if "tests/" not in fileName:
                fileName = "tests/" + fileName
            file = open(fileName, "r")
            number = int(file.readline())
            data = list(map(int, file.readline().split()))

    else:
        print("Invalid input")
        return

    assert len(data) == number
    swaps = build_heap(number ,data)

    # output all swaps

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
