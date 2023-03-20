def heapify(data, m, i, swaps):
    minIndex = i
    leftChild = 2*i+1
    if leftChild < m and data[leftChild] < data[minIndex]:
        minIndex = leftChild

    rightChild = 2*i+2
    if rightChild < m and data[rightChild] < data[minIndex]:
        minIndex = rightChild

    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append((i, minIndex))
        heapify(data, m, minIndex, swaps)


def build_heap(data):
    swaps = []
    m = len(data)
    for i in range(m-1, -1, -1):
        heapify(data, m, i, swaps)

    return swaps


def main():
    n = input()
    m = int(n.strip())
    data = list(map(int, input().split()))

    #assert len(data) == m

    swaps = build_heap(data)



    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    

if __name__ == "__main__":
    main()