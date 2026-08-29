import pgzrun, random

WIDTH = 500
HEIGTH = 500
size = 100

def draw():
    global size
    for i in range(5):
        red =random.randint(0, 255)
        blue =random.randint(0, 255)
        green =random.randint(0, 255)
        screen.draw.filled_circle((250, 250), size, (red, blue, green))
        size -= 20

def update():
    pass

pgzrun.go()