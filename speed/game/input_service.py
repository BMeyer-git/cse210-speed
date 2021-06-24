import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _directions (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        
    def get_key(self):
        event = self._screen.get_key()
        if not event is None:
            return event
        return -1

    def get_backspace(self):
        event = self._screen.get_key()
        if not event is None:
            return event == 8
        return False

    def get_submit(self):
        event = self._screen.get_key()
        if not event is None:
            return event == 13
        return False


    def get_esc(self):
        event = self._screen.get_key()
        if not event is None:
            return event == 27
        return False
    
