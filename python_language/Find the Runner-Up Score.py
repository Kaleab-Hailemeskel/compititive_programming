if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    n = n - 1
    i = n - 1
    while i > 0 and arr[n] == arr[i]:
        i -= 1
    print(arr[i])
