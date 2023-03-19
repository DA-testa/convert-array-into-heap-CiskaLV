# python3
import math
def build_heap(data):
    swaps = []

    def swap(child, parent):
        if (data[parent] >= data[child]):
            data[child], data[parent] = data[parent], data[child]
            swaps.append((parent,child))

    upsideDown = reversed(data)
    for i in upsideDown:
        element = data.index(i)

        while element != 0:
            parent = math.floor((element - 1) / 2)
            swap(element,parent)

            element = parent

    return swaps


def main():
    text = input()
    number = int
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
            if "test/" not in fileName:
                fileName = "test/" + fileName
            file = open(fileName, "r")
            number = int(file.readline())
            data = list(map(int, file.readline().split()))

    else:
        print("Invalid input")
        return

    assert len(data) == number
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
