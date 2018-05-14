#displays all game text
import pygame
import HangmanGame
import time
import tkinter as tk
import secretWords
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
letterSelection = False;
secretWord = secretWords.get_secret_word()
drawStep = 0


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.intro_message_display()
        self.secret_word_display()
        self.get_letters(master)
        self.create_choose_letter()
        self.create_letters_chosen()
        self.image_one_display()

    def intro_message_display(self):
        self.intro = tk.Label(text="Welcome to Hangman! The goal is to complete the word within 5 guesses.", font=("Helvetica", 12))
        self.intro.place(x = 720/6, y = 480/100);


    def secret_word_display(self):
        import convertToAsterisk
        global secretWord
        self.displaySecretWord = tk.Label(text="Your word is: " + convertToAsterisk.replace_with_asterisks(secretWord), font=("Helvetica", 16))
        self.displaySecretWord.place(x = 720/4, y = 480/8);

    def create_choose_letter(self):
        self.letter_selection = tk.Label(text="Please choose a letter:", font=("Helvetica", 16))
        self.letter_selection.place(x = 720/3, y = 480/2);

    def create_letters_chosen(self):
        import letterCorrect
        self.letters_chosen = tk.Label(text="You have guessed: \n" + str(letterCorrect.guessedLetters), font=("Helvetica", 12))
        self.letters_chosen.place(x = 720/1.4, y = 480/9);

    def image_one_display(self):
        self.HangmanImageOne = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck Torso.png")
        self.HangmanImageOneLabel = tk.Label(image = self.HangmanImageOne)
        self.HangmanImageOneLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def image_two_display(self):
        self.HangmanImageTwo = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck with head.png")
        self.HangmanImageTwoLabel = tk.Label(image = self.HangmanImageTwo)
        self.HangmanImageTwoLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def image_three_display(self):
        self.HangmanImageThree = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck missing one arm.png")
        self.HangmanImageThreeLabel = tk.Label(image = self.HangmanImageThree)
        self.HangmanImageThreeLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def image_four_display(self):
        self.HangmanImageFour = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck missing two timbs.png")
        self.HangmanImageFourLabel = tk.Label(image = self.HangmanImageFour)
        self.HangmanImageFourLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def image_five_display(self):
        self.HangmanImageFive = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck missing one Timb.png")
        self.HangmanImageFiveLabel = tk.Label(image = self.HangmanImageFive)
        self.HangmanImageFiveLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def image_six_display(self):
        self.HangmanImageSix = tk.PhotoImage(file = "C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/Hangman/Zuck Complete.png")
        self.HangmanImageSixLabel = tk.Label(image = self.HangmanImageSix)
        self.HangmanImageSixLabel.place(x = 720/2.5, y = 480/5, width=180, height=120);

    def get_letters(self,master):
        import letterCorrect
        #First row
        self.A_button = tk.Button(master, text="A", fg="black",command =lambda: self.check_guess("A"))
        self.A_button.place(x = 150, y = 280)

        self.B_button = tk.Button(master, text="B", fg="black",command =lambda: self.check_guess("B"))
        self.B_button.place(x = 185, y = 280)

        self.C_button = tk.Button(master, text="C", fg="black",command =lambda: self.check_guess("C"))
        self.C_button.place(x = 220, y = 280)

        self.D_button = tk.Button(master, text="D", fg="black",command =lambda: self.check_guess("D"))
        self.D_button.place(x = 255, y = 280)

        self.E_button = tk.Button(master, text="E", fg="black",command =lambda: self.check_guess("E"))
        self.E_button.place(x = 290, y = 280)

        self.F_button = tk.Button(master, text="F", fg="black",command =lambda: self.check_guess("F"))
        self.F_button.place(x = 325, y = 280)

        self.G_button = tk.Button(master, text="G", fg="black",command =lambda: self.check_guess("G"))
        self.G_button.place(x = 360, y = 280)

        self.H_button = tk.Button(master, text="H", fg="black",command =lambda: self.check_guess("H"))
        self.H_button.place(x = 395, y = 280)

        self.I_button = tk.Button(master, text="I", fg="black",command =lambda: self.check_guess("I"))
        self.I_button.place(x = 430, y = 280)

        self.J_button = tk.Button(master, text="J", fg="black",command =lambda: self.check_guess("J"))
        self.J_button.place(x = 465, y = 280)

        self.K_button = tk.Button(master, text="K", fg="black",command =lambda: self.check_guess("K"))
        self.K_button.place(x = 500, y = 280)

        #Second row

        self.L_button = tk.Button(master, text="L", fg="black",command =lambda: self.check_guess("L"))
        self.L_button.place(x = 170, y = 320)

        self.M_button = tk.Button(master, text="M", fg="black",command =lambda: self.check_guess("M"))
        self.M_button.place(x = 205, y = 320)

        self.N_button = tk.Button(master, text="N", fg="black",command =lambda: self.check_guess("N"))
        self.N_button.place(x = 240, y = 320)

        self.O_button = tk.Button(master, text="O", fg="black",command =lambda: self.check_guess("O"))
        self.O_button.place(x = 275, y = 320)

        self.P_button = tk.Button(master, text="P", fg="black",command =lambda: self.check_guess("P"))
        self.P_button.place(x = 310, y = 320)

        self.Q_button = tk.Button(master, text="Q", fg="black",command =lambda: self.check_guess("Q"))
        self.Q_button.place(x = 345, y = 320)

        self.R_button = tk.Button(master, text="R", fg="black",command =lambda: self.check_guess("R"))
        self.R_button.place(x = 380, y = 320)

        self.S_button = tk.Button(master, text="S", fg="black",command =lambda: self.check_guess("S"))
        self.S_button.place(x = 415, y = 320)

        self.T_button = tk.Button(master, text="T", fg="black",command =lambda: self.check_guess("T"))
        self.T_button.place(x = 450, y = 320)

        self.U_button = tk.Button(master, text="U", fg="black",command =lambda: self.check_guess("U"))
        self.U_button.place(x = 485, y = 320)

        #Third row

        self.V_button = tk.Button(master, text="V", fg="black",command =lambda: self.check_guess("V"))
        self.V_button.place(x = 260, y = 360)

        self.W_button = tk.Button(master, text="W", fg="black",command =lambda: self.check_guess("W"))
        self.W_button.place(x = 295, y = 360)

        self.X_button = tk.Button(master, text="X", fg="black",command =lambda: self.check_guess("X"))
        self.X_button.place(x = 330, y = 360)

        self.Y_button = tk.Button(master, text="Y", fg="black",command =lambda: self.check_guess("Y"))
        self.Y_button.place(x = 365, y = 360)

        self.Z_button = tk.Button(master, text="Z", fg="black",command =lambda: self.check_guess("Z"))
        self.Z_button.place(x = 400, y = 360)


    def check_guess(self,s):
        import letterCorrect
        global drawStep
        global drawStep
        str = letterCorrect.is_letter_correct(s)
        if str == "correct":
            self.secret_word_display()
            self.create_letters_chosen()
        elif str == "incorrect":
            self.letter_selection.after(1000, self.clear_letter_selection)    # 1000ms
            self.create_letter_incorrect()
            time.sleep(2)
            self.letter_incorrect.after(1000, self.clear_letter_incorrect)    # 1000ms
            self.create_choose_letter()
            self.create_letters_chosen()
            drawStep += 1
        elif str == "chosen":
            self.letter_selection.after(1000, self.clear_letter_selection)    # 1000ms
            self.create_letter_already_chosen()
            time.sleep(2)
            self.letter_already_chosen.after(1000, self.clear_letter_already_chosen)    # 1000ms
            self.create_choose_letter()
            self.create_letters_chosen()

        self.check_game_over()

    def clear_letter_selection(self):
        self.letter_selection.place_forget()

    def clear_letter_already_chosen(self):
        self.letter_already_chosen.place_forget()

    def clear_letter_incorrect(self):
        self.letter_incorrect.place_forget()

    def clear_all_buttons(self):
        self.A_button.place_forget()
        self.B_button.place_forget()
        self.C_button.place_forget()
        self.D_button.place_forget()
        self.E_button.place_forget()
        self.F_button.place_forget()
        self.G_button.place_forget()
        self.H_button.place_forget()
        self.I_button.place_forget()
        self.J_button.place_forget()
        self.K_button.place_forget()
        self.L_button.place_forget()
        self.M_button.place_forget()
        self.N_button.place_forget()
        self.O_button.place_forget()
        self.P_button.place_forget()
        self.Q_button.place_forget()
        self.R_button.place_forget()
        self.S_button.place_forget()
        self.T_button.place_forget()
        self.U_button.place_forget()
        self.V_button.place_forget()
        self.W_button.place_forget()
        self.X_button.place_forget()
        self.Y_button.place_forget()
        self.Z_button.place_forget()
        self.intro.place_forget()
        self.letter_selection.place_forget()


    def create_letter_already_chosen(self):
        self.letter_already_chosen = tk.Label(text="You have already chosen that letter", fg="red", font=("Helvetica", 16))
        self.letter_already_chosen.place(x = 720/3, y = 480/2);

    def create_letter_incorrect(self):
        self.letter_incorrect = tk.Label(text="That letter is not in the word!", fg="red",font=("Helvetica", 16))
        self.letter_incorrect.place(x = 720/3, y = 480/2);



    def game_over(self):
        self.clear_all_buttons()
        self.game_over_text = tk.Label(text="Game Over", fg="red", font=("Helvetica", 25))
        self.game_over_text.place(x = 310, y = 320)

    def player_won(self):
        self.clear_all_buttons()
        self.image_six_display()
        self.win_text = tk.Label(text="You Win!!!", fg="green", font=("Helvetica", 25))
        self.win_text.place(x = 310, y = 320)

    def check_game_over(self):
        import convertToAsterisk
        global secretWord
        global drawStep
        if drawStep == 5:
            self.image_six_display()
            self.game_over()

        elif secretWord == convertToAsterisk.replace_with_asterisks(secretWord):
            self.player_won()

        elif drawStep == 1:
            self.image_two_display()

        elif drawStep == 2:
            self.image_three_display()

        elif drawStep == 3:
            self.image_four_display()

        elif drawStep == 4:
            self.image_five_display()

        else:
            pass

