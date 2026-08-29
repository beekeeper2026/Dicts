import pgzrun, random

WIDTH=600
HEIGHT=600
rwidth = 500
rheight = 300

def draw():
    global rwidth, rheight
    #screen.fill("Black")
    for i in range(5):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        r = Rect((0, 0),(rwidth, rheight))
        r.center = 300, 300
        screen.draw.rect(r, (red, green, blue))
        rwidth -= 10
        rheight += 10

def update():
    pass

pgzrun.go()