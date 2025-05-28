from validators import get_float, get_positive_float
from visualisation import show_interface



def main():
    print("Two body collision simulator")

    class Body:
        def __init__(self, mass, velocity, position, radius=5, color = (255,0,0)):
            self.mass = mass
            self.velocity = velocity
            self.position = position
            self.radius = (mass * radius) // 2
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
            
            


    print("\nEnter the parametr of the two object to simulate collision")

    # m1 = get_positive_float("Weight of the first object: ")
    # v1 = get_float("Velocity of the first object: ")
    m1 = 10
    v1 = 25
     
    body_1  = Body(mass=m1, velocity=v1 * 10, position=100)

    # m2 = get_positive_float("Weight of the second object: ")
    # v2 = get_float("Velocity of the second object: ")
    m2 = 20
    v2 = 18
    body_2 = Body(mass=m2, velocity=-v2 * 10, color=(0,0,255), position=500)
    
    show_interface(body_1, body_2)


if __name__ == '__main__':
    main()