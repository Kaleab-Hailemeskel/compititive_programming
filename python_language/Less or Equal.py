cin = input()
size = int((cin.split(" "))[0])
comp = int((cin.split(" "))[1])
strOfNums = input()
strOfNums = [eval(i) for i in strOfNums.split(" ")]
strOfNums.sort()
if comp == 0:
    print(-1 if strOfNums[0] == 1 else strOfNums[0] - 1)
elif comp == len(strOfNums):
    print(strOfNums[comp - 1])
elif strOfNums[comp - 1] == strOfNums[comp]:
    print(-1)
else:
    print(strOfNums[comp - 1])
