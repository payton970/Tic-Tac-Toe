import tkinter 
from tkinter import messagebox
import Player
import Game

class TICTACTOEGUI():
  def __init__(self):
    #make the main window 
    self.mainWindow = tkinter.Tk()
    self.mainWindow.geometry("500x600")
    self.mainWindow.configure(background='white')
    self.mainWindow.title('Tic Tac Toe')
    self.__game = Game.Game()
    self.game_start = False

    #make the frame for the different buttons 
    self.Frame = tkinter.Frame(self.mainWindow)
    self.start_label = tkinter.Label(self.mainWindow, text = "Player 1-Choose Symbol",\
                                     font = ('Courier', 16))
    self.start_label.configure(background='blue')
    self.button_x = tkinter.Button(self.mainWindow, text = 'X', \
                                   command = lambda: self.start_game('X'), font = ('Courier', 16))
    self.button_x.configure(background='yellow')
    
    self.button_o = tkinter.Button(self.mainWindow, text = 'O',
                                   command = lambda: self.start_game('O'), font = ('Courier', 16))
    self.button_o.configure(background='yellow')
    self.button_exit = tkinter.Button(self.mainWindow, text = 'Close',\
                                      command = self.end_game, font =('Courier', 16))
    self.button_exit.configure(background='red')
    self.repeat_button = tkinter.Button(self.mainWindow, text = 'Play Again',\
                                        state = 'disabled',command = self.reset_game, font = ('Courier', 16))
    self.repeat_button.configure(background='red')
    # make a list of numbers which will correspond to an event on one function using lambda
    
    self.grid_list = [0,1,2,3,4,5,6,7,8,9]

    for i in range(1,10):
      self.grid_list[i] = tkinter.Button(self.mainWindow, text = '---',state= 'disabled',\
                                   command=lambda j = i : self.button_click(j),height = 3, width = 7, font=("Courier", 24))
    # Place the buttons and Frame on the window using grid 
    self.Frame.grid()
    self.start_label.grid(row = 0, columnspan = 4)
    self.button_x.grid(row = 1, column = 0)
    self.button_o.grid(row = 1, column = 2)
    self.button_exit.grid(row = 5, column = 0)
    self.repeat_button.grid(row = 5, column = 2)
    #Using game_map to grid the buttons 
    game_map = [[1,4,0], [2,4,1], [3,4,2], [4,3,0], \
                [5,3,1], [6,3,2], [7,2,0], [8,2,1], [9,2,2]]
    for i in game_map:
      self.grid_list[i[0]].grid(row=i[1], column=i[2])
      #game_map[i].configure(background = 'gray')
    tkinter.mainloop()
  #Mutator - changes value of symbol after a button is pressed 
  def decide_player(self):
    if self.symbol == 'X':
      self.symbol = 'O'
    else:
      self.symbol = 'X'
  #Param symbol (str)
  #Mutator sets up the game after the 'X' or 'O' button is clicked  
  def start_game(self,symbol):
    self.game_start = True 
    self.button_x.config(state = 'disabled')
    self.button_o.config(state = 'disabled')
    self.symbol = symbol 
    for i in range(1,10):
      self.grid_list[i].config(state = 'normal')
    if self.symbol == 'X' :
      self.start_label.configure(text = 'Player 1 is X\nPlayer 2 is O')
    else:
      self.start_label.configure(text = 'Player 1 is O\nPlayer 2 is X')
    #keeps a record of which symbol player 1 and 2 are associated with 
    self.__game.associate(self.symbol)
  #param - i (int)
  #shows what happens when the ith button is clicked 
  def button_click(self,i):
    if self.symbol == 'X' :
      myText = 'X'
      self.grid_list[i].config(background = 'purple')
      self.__game.add_tile(self.symbol, i)
      self.decide_player()
    else:
      myText = 'O'
      self.grid_list[i].config(background = 'orange')
      self.__game.add_tile(self.symbol, i)
      self.decide_player()
    self.grid_list[i].config(text = myText, state = 'disabled')
    #checks to see if the game is over
    self.test_game_over()
  #checks to see if the game is over
  #
  def test_game_over(self):
    #print(self.__game.result_game())
    enabled = self.__game.get_both_player_list()
      #self.start_label.config(self.__game.result_game())
    # if the game is over it will display a message box and disable the rest of the buttons 
    if (self.__game.result_game() == self.__game.PLAYER_ONE or self.__game.result_game() == self.__game.PLAYER_TWO or self.__game.result_game()==self.__game.PLAYER_DRAW):     
        for i in range(1,10):
          if i not in enabled:
            self.grid_list[i].config(text="---", state = 'disabled', background = 'gray')
        if self.__game.result_game() == self.__game.PLAYER_ONE:
          tkinter.messagebox.showinfo("GAME OVER", self.__game.PLAYER_ONE)
        elif (self.__game.result_game() == self.__game.PLAYER_TWO):
          tkinter.messagebox.showinfo("GAME OVER", self.__game.PLAYER_TWO)
        else:
          tkinter.messagebox.showinfo("GAME OVER", self.__game.PLAYER_DRAW)
        self.repeat_button.config(state = 'normal')
  #resets the game if the person clicks reset game 
  def reset_game(self):
    self.button_x.config(state = 'normal')
    self.button_o.config(state = 'normal')
    self.start_label.config(text = "Player 1: Choose symbol")
    for i in range(1,10):
      self.grid_list[i].config(text="---", state = 'disabled', background = 'gray')
    self.__game.reset_game()
    self.game_start = False
  #closes the Window if the user clicks close 
  def end_game(self):
    # if the game has started and user clicks close a warning message opens up otherwise, window closes
    if self.game_start:
      end_game = tkinter.messagebox.askyesno("Warning", "You are in the middle of a game!\nAre you sure you want to exit?")
      if end_game:
        self.mainWindow.destroy()
    else:
      self.mainWindow.destroy()
    
TICTACTOEGUI()
