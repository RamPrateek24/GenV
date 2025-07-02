from manim import *

class TwoEllipses(Scene):
    def construct(self):
        ellipse1 = Ellipse(width=2, height=1, color=BLUE).shift(LEFT * 3)
        ellipse2 = Ellipse(width=2, height=1, color=RED).shift(RIGHT * 3)
        self.add(ellipse1, ellipse2)
        self.play(ellipse1.animate.shift(RIGHT * 3), ellipse2.animate.shift(LEFT * 3), run_time=2)
        self.wait()
