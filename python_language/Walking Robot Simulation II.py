class Robot:
    DIRS = ['North', 'East', 'South', 'West']
    def __init__(self, width: int, height: int):
        self.width = width
        self.height=height
        self.dir = 1
        self.steps = 0

    def turn(self) -> None:
        self.dir = (self.dir+3) % 4
        
    def step(self, num: int) -> None:
        self.steps+=num

    def getPos(self) -> List[int]:
        delta = self.steps%(self.width*2+self.height*2 -4)
        if delta < self.width:
            return [delta, 0]
        elif delta < self.width + self.height-1:
            return [self.width-1, delta-self.width+1]
        elif delta < self.width * 2 + self.height - 2:
            return [self.width * 2 + self.height - 3 - delta, self.height-1]
        else:
            return [0, self.width*2+self.height*2 -4 - delta]

    def getDir(self) -> str:
        delta = self.steps%(self.width*2+self.height*2 -4)
        if delta == 0 and self.steps>0:
            return 'South'
        if delta < self.width:
            return 'East'
        elif delta < self.width + self.height-1:
            return 'North'
        elif delta < self.width * 2 + self.height - 2:
            return 'West'
        else:
            return 'South'
            self.turn += 1
        
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
