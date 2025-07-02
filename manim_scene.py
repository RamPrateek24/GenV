from manim import *

class TwoEllipses(Scene):
    def construct(self):
        ellipse1 = Ellipse(width=2, height=1)
        ellipse2 = Ellipse(width=2, height=1).shift(RIGHT * 4)
        
        self.play(Create(ellipse1), Create(ellipse2))
        self.play(ellipse1.animate.shift(RIGHT * 4), ellipse2.animate.shift(LEFT * 4))
        self.wait()
