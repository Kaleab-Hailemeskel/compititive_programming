n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
ans = [0] * (n + m)
l, r, k = 0, 0, 0
while l < n and r < m:
    if arr_1[l] < arr_2[r]:
        ans[k] = arr_1[l]
        l += 1
    else:
        ans[k] = arr_2[r]
        r += 1
    k += 1
while l < n:
    ans[k] = arr_1[l]
    l += 1
    k += 1
while r < m:
    ans[k] = arr_2[r]
    r += 1
    k += 1
    
print(*ans)
