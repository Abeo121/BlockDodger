import pygame
import time
import random
pygame.font.init()
pygame.init()

class Player():
    def __init__(self, color):
        self.color =  color 

        self.xLoc = 200
        self.yLoc = 500

    def draw(self, surface):
        self.PlayerObject = pygame.draw.rect(surface, self.color, (  self.xLoc, self.yLoc,
                                                                    25, 25 ))
    def CheckCollision(self, Walls):
        Collided = self.PlayerObject.collidelist(Walls)

        if Collided == -1:
            return False
        return True
        



TimeElapsed = 2
class Obstacle():
    
    def __init__(self, Gap, WindowWidth, WindowHeight):
        self.gap = Gap

        self.WinWidth = WindowWidth

        self.WinHeight = WindowHeight


        self.xLoc = random.randint(0, WindowWidth - Gap)
        self.yLoc = 0
        
        ResetTimer()
        
    def draw(self, surface, Color):
        if self.yLoc < self.WinHeight:
            self.rWall = pygame.draw.rect(surface, Color, (  self.WinWidth - self.xLoc, self.yLoc,
                                                self.xLoc, 50 ))

            self.lWall = pygame.draw.rect(surface, Color, (  0, self.yLoc,
                                                self.WinWidth - self.xLoc - self.gap, 50 ))
            self.yLoc += .3

        
            

def CanMakeWall():

    if TimeElapsed > 3:
        return True
    else:
        return False

def ResetTimer():
    global TimeElapsed
    TimeElapsed = 0


        

def MakeWall(Gap : int, winWidth, winHeight):

    wall = Obstacle(50, winWidth, winHeight)
    return wall




def CheckEvents():
    run = True;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    return run
    


def run(WindowWidth : int, WindowHeight : int ):

    global TimeElapsed
    
    win = pygame.display.set_mode((WindowWidth, WindowHeight))

    WallObstacles = []

    player = Player((0,255,0))
    
    x = WindowWidth -40
    y =100
    width = 40
    height = 60
    vel = 5
    ShouldRun =True
    ShouldNewWall = True
    while ShouldRun:

        StartTime = time.time()
        ShouldRun = CheckEvents()
        #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    

        if TimeElapsed > 2:
            Wall = MakeWall(10, WindowWidth,WindowHeight)

            WallObstacles.append(Wall)

        for wall in WallObstacles:
            wall.draw(win, (255,0,0))
        
        player.draw(win)
        pygame.display.update()
        pygame.display.flip()
        win.fill((0,0,0))

        DeltaTim = time.time() - StartTime
        WallRects = []

        for wall in WallObstacles:
            WallRects.append(wall.rWall)
            WallRects.append(wall.lWall)

        print(player.CheckCollision(WallRects))
        TimeElapsed += DeltaTim




run(400, 600)