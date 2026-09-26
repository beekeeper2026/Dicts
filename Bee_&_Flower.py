import pgzrun, random, time

WIDTH=600
HEIGHT=500
start_time=time.time()
updated_time=0
score=0

bee=Actor("bee")
bee.pos=(100, 250)

flower=Actor("flower")
flower.pos=(300, 250)

def draw():
    screen.blit("background", (0, 0))   
    bee.draw()
    flower.draw()
    if updated_time-start_time > 10:
        screen.fill("firebrick")
        screen.draw.text("Your final score is: " + str(score), center=(100, 30))

def update():
    global updated_time, score
    updated_time=time.time()
    

    if keyboard.left and bee.x > 0:
        bee.x=bee.x-2
    if keyboard.right and bee.x < 600:
        bee.x=bee.x+2
    if keyboard.down and bee.y < 500:
        bee.y=bee.y+2
    if keyboard.up and bee.y > 0:
        bee.y=bee.y-2

    if bee.colliderect(flower):
        flower.pos=(random.randint(0, 600), random.randint(0, 500))
        score+=1


pgzrun.go()