class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        n = len(speed)
        for i in range(n):
            posSpeed.append((position[i], speed[i]))
        posSpeed.sort()
        lastMaxSpeed = ((target - posSpeed[-1][0]) / posSpeed[-1][1])
        posSpeed.pop()
        fleet = 1
        while posSpeed:
            ps = posSpeed.pop()
            numOfSteps = ((target - ps[0]) / ps[1])
            if  numOfSteps > lastMaxSpeed:
                lastMaxSpeed = numOfSteps
                fleet += 1

        return fleet
