from time import sleep
from game import constants
from game.score import Score
from game import buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = buffer()
        self._word = word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        #Declare "direction" as the variable that holds the Director's directions, such as entering a word.
        direction = self._input_service.get_key()
        # ASCII value of 10 means the enter key.
        if direction == 10:
            for word in words:
                if word.text == self._buffer.get_content():
                    self._score.add_points(points)
                    word.reset()
                    

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        snake's case, it meant checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        #Not sure what the difference is between draw_actors and draw_actor, I think this depends on how the words are stored/displayed        self._output_service.draw_actors(self._words)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()