class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        pi, ti = 0, 0
        ts, ps = len(trainers), len(players)
        while ti < ts and pi < ps:
            while pi < ps and players[pi] > trainers[ti]:
                pi += 1
            if pi >= ps:
                break
            pi += 1
            ti += 1
        return ti
                
            
        
