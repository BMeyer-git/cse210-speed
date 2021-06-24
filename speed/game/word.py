import random

from game import constants
from game.actor import Actor
from game.location import Location

class Word(Actor):
    '''This class keeps track of the score value for each wod, and resets the screen 
    when the word is guessed correctly
    
    _score_value (int): how much each word is worth'''

    def __init__(self):
        super().__init__()
        self.reset()
        self._score_value = 0 
    def reset(self):
        position = Location(random.randint(1,constants.MAX_X), random.randint(1,constants.MAX_Y))
        self.set_position(position)
    def get_score(self, _score_value):
        _score_value = len(self._text)
        return _score_value

