from tkinter import *
import random

win=Tk()
win.title("Snake Game")
win.resizable(False,False)

Label(win,text="SUBSCRIBE",font="arial 20 bold").pack(side=BOTTOM) #Footar
score=0
direction="down"

GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=180
SPACE_SIZE=50
BODY_PARTS=2
SNAKKE_COLOR="Green"
FOOD_COLOR="red"
BACKGROUND_COLOR="#000000"
label=Label(win,text="Score:{}".format(score),font="consolas 40").pack()

canvas=Canvas(win,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH).pack()

class Snake:

    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x=random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,int(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates=[x,y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake,food):
    x,y=snake.coordinates[0]

    if direction=="up":
        y-=SPACE_SIZE
    elif direction=="down":
        y+=SPACE_SIZE
    elif direction=="left":
        x-=SPACE_SIZE
    elif direction=="right":
        x+=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        win.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
    global direction

    if new_direction=="left":
        if direction!="right":
            direction=new_direction
    elif new_direction=="right":
        if direction!="left":
            direction=new_direction
    elif new_direction=="up":
        if direction!="down":
            direction=new_direction
    elif new_direction=="down":
        if direction!="up":
            direction=new_direction
def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y== body_part[1]:
            return True


    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font="consolas 70",text="GAME OVER",fill="red",tag="gameover")


win.update()
win_width=win.winfo_width()
win_height=win.winfo_height()
screen_width=win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

x=int((screen_width/2)-(win_width/2))
y=int((screen_height/2)-(win_height/2))

win.geometry(f"{win_width}x{win_height}+{x}+{y}")

win.bind("<Left>",lambda event:change_direction("left"))
win.bind("<Right>",lambda event:change_direction("right"))
win.bind("<Up>",lambda event:change_direction("up"))
win.bind("<Down>",lambda event:change_direction("down"))

snake=Snake()

food=Food()
next_turn(snake,food)
win.mainloop()

