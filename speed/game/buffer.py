from typing import Text
from game.point import Point
from game.text_label import Text_Label


"""
    Buffer
        Handles storage of the player's input buffer and is able to display it in a formatted output.
    
    Methods:
        add_to_buffer(character : char)
            Adds the given character to this _content.
        reset()
            Resets this buffer's _content to be empty.
"""
class Buffer(Text_Label):

    def __init__(self):
        super().__init__()
        self.set_text("Buffer")
        self.clear_buffer()
        self.set_position(Point(1,19))

    def add_to_buffer(self, character):
        self._content += character

    def reset(self):
        self.set_content("")
    