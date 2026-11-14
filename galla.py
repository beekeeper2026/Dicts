import pgzrun

WIDTH=600
HEIGHT=600
bullets=[]
bees=[]
di=1

ship=Actor("ship")


ship.pos=(300, 500)


def draw():
    screen.clear()
    screen.fill("Black")
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for row in range(5):
        for col in range(5):
            bee=Actor("attackbee")
            bees.append(bee)
            bees[-1].x=50+70*row
            bees[-1].y=50+50*col
    for bee in bees:
        bee.draw()

def update():
    global di
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5
    if keyboard.SPACE:
        bullet=Actor("gun")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y
    for bullet in bullets:
        bullet.y-=10
    #if len(bees) > 0 and (bees[-1].x > WIDTH or bees[-1].x < 0):
        #di = di*-1
    for bee in bees:
        bee.x+=5*di


pgzrun.go()