def heapify(data, n, i, swaps):
    minIndex = i
    leftChild = 2*i+1
    if leftChild < n and data[leftChild] < data[minIndex]:
        minIndex = leftChild

    rightChild = 2*i+2
    if rightChild < n and data[rightChild] < data[minIndex]:
        minIndex = rightChild

    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append((i, minIndex))
        heapify(data, n, minIndex, swaps)


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n-1, -1, -1):
        heapify(data, n, i, swaps)

    return swaps


def main():
    ##n = int(input())
    ##data = list(map(int, input().split()))

    ##assert len(data) == n

    ##swaps = build_heap(data)



    ##print(len(swaps))
    ##for i, j in swaps:
        ##print(i, j)

    file = input()
    file = ("tests/" + file)
    if 'a' not in file:
        with open(file, 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
            data = list(map(int, lines[1].split()))
            assert len(data) == n

            swaps = build_heap(data)



            print(len(swaps))
            for i, j in swaps:
                print(i, j)

if __name__ == "__main__":
    main()