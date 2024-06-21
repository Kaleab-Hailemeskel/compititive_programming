# Enter your code here. Read input from STDIN. Print output to STDOUT
lang = []
for i in range(2):
    input()
    lang.append(set(map(int, input().split())))

print(len(lang[0].union(lang[1])))
