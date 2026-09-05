import pgzrun

WIDTH = 800
HEIGHT = 800
x = 0
y = 0

def draw():
    global x, y
    #  row 1
    for i in range(8):
        x=0
        for j in range(8):
            if (i + j) % 2 == 0:
                r = Rect((x, y), (100, 100))
                screen.draw.filled_rect(r, "White")
            x += 100
        y+=100
        

def update():
    pass


pgzrun.go()