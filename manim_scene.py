from manim import *

class CombineCircles(Scene):
    def construct(self):
        circle1 = Circle(radius=1, color=BLUE).shift(LEFT)
        circle2 = Circle(radius=1, color=RED).shift(RIGHT)

        self.play(Create(circle1), Create(circle2))
        self.play(circle1.animate.shift(RIGHT), circle2.animate.shift(LEFT))
        self.wait(1)

        combined_circle = Circle(radius=1.5, color=PURPLE)
        self.play(Transform(circle1, combined_circle), Transform(circle2, combined_circle))
        self.wait(2)
