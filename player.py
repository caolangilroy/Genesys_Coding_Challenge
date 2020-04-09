class Player:

    def __init__(self, name, player_number):
        self.name = name
        self.number = player_number
        # Initial message for the player to welcome them
        self.message = self._welcome_message()

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def _welcome_message(self):
        return f'Welcome {self.name}! You are player {self.number}'
