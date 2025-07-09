from manim import *

class PlanetsRevolving(Scene):
    def construct(self):
        sun = Circle(color=YELLOW, fill_opacity=1).scale(0.5)
        self.add(sun)
        
        planets = []
        colors = [BLUE, RED, GREEN, ORANGE, PURPLE]
        distances = [1.5, 2, 2.5, 3, 3.5]
        
        for i in range(5):
            planet = Circle(color=colors[i], fill_opacity=1).scale(0.1)
            planet_path = Circle(radius=distances[i])
            self.add(planet)
            planets.append((planet, planet_path))
        
        for planet, path in planets:
            self.play(ShowCreation(path), RunTime=4)
            self.play(ApplyMethod(planet.move_to, path.get_start()))
            self.play(ApplyMethod(planet.move_to, path.get_end(), run_time=4), rate_func=linear)
            self.play(FadeOut(path))
        
        self.wait()
