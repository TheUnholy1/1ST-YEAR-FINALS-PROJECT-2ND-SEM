from tkinter import *
import random
import ALCANTARA_FINALSPROJECT
import pygame

#snake game

pygame.mixer.init()

def game_overs():
    pygame.mixer.music.load("Music/gameover.wav")
    pygame.mixer.music.play(loops=0)

def eat_food():
    pygame.mixer.music.load("Music/eat.wav")
    pygame.mixer.music.play(loops=0)


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
SPACE_SIZE = 50
BODY_PARTS = 2
SNAKE_COLOR = "#8F00FF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
               self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

        def __init__(self):

            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
       
        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))
        
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            eat_food()
            global score

            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        if check_collisions(snake):
            game_over()

        else:
            window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

        global direction

        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction


def check_collisions(snake):

        x, y = snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False


def game_over():
        game_overs()
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

def restart():
    
    window.destroy()
    main()

def main_menu():
    
    window.destroy()
    ALCANTARA_FINALSPROJECT.main()

def main():
    global window
    window = Tk()
    window.title("Snake game")
    window.resizable(False, False)
    
    
    global score
    score = 0
    global direction
    direction = 'down'
    global label
    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()
    global canvas
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=(GAME_HEIGHT- 10), width=(GAME_WIDTH - 10))
    canvas.pack()

    window.update()

    window_width = GAME_WIDTH
    window_height = GAME_HEIGHT
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    
    window.iconbitmap('Images/snakey.ico')
    
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)
    
    #create a menu
    my_menu = Menu(window)
    window.config(menu=my_menu)

    #create options for dropdown menu

    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Reset Game", command=restart)
    option_menu.add_separator()
    option_menu.add_command(label="Exit Game", command=main_menu)
   
    window.mainloop()

if __name__ == "__main__":
    main()

