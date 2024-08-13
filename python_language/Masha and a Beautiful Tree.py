def swap(arr, left, right, size):
    for i in range(size):
        arr[left + i], arr[right+ i] = arr[right + i], arr[left + i]
itt = int(input())
for _ in range(itt):
    n = int(input())
    arr = list(map(int, input().split()))  
    count = 0
    jump = 2
    
    while jump <= n:
        comp = jump // 2
        for index in range(0, n, jump):
            if arr[index] > arr[index + comp]:
                count += 1
                swap(arr, index, index + comp, comp)
        jump *= 2
    
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            count = -1
            break
    print(count)
        
