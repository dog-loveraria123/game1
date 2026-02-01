import pgzrun
import random
WIDTH=500
HEIGHT=500
a= Actor('dog.png')
a.x=250
a.y=250
def draw():
    screen.fill('light blue')
    a.draw()
    screen.draw.text('Dog Clicker Game',(30,20),fontsize=30,color='black')
# function for random position
def rp():
    a.x=random.randint(50,450)
    a.y=random.randint(50,450)
clock.schedule_interval(rp,2.0)
def update():
    pass
pgzrun.go()