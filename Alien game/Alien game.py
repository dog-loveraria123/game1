import pgzrun
import random
WIDTH=500
HEIGHT=500
a= Actor('dog.png')
a.x=250
a.y=250
m='Dog Clicker Game'
def draw():
    screen.fill('light blue')
    a.draw()
    screen.draw.text(m,(30,20),fontsize=30,color='black')
# function for random position
def rp():
    a.x=random.randint(50,450)
    a.y=random.randint(50,450)
    clock.schedule(mc,2.0)
clock.schedule_interval(rp,2.0)
def mc():
    global m 
    m='You Missed!'
    rp()
def on_mouse_down(pos):
    global m
    if a.collidepoint(pos):
        m='Good Job!'
        clock.unschedule(mc)
        rp()
    else:
        m='You Missed!'
def update():
    pass
pgzrun.go()
