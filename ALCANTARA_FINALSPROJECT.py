#Working Main Menu 
#Jaspher B. Alcantara BSIT 1-1 Finals Project

from tkinter import *
import time
import tictactoe
import tilematch
import snake_game
import card_game
import pygame

pygame.mixer.init()

def clicked():
    pygame.mixer.music.load("Music/click.wav")
    pygame.mixer.music.play(loops=0)



def play():
    pygame.mixer.music.load("Music/Naruto.wav")
    pygame.mixer.music.play(loops=50)
    


def stop():
    pygame.mixer.music.stop()
    
def open_card():
    
    stop()
    clicked()
    root.destroy()
    card_game.main()

def open_tic():
    
    stop()
    clicked()
    root.destroy()
    tictactoe.main()

def open_tile():
    
    stop()
    clicked()
    root.destroy()
    tilematch.main()

def open_snake():
    
    stop()
    clicked()
    root.destroy()
    snake_game.main()

def onenter(b):
    b.widget['background'] = 'white'
    b.widget['foreground'] = 'green' 
    
def onleave(b):
     b.widget['background'] = 'white'
     b.widget['foreground'] = 'black'   
#eto din delete kung ayaw ng command error sa terminal
def clock():
    current_time=time.strftime('%A %B %d %Y %I:%M:%S %p')
    my_label =Label(root, text=current_time, font="Helvetica 12 bold",fg='white',bg='#282828' )
    my_label.grid(row=0, column=0,sticky="N", columnspan=2)
    my_label.after(1000,clock)

def main():
    
    global root
    root = Tk()
    root.title("Game Box")
    root.resizable(width=False,height=False)
    root.configure(bg='#282828')
    root.iconbitmap('Images/games.ico')
    fs = "Arial 8 bold"

    app_width = 300
    app_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    #cinomment ko muna to para sa clock experiment
    #current_time=time.strftime('%A %B %d %Y %I:%M %p')
    #my_label =Label(root, text=current_time, font="Helvetica 12 bold",fg='white',bg='#282828' )
    #my_label.grid(row=0, column=0,sticky="N", columnspan=2)
    

    card = Button(root, text="Card Game",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white", background="white",command=open_card)
    card.grid(row=1, column=0, padx=7)
    card.bind("<Enter>", onenter)
    card.bind("<Leave>", onleave)

    games = Button(root, text="Tic Tac Toe",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white",command=open_tic)
    games.grid(row=1, column=1)
    games.bind("<Enter>", onenter)
    games.bind("<Leave>", onleave)

    snake = Button(root, text="Snake",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white",command=open_snake)
    snake.grid(row=2, column=0)
    snake.bind("<Enter>", onenter)
    snake.bind("<Leave>", onleave)

    tile = Button(root, text="Tile Match",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white",command=open_tile)
    tile.grid(row=2, column=1)
    tile.bind("<Enter>", onenter)
    tile.bind("<Leave>", onleave)

    exit = Button(root, text="Exit",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white", command=root.destroy)
    exit.place(relx=0.5, rely=0.5, anchor='center')
    #exit.grid(row=3, column=1, pady=5)
    exit.bind("<Enter>", onenter)
    exit.bind("<Leave>", onleave)

    play()
    #delete clock() kung ayaw mo ng command error sa terminal hehe
    clock()
    root.mainloop()

if __name__ == "__main__":
    main()