root = tk.Tk()
root.geometry("720x480")
app = Application(master=root)
app.master.title('Hangman')
app.mainloop()


















'''
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def intro_message_display(text):
    import HangmanGame
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((HangmanGame.width/2),(HangmanGame.height/2.5))
    HangmanGame.screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(4)

    HangmanGame.screen.fill(white)

    pygame.display.update()

def secretWord_display(text):
    import HangmanGame
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((HangmanGame.width/2),(HangmanGame.height/9))
    HangmanGame.screen.blit(TextSurf, TextRect)

    pygame.display.update()

def enter_guess_display():
    import HangmanGame
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects("Please enter a letter:", largeText)
    TextRect.center = ((HangmanGame.width/2),(HangmanGame.height/1.8))
    HangmanGame.screen.blit(TextSurf, TextRect)

    pygame.display.update()


def guesses_display():
    import HangmanGame
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects("Your guesses are: ", largeText)
    TextRect.center = ((HangmanGame.width/2),(HangmanGame.height/9))
    HangmanGame.screen.blit(TextSurf, TextRect)

    pygame.display.update()

def letters_display():
    import HangmanGame
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(letterCorrect.guessedLetters, largeText)
    TextRect.center = ((HangmanGame.width/2),(HangmanGame.height/9))
    HangmanGame.screen.blit(TextSurf, TextRect)

    pygame.display.update()


def buttons_display():
    A_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(150,280,30,30));
    B_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(185,280,30,30));
    C_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(220,280,30,30));
    D_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(255,280,30,30));
    E_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(290,280,30,30));
    F_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(325,280,30,30));
    G_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(360,280,30,30));
    H_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(395,280,30,30));
    I_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(430,280,30,30));
    J_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(465,280,30,30));
    K_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(500,280,30,30));
    #Start of second row
    L_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(170,320,30,30));
    M_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(205,320,30,30));
    N_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(240,320,30,30));
    O_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(275,320,30,30));
    P_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(310,320,30,30));
    Q_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(345,320,30,30));
    R_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(380,320,30,30));
    S_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(415,320,30,30));
    T_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(450,320,30,30));
    U_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(485,320,30,30));
    #Start of third row
    V_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(260,360,30,30));
    W_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(295,360,30,30));
    X_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(330,360,30,30));
    Y_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(365,360,30,30));
    Z_button = pygame.draw.rect(HangmanGame.screen,(0,0,240),(400,360,30,30));
    pygame.display.update()
'''

'''
def select_button():
    global letterSelection
    while letterSelection == False:
        for letterSelection in pygame.event.get():
            print(letterSelection);
            if letterSelection.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 280:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        pygame.quit();
'''
