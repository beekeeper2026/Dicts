import pgzrun

WIDTH=900
HEIGHT=800

question_box = Rect(20, 100, 680, 150)
answer_box_1 = Rect(20, 350, 300, 150)
answer_box_2 = Rect(400, 350, 300, 150)

def draw():
    screen.fill("LightSeaGreen")
    screen.draw.filled_rect(question_box, "DarkOliveGreen2")
    screen.draw.filled_rect(answer_box_1, "Black")
    screen.draw.filled_rect(answer_box_2, "Black")
    


def update():
    pass


pgzrun.go()