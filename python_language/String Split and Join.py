def split_and_join(line):
    splited = line.split(" ")
    ans = ""
    for aWord in splited:
        ans += aWord
        ans += '-'
        
    ans = ans[0:len(ans) - 1]
    return ans
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
