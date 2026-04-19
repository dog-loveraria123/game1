import pgzrun
import time
import random
WIDTH=600
HEIGHT=350
#putting background image
sl=[]
st=0
tt=0
et=0
sc=0
l=[]
def duplicate():
    global st
    for i in range(8):
        satellite=Actor('stellite.png')    
        satellite.x=random.randint(50,550)
        satellite.y=random.randint(50,300)
        sl.append(satellite)
    st=time.time()
def draw():
    global tt
    screen.blit('background.jpg',(0,0))
    cn=1
    for i in sl:
        i.draw()
        screen.draw.text(str(cn),(i.pos[0],i.pos[1]-10),color='darkred')
        cn=cn+1
    for ld in l:
        screen.draw.line(ld[0],ld[1],'darkred')
    if sc<8:
        tt=(time.time())-st
        screen.draw.text(str(round(tt,1)),(0,0),color='pink')
    else:
        screen.draw.text(str(round(tt,1)),(0,0),color='pink')
#Function for Mouse Event
def on_mouse_down(pos):
    global sc,l
    if sc<8:
        if sl[sc].collidepoint(pos):
            if sc:
                l.append((sl[sc-1].pos,sl[sc].pos))
            sc=sc+1
        else:
            l=[]
            sc=0
def update():
    pass
duplicate()
pgzrun.go()
