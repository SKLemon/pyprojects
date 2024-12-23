from turtle import Turtle

SCREEN_REFRESH = 0.03
MOVE_DISTANCE = 20


class Snake:
    """Class to represent the Snake in the game.

    This class manages the snake's segments, movement, and appearance in the game.
    The snake consists of multiple connected segments that follow the head segment.
    """

    def __init__(self, starting_snakes=3, shape="square", colour="white"):
        """Initialize a new Snake instance.

        Args:
            starting_snakes (int, optional): Initial number of snake segments. Defaults to 3.
            shape (str, optional): Shape of each snake segment. Defaults to "square".
            colour (str, optional): Color of the snake segments. Defaults to "white".

        Attributes:
            distance_from_head (int): Spacing between snake segments
            count (int): Counter for segment positioning
            segments (list): List of turtle objects forming the snake
        """
        self.distance_from_head = 20
        self.segments = []
        self.starting_snakes = starting_snakes
        self.shape = shape
        self.colour = colour
        self.__create_snake__()
        self.head = self.segments[0]

    def __create_snake__(self):
        """Create the initial snake with multiple segments.

        Creates a snake with the number of segments specified by starting_snakes.
        Each segment is:
        - Given the specified shape and color
        - Positioned horizontally with equal spacing
        - Added to the segments list

        The segments are created from left to right, with the head being the rightmost segment.
        """
        for i in range(self.starting_snakes):
            segment = Turtle(self.shape)
            segment.penup()
            segment.color(self.colour)
            segment.goto(x=-i * self.distance_from_head, y=0)
            self.segments.append(segment)

    def move(self):
        """Control the continuous movement of the snake.

        The snake moves by:
        1. Moving the head segment forward
        2. Having each following segment move to the position of the segment in front of it
        3. Updating the screen at regular intervals (0.05 seconds)

        This creates a smooth, continuous movement where all segments follow the head's path.
        """

        # Move each segment to the position of the segment in front of it
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)  # Moves head forward

    def up(self):
        """Moves the snake upwards without reversing."""
        (self.head.setheading(90) if not self.head.heading() == 270 else None)

    def down(self):
        """Moves the snake downwards without reversing."""
        (self.head.setheading(270) if not self.head.heading() == 90 else None)

    def left(self):
        """Moves the snake leftwards without reversing."""
        (self.head.setheading(180) if not self.head.heading() == 0 else None)

    def right(self):
        """Moves the snake rightwards without reversing."""
        (self.head.setheading(0) if not self.head.heading() == 180 else None)

    def extend(self):
        """Extend the snake by adding a new segment.

        Adds a new segment to the end of the snake, effectively extending the snake by one segment.
        The new segment is positioned at the same location as the last segment of the snake.
        """
        segment = Turtle(self.shape)
        segment.penup()
        segment.color(self.colour)
        segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(segment)
