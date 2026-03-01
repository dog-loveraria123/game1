import pgzrun
import random
WIDTH=600
HEIGHT=400
dog=Actor('dog.png')
treat=Actor('dog biscut.png')
s=0
def draw():
    #putting Background image
    screen.blit('background.jpg',(0,0))
    dog.draw()
    treat.draw()
    screen.draw.text('Score:'+str(s),midtop=(300,20),fontsize=40)
def rt():
    treat.x=random.randint(10,550)
    treat.y=random.randint(10,390)
def update():
    if keyboard.left:
        if dog.x>50:
           dog.x-=5
    if keyboard.right:
         if dog.x<550:
             dog.x+=5
    if keyboard.up:
        if dog.y>50:
           dog.y-=5
    if keyboard.down:
        if dog.y<350:
           dog.y+=5
    #treat collection
    if dog.colliderect(treat):
        rt()
rt()
pgzrun.go()
