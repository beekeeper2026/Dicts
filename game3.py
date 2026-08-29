import pgzrun

WIDTH = 800
HEIGTH = 800
x = 0
y = 0

def draw():
    global x, y
    for i in range(8):
        r = Rect((x, y), (50, 50))
        screen.draw.filled_rect(r, "White")
        x += 100



def update():
    pass


pgzrun.go()