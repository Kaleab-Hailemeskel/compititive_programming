itt = int(input())
for i in range(itt):
    size = int(input())
    arr = list(map(int, input().split(" ")))
    pos = True
    LOW = -10 ** 9
    maxInTheSet = arr[0]
    aSum = 0
    for i in range(1, size):
        if arr[i] * arr[i - 1] >= 0:
            maxInTheSet = max(maxInTheSet, arr[i])
        else:
            aSum += maxInTheSet
            maxInTheSet = arr[i]
    
    print(aSum + maxInTheSet)

    
