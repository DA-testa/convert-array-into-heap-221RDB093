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
    n = input()
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)



    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    

if __name__ == "__main__":
    main()