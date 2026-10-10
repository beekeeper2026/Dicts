import pgzrun, random, time

WIDTH=800
HEIGHT=580
sats=[]

for i in range(8):
    sat=Actor("sat")
    sat.pos=(random.randint(50, 750), random.randint(50, 530))
    sats.append(sat)

def draw():
    numbers=1
    screen.blit("galaxy", (0, 0))
    for sat in sats:
        sat.draw()
        screen.draw.text(str(numbers), (sat.pos[0], sat.pos[1]+20))
        numbers+=1





def update():
    pass


pgzrun.go()