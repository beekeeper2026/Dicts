import pgzrun

WIDTH=900
HEIGHT=800
questions=[]
question=[]
time_left=10
score=0
game_over=False

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
    screen.draw.textbox(str(time_left), timer_box, color="Black")
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
    if questions:
        question=questions.pop(0).split(",")
    else:
        lost()

read_q_file()
read_q()
print(question)


def on_mouse_down(pos):
    global time_left, score
    answer=question[5]
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index==int(answer):
                score+=1
                read_q()
                time_left=10
            else:
                lost()
        index+=1
    if skip_box.collidepoint(pos) and game_over==False:
        read_q()
        time_left=10

def update_timer():
    global time_left
    if time_left > 0 and game_over==False:
        time_left-=1
    else:
        lost()

def lost():
    global time_left, question, score, game_over
    game_over=True
    question=["GAME OVER YOUR SCORE IS: "+str(score), " ", " ", " ", " ", 0]
    time_left=0



clock.schedule_interval(update_timer, 1)


pgzrun.go()