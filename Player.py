class Player:
    # Make instance
    def __init__(self):
        self.__value = None
        self.__playerlist = []

    # Adding new tile
    def add_tile(self, tile):
        self.__playerlist.append(tile)

    # Make user_input same to self.__value
    def set_value(self, some_value):
        self.__value = some_value

    # Accessor
    def get_playerlist(self):
        return self.__playerlist

    # Accessor
    def get_value(self):
        return self.__value

    # Reset the game
    def reset(self):
        self.__playerlist = []
        self.__value = None
