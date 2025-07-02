from manim import *

class DiagonalShapes(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        square.move_to(LEFT * 3 + DOWN * 2)
        circle.move_to(RIGHT * 3 + UP * 2)

        self.add(square, circle)
        self.play(square.animate.move_to(RIGHT * 3 + UP * 2), circle.animate.move_to(LEFT * 3 + DOWN * 2), run_time=3)
        self.wait()
