from manim import *

class RevolvingSquares(Scene):
    def construct(self):
        square1 = Square(color=BLUE).shift(LEFT)
        square2 = Square(color=RED).shift(RIGHT)
        self.add(square1, square2)
        self.play(Rotate(square1, angle=TAU, run_time=2, rate_func=linear), 
                  Rotate(square2, angle=-TAU, run_time=2, rate_func=linear))
        self.wait()
