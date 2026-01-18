import pgzrun
#screen dimensions
WIDTH=500
HEIGHT=400
def draw():
    #changing the screen color
    screen.fill('lavender')
    a=Rect((250,200),(100,50))
    a.center=250,200
    #function for drawing rectangle
    screen.draw.rect(a,'turquoise',width=3)
    #square
    b=Rect((300,300),(100,100))
    screen.draw.filled_rect(b,('purple'))
#showing the screen
pgzrun.go()