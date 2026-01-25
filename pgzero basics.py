import pgzrun
import random
#screen dimensions
WIDTH=500
HEIGHT=400
def draw():
    w=500
    h=200
    screen.fill('black')
    r=255
    g=random.randint(0,255)
    b=0
    for i in range(25):
        
    #changing the screen color
        a=Rect((250,200),(w,h))
        a.center=250,200
        #function for drawing rectangle
        screen.draw.rect(a,(r,g,b))
        r-=5
        b+=5
        w-=15
        h+=7


#showing the screen
pgzrun.go()
