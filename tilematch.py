from tkinter import *
import random
from tkinter import messagebox
import ALCANTARA_FINALSPROJECT
import pygame

#tile match game
pygame.mixer.init()

def play():
    pygame.mixer.music.load("Music/click.wav")
    pygame.mixer.music.play(loops=0)
    


def stop():
    pygame.mixer.music.stop()
    

def winners():
    pygame.mixer.music.load("Music/win.wav")
    pygame.mixer.music.play(loops=0)

count = 0
answer_list = []
answer_dic = {}



#Reset Game
def reset():
    global matches, winner
    winner = 0
    #create our matches
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    #shuffle matches
    random.shuffle(matches)
    
    #reset label
    my_label.config(text=" ")
    
    #reset tiles
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #loop through buttons and change colors
    for button in button_list:
        button.config(text=" ",bg="SystemButtonFace", state="normal")


def win():
    winners()
    my_label.config(text="Congratulations! You Win!")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #loop through buttons and change colors
    for button in button_list:
        button.config(bg="yellow")

#function for clicking buttons
def button_click(b, number):
    play()
    global count, answer_list, answer_dic, winner

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        #add number to answer list
        answer_list.append(number)
        #add button and number to answer dict
        answer_dic[b] = matches[number]
        #Increment our counter
        count += 1
        
        #start to determine correct or not
        if len(answer_list) == 2:
            if matches[answer_list[0]] == matches[answer_list[1]]:
                my_label.config(text="Match!!")
                for key in answer_dic:
                    key["state"] = "disabled"
                count = 0
                answer_list = []
                answer_dic = {}
                #increment winner counter
                winner += 1
                if winner == 6:
                    win()
            else:
                my_label.config(text="Try Again!",font="Helvetica 15 bold", fg="Red")
                count = 0
                answer_list = []
                #pop up box
                messagebox.showinfo("Incorrect!", "Incorrect!")
                
                #reset the buttons
                for key in answer_dic:
                    key["text"] = " "
                    
                answer_dic = {}

def main_menu():
    root.destroy()
    ALCANTARA_FINALSPROJECT.main()

global winner, matches
winner = 0

#create our matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
#shuffle matches
random.shuffle(matches)


def main():
    global root
    root = Tk()
    root.title("Tile Match")
    root.resizable(width=False,height=False)
    
    app_width = 450
    app_height = 480

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    root.iconbitmap('Images/tile.ico')
    
    my_frame = Frame(root)
    my_frame.pack(pady=10,padx=10)
   
#define buttons
    global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11
    b0 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b0, 0), relief="groove")
    b1 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b1, 1), relief="groove")
    b2 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b2, 2), relief="groove")
    b3 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b3, 3), relief="groove")
    b4 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b4, 4), relief="groove")
    b5 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b5, 5), relief="groove")
    b6 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b6, 6), relief="groove")
    b7 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b7, 7), relief="groove")
    b8 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b8, 8), relief="groove")
    b9 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b9, 9), relief="groove")
    b10 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b10, 10), relief="groove")
    b11 = Button(my_frame, text=' ', font=("Helvetica", 20),height=3, width=6, command=lambda: button_click(b11, 11), relief="groove")
    #b12 = Button(my_frame, text='Exit', font=("Helvetica", 20),height=3, width=6, command=root.quit, relief="groove")


#grid our buttons
    b0.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    b2.grid(row=0, column=2)
    b3.grid(row=0, column=3)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=1, column=3)

    b8.grid(row=2, column=0)
    b9.grid(row=2, column=1)
    b10.grid(row=2, column=2)
    b11.grid(row=2, column=3)

    #b12.grid(row=3, column=1, columnspan=2)
    global my_label
    my_label = Label(root, text="")
    my_label.pack(pady=20)
    
    #create a menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    #create options for dropdown menu

    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Reset Game", command=reset)
    option_menu.add_separator()
    option_menu.add_command(label="Exit Game", command=main_menu)    
    
    root.mainloop()
if __name__ == "__main__":
    main()