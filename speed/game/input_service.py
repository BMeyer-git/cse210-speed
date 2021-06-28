import threading
from asciimatics.event import KeyboardEvent

def _thread_runtime(input):
    
    while not input._esc:
        try:
            input._screen.print_at("thread input: " + str(input._key_buffer), 0, 3, 7)
            event = input._screen.get_key()
            if not event is None:
                
                if event == 8:
                    pass # Backspace logic
                elif event == 13:
                    pass # Enter logic
                elif event == 27:
                    # Escape logic
                    input._esc = True
                else:
                    input._key_buffer += chr(event)
        except Exception as e:
            input._screen.print_at("input thread exception!", 0, 3, 7)
    
    input._screen.print_at("thread ending", 0, 4, 7)

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
        self._key_buffer = ""
        self._backspace_buffer = 0
        self._esc = False
        self._screen = screen
        self._thread = threading.Thread(target=_thread_runtime, args=(self, ))
        self._thread.start()
        self._lock = threading.Lock()
        
    def get_keys(self):
        keys = str(self._key_buffer)
        self._key_buffer = ""
        return keys

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
        esc = self._esc
        self._esc = False
        return esc
    
if __name__ == "__main__":
    from asciimatics.screen import Screen 
    from time import sleep
    import sys
    
    def main(screen):
        input = InputService(screen)
        buffer = ""
        while True:
            buffer += input.get_keys()
            screen.print_at("input: " + buffer, 0, 0, 7)
            screen.print_at("esc: " + str(input.get_esc()), 0, 1, 7)
            screen.refresh()
            screen.clear_buffer(7, 0, 0)
            if input.get_esc():
                raise;
            sleep(1)
    Screen.wrapper(main)

    