from unittest import mock
import importlib

# Dummy Turtle class
class DummyTurtle:
    def __init__(self):
        pass
    def color(self, *args, **kwargs):
        pass
    def penup(self):
        pass
    def hideturtle(self):
        pass
    def goto(self, *args, **kwargs):
        pass
    def write(self, *args, **kwargs):
        pass
    def seth(self, *args, **kwargs):
        pass
    def ycor(self):
        return -400
    def pendown(self):
        pass
    def forward(self, *args, **kwargs):
        pass
    def clear(self):
        pass

def test_scoreboard_updates_without_error():
    with mock.patch('turtle.Turtle', DummyTurtle):
        sb_module = importlib.import_module('Projects.Pong.scoreboard')
        sb = sb_module.Scoreboard()
        sb.update_left()
        sb.update_right()
