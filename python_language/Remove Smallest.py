ansArrString = []
for i in range(0, int(input())):
    arr = []
    ansString = "YES"
    cin = int(input())
    if cin != 1:
        nums = input()
        arr =[ eval(i) for i in nums.split(" ")]
        arr.sort()
        size = len(arr)
        countPossibleRemoval = 0
        for k in range(1, size):
            if abs(arr[k] - arr[k - 1]) < 2:
                countPossibleRemoval += 1
                if(countPossibleRemoval + 1 >= size):
                    ansString = "YES"
                    break
        if countPossibleRemoval + 1 < size:
            ansString = "NO"
    else:
        h = int(input())
 
    ansArrString.append(ansString)
 
for word in ansArrString:
    print(word)
