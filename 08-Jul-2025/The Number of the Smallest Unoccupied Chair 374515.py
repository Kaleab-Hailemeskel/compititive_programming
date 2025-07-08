# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        s,e = defaultdict(list),defaultdict(list)
        mapp = defaultdict(int)
        h = list(range(len(times)))
        miny = float('inf')
        maxy = float('-inf')

        for i,val in enumerate(times):
            start,end = val
            s[start].append(i)
            e[end].append(i)
            miny= min(miny,start,end)
            maxy= max(maxy,start,end)
       
        for i in range(miny,maxy+1):
            for person in e[i]:
                heappush(h,mapp[person])
                del mapp[person]
            for person in s[i]:
                mapp[person] = heappop(h)
                if person == targetFriend:
                    return mapp[person]