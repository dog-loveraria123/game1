import pgzrun
import time
import random
WIDTH=600
HEIGHT=350
#putting background image
satellite=Actor('stellite.png')
satellites
def duplicate():
    for i in range(8):
        satellite=Actor('stellite.png')    
        satellite.x=random.randint(150,500)
        satellite.y=random.randint(150,300)
def draw():
    screen.blit('background.jpg',(0,0))
    satellite.draw()
def update():
    pass
pgzrun.go()