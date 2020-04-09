import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def test_player_create(self):
        player = Player('test', 1)
        self.assertEqual(player.name, 'test')
        self.assertEqual(player.number, 1)
        self.assertEqual(player.number, 1)
        welcomeMessage = 'Welcome test! You are player 1'
        self.assertEqual(player.message, welcomeMessage)

    def test_player_change_token(self):
        player = Player('test', 1)
        player.set_color('X')
        self.assertEqual(player.get_color(), 'X')
