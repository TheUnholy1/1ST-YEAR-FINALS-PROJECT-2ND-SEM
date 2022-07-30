from tkinter import *
import random
import ALCANTARA_FINALSPROJECT
from PIL import Image, ImageTk
import pygame


pygame.mixer.init()

def play():
    pygame.mixer.music.load("Music/draw.wav")
    pygame.mixer.music.play(loops=0)

#resize cards
def resize_cards(card):
    #open the image
    our_card_img = Image.open(card)
    
    #resize
    
    our_card_resize_image = our_card_img.resize((150,218))
    
    #output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    
    #return that card
    return our_card_image
    


#shuffle the cards
def shuffle():
    
    #define deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2,15)
    #11 = Jack, 12 = Queen, 13 = King, 14 = Ace
    
    global deck
    deck = []
    
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    
    #create our players
    global dealer, player, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []
    
    #grab a random card for the dealer
    dealer_card = random.choice(deck)
    #remove card from deck
    deck.remove(dealer_card)
    #append card to dealer list
    dealer.append(dealer_card)
    #output card to screen
    
    global dealer_image
    dealer_image = resize_cards(f'Images/Deck/{dealer_card}.png')
    dealer_label.config(image=dealer_image)
    
    
    
    
    #grab a random card for player
    player_card = random.choice(deck)
    #remove card from deck
    deck.remove(player_card)
    #append card to dealer list
    player.append(player_card)
    #output card to screen
    global player_image
    player_image = resize_cards(f'Images/Deck/{player_card}.png')
    player_label.config(image=player_image)
    
    #show number of remaining cards
    root.title(f'Card Game - {len(deck)} Cards Left')
    
    #get the score
    score(dealer_card,player_card)
    play()
    #put number of remaining cards
    #card_count.config(text=len(deck))

def deal_cards():
    try:
        #get the dealer card
        dealer_card = random.choice(deck)
        #remove card from deck
        deck.remove(dealer_card)
        #append card to dealer list
        dealer.append(dealer_card)
        #output card to screen
        
        global dealer_image
        dealer_image = resize_cards(f'Images/Deck/{dealer_card}.png')
        dealer_label.config(image=dealer_image)
        
        #get the player card
        player_card = random.choice(deck)
        #remove card from deck
        deck.remove(player_card)
        #append card to dealer list
        player.append(player_card)
        #output card to screen
        play()
        global player_image
        player_image = resize_cards(f'Images/Deck/{player_card}.png')
        player_label.config(image=player_image)
        
        #show number of remaining cards
        root.title(f'Card Game - {len(deck)} Cards Left')
        #get the score
        score(dealer_card,player_card)
        
    except:
        #tiw
        if dscore.count("j") == pscore.count("j"):
            root.title(f'Card Game - Game Over! Tie! {dscore.count("j")} to {pscore.count("j")}')
            
        #Dealer wins
        elif dscore.count("j") > pscore.count("j"):
            root.title(f'Card Game - Game Over! Dealer Wins! {dscore.count("j")} to {pscore.count("j")}')
        else:
            root.title(f'Card Game - Game Over! Player Wins! {dscore.count("j")} to {pscore.count("j")}')

#return to main menu
def main_menu():
    root.destroy()
    ALCANTARA_FINALSPROJECT.main()
 
def score(dealer_card,player_card):
    #split card numbers
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])
    
    #compare card numbers
    if dealer_card == player_card:
        score_label.config(text="Tie! Play Again!")
        
    elif dealer_card > player_card:
        score_label.config(text="Dealer Wins!")
        dscore.append("j")
    else:
        score_label.config(text="Player Wins!")
        pscore.append("j")
    
    root.title(f'Card Game - {len(deck)} Cards Left |   Dealer:  {dscore.count("j")}      Player: {pscore.count("j")} ')
    
#main code
def main():
    global root
    root = Tk()
    root.title('Card Game')
    root.resizable(width=False,height=False)
    root.configure(background="green")
    
    app_width = 900
    app_height = 650

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    root.iconbitmap('Images/cards.ico')
    
    #root.iconbitmap('tile.ico')
    
    #Create Frames for Cards
    my_frame = Frame(root, bg="green")
    my_frame.pack(pady=20)
    
    dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
    dealer_frame.grid(row=0,column=0,padx=20, ipadx=20)
    
    player_frame = LabelFrame(my_frame, text="Player", bd= 0)
    player_frame.grid(row=0, column=1, ipadx=20)
    
    #card_frame = LabelFrame(my_frame, text="Remaining Cards", bd= 0)
    #card_frame.grid(row=0, column=2, ipadx=20, padx=20)
    
    global dealer_label
    dealer_label = Label(dealer_frame, text='')
    dealer_label.pack(pady=20)
    
    global player_label
    player_label = Label(player_frame, text='')
    player_label.pack(pady=20)
     
    
    #global card_count
    #card_count = Label(card_frame, text='')
    #card_count.pack(pady=20)
    
    #Create Score Label
    global score_label
    score_label = Label(root,text="", font=("Helvetica, 14"), bg="green" )
    score_label.pack(pady=20)
    
    
    #Create a couple buttons
    shuffle_button = Button(root,text="Shuffle Deck",font=("Helvetica  14"), command=shuffle)
    shuffle_button.pack(pady=20)
    
    card_button = Button(root,text="Draw Card",font=("Helvetica  14"), command=deal_cards)
    card_button.pack(pady=20)

    #create a menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    #create option menu
    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    #option_menu.add_command(label="Reset", command=shuffle)
    #option_menu.add_separator()
    option_menu.add_command(label="Exit Game", command=main_menu)

    shuffle()

    root.mainloop()

if __name__ == "__main__":
    main()