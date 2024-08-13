class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def backtrack(index, ip):
            if index >= n:
                if len(ip) != 4:
                    return
                ans.append(".".join(ip))           
            
            for i in range(index, n):
                valid = s[index : i + 1]
                if int(valid) > 255 or (i > index and valid[0] == '0'): # i > index means it is that it has more than 1 digits in valid var
                    continue
                ip.append(valid)
                backtrack(i + 1, ip)
                ip.pop()
        backtrack(0, [])
        return ans
                        
                    
