from tkinter import *
import random
from tkinter.font import BOLD
import ALCANTARA_FINALSPROJECT
import pygame

pygame.mixer.init()

def play():
    pygame.mixer.music.load("Music/click.wav")
    pygame.mixer.music.play(loops=0)
    

def stop():
    pygame.mixer.music.stop()


def winner():
    pygame.mixer.music.load("Music/win.wav")
    pygame.mixer.music.play(loops=0)

#tictactoe game

def next_turn(row, column):
    
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                winner()
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
                winner()
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():
    play()
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
    
def main_menu():
    
    window.destroy()
    ALCANTARA_FINALSPROJECT.main()

def main():
    global window
    window = Tk()
    window.title("Tic-Tac-Toe")
    window.resizable(width=False,height=False)
    
    app_width = 465
    app_height = 580

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    window.iconbitmap('Images/tictactoe.ico')
    
    global players
    players = ["x","o"]
    global player
    player = random.choice(players)
    global buttons
    buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    global label
    label = Label(window,text=player + " Turn", font=('consolas',40, BOLD))
    label.grid(column=4, row=0, columnspan= 8)


    frame = Frame(window)
    frame.grid(column=4,row=6)
    
    #create a menu
    my_menu = Menu(window)
    window.config(menu=my_menu)
    #create options for dropdown menu
    
    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Reset Game", command=new_game)
    option_menu.add_separator()
    option_menu.add_command(label="Exit Game", command=main_menu)

    

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,relief="groove"
                                      ,command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)

    window.mainloop()

if __name__ == "__main__":
    main()