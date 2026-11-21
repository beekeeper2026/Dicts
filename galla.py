import pgzrun

WIDTH=600
HEIGHT=600
bullets=[]
bees=[]
di=1
score=0
game=False

ship=Actor("ship")


ship.pos=(300, 500)

for row in range(5):
        for col in range(5):
            bee=Actor("attackbee")
            bees.append(bee)
            bees[-1].x=50+70*row
            bees[-1].y=50+50*col
    
def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("gun")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y
      

def update():
    global di, game, score, bees
    move_down=False
    if keyboard.left and ship.x >50:
        ship.x-=5
    if keyboard.right and ship.x <550:
        ship.x+=5
    for bullet in bullets:
        bullet.y-=10
    if len(bees) > 0 and (bees[-1].x > WIDTH or bees[-1].x < 0):
        move_down=True
        di = di*-1
    for bee in bees:
        bee.x+=5*di
        if move_down==True:
            bee.y+=100
        #if bee.y > 600:
            #bees.remove(bee)
        for bullet in bullets:
             if bullet.colliderect(bee):
                  bullets.remove(bullet)
                  bees.remove(bee)
                  score+=1
        if bee.colliderect(ship):
            game=True
             

def draw():
    screen.clear()
    screen.fill("Black")
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for bee in bees:
        bee.draw()
    if game==True:
        screen.fill("Red")
        screen.draw.text("You lost! Your final score is: " + str(score), center=(300, 300))
    if len(bees)==0:
        screen.fill("Blue")
        screen.draw.text("You won! Your final score is: " + str(score), center=(300, 300))

        


pgzrun.go()