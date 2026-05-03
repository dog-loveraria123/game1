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
listfall=['bear.png','bird.png','bunny.png','cat.png','dog.png','tiger.png']
actors=[]
def draw():
    screen.blit('main bg.jpg',(0,0))
    for item in actors:
        item.draw()
    #gameover/gamewin
    if go==True:
        screen.blit('lose bg.jpg',(0,0))
    elif yw==True:
        screen.blit('win bg.jpg',(0,0))
#Function fo falling items
def falling(levels):
    global actualtarget,actors
    temp=[]
    actualtarget=random.choice(listfall)
    #List for extra items
    extra=random.choices([i for i in listfall if i != actualtarget],k=levels)
    print(actualtarget,extra)
    option=[actualtarget]+extra
    random.shuffle(option)
    size=WIDTH/(len(option)+1)
    xc=100
    for u, img in enumerate(option):
        actor=Actor(img)
        actor.active=True
        actor.x=(xc)
        actor.y=(50)   
        actors.append(actor)
        xc=xc+400
falling(1)
def on_mouse_down(pos):
    global yw,go
    for item in actors:
        if item.collidepoint(pos):
            if (item.image)==actualtarget:
                yw=True
            else:
                go=True
pgzrun.go()
