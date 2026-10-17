import pgzrun, random, time

WIDTH=800
HEIGHT=580
lines=[]
sats=[]
start_time=time.time()
end_time=0
display_time=0
current_sat=0


for i in range(8):
    sat=Actor("sat")
    sat.pos=(random.randint(50, 750), random.randint(50, 530))
    sats.append(sat)

def draw():
    global display_time
    numbers=1
    screen.blit("galaxy", (0, 0))
    for sat in sats:
        sat.draw()
        screen.draw.text(str(numbers), (sat.pos[0], sat.pos[1]+20))
        numbers+=1
    for line in lines:
        screen.draw.line(line[0], line[1], "Red")
    if current_sat < 8:
        display_time= round((time.time() - start_time), 1)
    screen.draw.text(str(display_time), center=(20, 20), color="Red")




def update():
    pass

def on_mouse_down(pos):
    global current_sat, lines, sats, start_time, end_time
    if current_sat < 8:
        if sats[current_sat].collidepoint(pos):
            if current_sat:
                lines.append((sats[current_sat-1].pos, sats[current_sat].pos))
            current_sat += 1
        else:
            current_sat = 0
            lines=[]



pgzrun.go()