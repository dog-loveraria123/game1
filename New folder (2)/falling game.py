import random
import pgzrun
#Screen size
WIDTH=600
HEIGHT=338
#gaming variables
go=False
yw=False
levels=1
totallevels=10
current=[]
speed=5
actualtarget=None
listfall=['bear.png','bird.png','bunny.png','cat.png','Dog.png','tiger.png']
def draw():
    screen.blit('main bg.jpg',(0,0))
    #gameover/gamewin
    if go==True:
        screen.blit('lose bg.jpg',(0,0))
    elif yw==True:
        screen.blit('win bg.jpg',(0,0))
#Function fo falling items
def falling(levels):
    global actualtarget
    temp=[]
    actualtarget=random.choice(listfall)
    #List for extra items
    extra=random.choices([i for i in listfall if i != actualtarget],k=levels)
    option=[actualtarget]+extra
    random.shuffle(option)
    size=WIDTH/(len(option)+1)
    for u, img in enumerate(option):
        actor=Actor(img)
        actor.active=True
        actor.x=(u+1)*size
pgzrun.go()
