import random
import pgzrun
#Screen size
WIDTH=600
HEIGHT=338
#gaming variables
go=False
yw=True
levels=1
totallevels=10
current=[]
speed=5
acualtarget=None
listofall=['bear.png','bird.png','bunny.png','cat.png','Dog.png','tiger.png']
def draw():
    screen.blit('main bg.jpg',(0,0))
    #gameover/gamewin
    if go==True:
        screen.blit('lose bg.jpg',(0,0))
    elif yw==True:
        screen.blit('win bg.jpg',(0,0))
pgzrun.go()