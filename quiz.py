import pgzrun

WIDTH=900
HEIGHT=800
questions=[]
question=[]


question_box = Rect(20, 100, 680, 150)
answer_box_1 = Rect(20, 350, 300, 150)
answer_box_2 = Rect(400, 350, 300, 150)
answer_box_3 = Rect(400, 600, 300, 150)
answer_box_4 = Rect(20, 600, 300, 150)
timer_box = Rect(750, 125, 100, 100)
skip_box = Rect(750, 350, 100, 400)

answer_boxes=[answer_box_1, answer_box_2, answer_box_3, answer_box_4]

def draw():
    screen.fill("LightSeaGreen")
    screen.draw.filled_rect(question_box, "DarkOliveGreen2")
    screen.draw.filled_rect(answer_box_1, "Black")
    screen.draw.filled_rect(answer_box_2, "Black")
    screen.draw.filled_rect(answer_box_3, "Black")
    screen.draw.filled_rect(answer_box_4, "Black")
    screen.draw.filled_rect(timer_box, "Yellow")
    screen.draw.filled_rect(skip_box, "Blue")

    screen.draw.textbox("SKIP", skip_box, color="Black", angle=-90)
    screen.draw.textbox(question[0], question_box, color="Black")
    screen.draw.textbox(question[1], answer_box_1, color="White")
    screen.draw.textbox(question[2], answer_box_2, color="White")
    screen.draw.textbox(question[3], answer_box_3, color="White")
    screen.draw.textbox(question[4], answer_box_4, color="White")
    


def update():
    pass


def read_q_file():
    file=open("questions.txt", "r")
    for line in file:
        questions.append(line)
    file.close()

def read_q():
    global question
    question=questions.pop(0).split(",")

read_q_file()
read_q()
print(question)


def on_mouse_down(pos):
    answer=question[5]
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index==int(answer):
                read_q()
        index+=1




pgzrun.go()