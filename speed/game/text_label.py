from game.actor import Actor
from game.point import Point

"""
    Text_Label 
        Child of Actor
    Purpose:
        A formatted actor output that allows for consistency throughout the program.
        Current format style is "{_text}: {_content}"
    Attributes:
        _content : What is added after the label's _text
    Methods:
        set_content( content : obj )
            Sets the _content attribute.
        get_text()
            Overrides the parent method. Formats this actors text.
"""
class Text_Label(Actor):

    def __init__(self):
        super().__init__()
        _content = ""

    def set_content(self, content):
        self._content = content 
    
    def get_content(self):
        return self._content

    def get_text(self):
        return f"{self._text}: {self._content}"

    