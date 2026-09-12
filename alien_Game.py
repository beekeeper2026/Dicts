import pgzrun, random, time

WIDTH=500
HEIGHT=500

alien=Actor("alien")
alien.pos=(250, 250)

result="Hit the alien to start!"
score=0
start=time.time()
game_over=False

def draw():
    screen.fill("VioletRed4")
    alien.draw()
    screen.draw.text(result, center=(400, 50))
    screen.draw.text(str(score), center=(50, 20))
    if game_over == True:
        screen.fill("SkyBlue")
    
def update():
    global game_over
    updated_time=time.time()
    if updated_time-start>10:
        game_over=True


def on_mouse_down(pos):
    global result, score
    if alien.collidepoint(pos):
        result="Nice shot!"
        alien.pos=(random.randint(10, 490), random.randint(10, 490))
        score+=1
    else:
        result="Try again!"
        score-=1.5
        


pgzrun.go()

