class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = [0] * (max(chain(*matches)) + 1 )
        for player in matches:
            winner = player[0]
            losser = player[1]
            if players[winner] == 0:
                players[winner] += 1

            if players[losser] == 1:
                players[losser] = -1

            else:
                players[losser] -= 1

        no_loose = []
        one_loose = []
        for i in range(len(players)):
            if players[i] == 1:
                no_loose.append(i)
            elif players[i] == -1:
                one_loose.append(i)

        return [no_loose,one_loose]
