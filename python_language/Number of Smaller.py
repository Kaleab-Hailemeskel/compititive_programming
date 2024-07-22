size1, size2 = map(int, input().split(" "))
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))
index1 = 0
for index2 in range(size2):
    while index1 < size1 and arr1[index1] < arr2[index2]:
        index1 += 1
    print(index1, end = " ")

# after some time

n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
ans = [0] * m
i, k = 0, 0
for j in range(m):
    while i < n and arr_1[i] < arr_2[j]:
        i += 1
    ans[j] = i
print(* ans)

    
