import Player

class Game:
    WINMETHOD =  [[1,2,3], [4,5,6], [7,8,9], \
                     [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    PLAYER_ONE = "Player 1 Won!"
    PLAYER_TWO = "Player 2 Won!"
    PLAYER_DRAW = "Draw!"
    GAME_IN_PLAY = "KEEP PLAYING!"
    
# Constructor --------------------------------------------------------------
    # Make instance
    def __init__(self):
        self.__player1 = Player.Player()
        self.__player2 = Player.Player()

    #
    def is_condition(self,conditions, tile_list):
        return_variable = True
        for number in conditions:
            if number not in tile_list:
                return_variable = False
        return return_variable

    def result_game(self):
        player1_list = int(len(self.__player1.get_playerlist()))
        player2_list = int(len(self.__player2.get_playerlist()))
        ret = "" 
        print(self.__player1.get_playerlist())
        print(self.__player2.get_playerlist())
        for condition in Game.WINMETHOD:
            if self.is_condition(condition, self.__player1.get_playerlist()):
                ret = Game.PLAYER_ONE
        for condition in Game.WINMETHOD:
            if self.is_condition(condition, self.__player2.get_playerlist()):
                ret =  Game.PLAYER_TWO
        if (ret != Game.PLAYER_ONE and ret != Game.PLAYER_TWO) and (player1_list + player2_list < 9):
            ret = Game.GAME_IN_PLAY
        elif (player1_list + player2_list == 9):
            ret = Game.PLAYER_DRAW            
        return ret

    # Adding tile to player who is playing
    def add_tile(self, which_player, tile):
        if which_player == self.__player1.get_value():   
            self.__player1.add_tile(tile)
        else:
            self.__player2.add_tile(tile)

    # If player 1 click X than player 2 will be O
    def associate(self, player):
        if player == 'X':
            self.__player1.set_value('X')
            self.__player2.set_value('O')
        else:
            self.__player1.set_value('O')
            self.__player2.set_value('X')

    # It show the enable 
    def get_both_player_list(self):
        enabled = self.__player1.get_playerlist() + self.__player2.get_playerlist()
        return enabled

    # Reset the game
    def reset_game(self):
        self.__player1.reset()
        self.__player2.reset()
                
            
    
