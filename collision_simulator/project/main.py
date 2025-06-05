from validators import get_float, get_positive_float
from visualisation import show_interface
from start_menu import simulator_menu
import sys
import os


BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
image_dir = os.path.join(BASE_DIR, "image")
image_files = ['ico.svg', 'mars.svg', 'saturno.svg', 'space.jpg']
image_paths = [os.path.join(image_dir, img) for img in image_files]
font_path = os.path.join(BASE_DIR, "fonts", "FiraCode-Regular.ttf")


# pyinstaller --onefile --noconsole --add-data "fonts:fonts" --add-data "image:image" project/main.py


def main():
    print("Two body collision simulator")

    class Body:
        def __init__(self, mass, velocity, position, color = (255,0,0), k=1):
            self.mass = mass
            self.velocity = velocity
            self.position = position
            self.radius = int(10 + mass * 2) * k
            self.color = color
            self.collisions = 0
            
        def move(self, dt):
            self.position += self.velocity * dt
        
        def bounce_off_walls(self, screen_width):
            if self.position - self.radius <= 0 or self.position + self.radius >= screen_width:
                self.velocity *= -1
                self.collisions += 1
        
        def collide(self, other):
            m1, v1 = self.mass, self.velocity
            m2, v2 = other.mass, other.velocity
            
            v1_new = ((m1 - m2) * v1 + 2*m2*v2) / (m1 + m2)
            v2_new = ((m2 - m1) * v2 + 2*m1*v1) / (m1 + m2)
            
            self.velocity = v1_new
            self.collisions += 1
            
            other.velocity = v2_new
            other.collisions += 1
    
    
    
    running = True
    
    while running:
        values = simulator_menu()
        if values:
            m1, v1, m2, v2 = values
        else:
            m1, v1, m2, v2 = [10, 25, 15, 18]
        
        body_1  = Body(mass=m1, velocity=v1 * 10, position=100)
        body_2 = Body(mass=m2, velocity=-v2 * 10, position=500, k = 1.75)
        
        reset = show_interface(body_1, body_2)
        if reset == 'restart':
            continue
        


if __name__ == '__main__':
    main()