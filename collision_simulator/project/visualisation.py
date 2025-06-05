import pygame
import sys
from pause_menu import pause
from time import sleep
from config import *

pygame.init()
WIDTH, HEIGHT = (700, 400)
pygame.display.set_caption("Collision Simulator")



screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.image.load("/Users/macbook/PycharmProjects/scripts_edu/collision_simulator/image/space.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

ico_image = pygame.image.load(ICON_PATH).convert_alpha()
pygame.display.set_icon(ico_image)

object_mars_image = pygame.image.load("/Users/macbook/PycharmProjects/scripts_edu/collision_simulator/image/mars.svg").convert_alpha()
object_saturno_image = pygame.image.load("/Users/macbook/PycharmProjects/scripts_edu/collision_simulator/image/saturno.svg").convert_alpha()

button_increase_obj1 = pygame.Rect(30, 130, 60, 30)
button_decrease_obj1 = pygame.Rect(110, 130, 60, 30)
button_increase_obj2 = pygame.Rect(WIDTH-170, 130, 60, 30)
button_decrease_obj2 = pygame.Rect(WIDTH-90, 130, 60, 30)

buttons = {
    'increase_1': (button_increase_obj1, "+10m/s"),
    'decrease_1': (button_decrease_obj1, "-10m/s"),
    'increase_2': (button_increase_obj2, "+10m/s"),
    'decrease_2': (button_decrease_obj2, "-10m/s"),
}


def draw_button_velocity(button_rect, name):
    font = pygame.font.SysFont(FONT_PATH, 25)
    text_surface = font.render(name, True, (0,0,0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    
    
def buttons_operations(body1, body2, mouse_pos):
    for button_name, button_rect in buttons.items():
        if button_rect[0].collidepoint(mouse_pos) and button_name == 'increase_1':
            body1.velocity += 100 if body1.velocity >= 0 else -100
            
        elif button_rect[0].collidepoint(mouse_pos) and button_name == 'decrease_1':
            body1.velocity += -100 if body1.velocity >= 0 else 100
            
        elif button_rect[0].collidepoint(mouse_pos) and button_name == 'increase_2':
            body2.velocity += -100 if body2.velocity <= 0 else 100
            
        elif button_rect[0].collidepoint(mouse_pos) and button_name == 'decrease_2':
            body2.velocity += 100 if body2.velocity <= 0 else -100 
    



def draw(body, screen, path,):
    image = pygame.transform.scale(path, (body.radius * 2, body.radius * 2))
    rect = image.get_rect(center=(int(body.position), HEIGHT // 2 + 100))
    screen.blit(image, rect)


def draw_velocity_text(screen, font, body, name, x = 0, y = 0, padding = 10):
    lines = [
        f'{name} body:',
        f'Weight: {body.mass}kg',
        f'Speed: {body.velocity // 10:.2f}m/s',
        f'Collisions: {body.collisions}'
    ]
    
    # comfortable positioning -> make 2 frames for info block
    rendered_lines = [font.render(line, True, (0,0,0)) for line in lines]
    line_height = font.get_height()
    box_width = max(line.get_width() for line in rendered_lines) + padding * 2
    box_height = len(lines) * line_height + padding * 2 + 5 * (len(lines)-1)
    
    background_rect = pygame.Rect(x, y, box_width, box_height)
    pygame.draw.rect(screen, (200, 200, 200), background_rect, border_radius = 10)
    pygame.draw.rect(screen, (50, 50, 50), background_rect, 2, border_radius = 10)
    
    for i, text in enumerate(rendered_lines):
        text_pos = (x + padding, y + padding + i * (line_height + 5))
        screen.blit(text, text_pos)
       
    # text = font.render(text_info, True, (0, 0, 0))
    
    # text_rect = text.get_rect(center=(x,y))
    
    # # text_rect = text.get_rect(center=(int(body.position), HEIGHT // 2 - y_offset))
    # screen.blit(text, text_rect)
    # # screen.blit(text, (x,y))
    
    

def show_interface(body1, body2):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(FONT_PATH, 25, bold=False)
    paused = False
    running = True
    result = None
    while running:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons_operations(body1, body2, event.pos) 
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                        #fix moment
            if paused:
                result = pause()
                if result == 'restart':
                    return 'restart'
                else:
                    paused = False
                    
                clock.tick(60)
        
                
        if not paused:        
            body1.move(dt)
            body2.move(dt)
            
            body1.bounce_off_walls(WIDTH)
            body2.bounce_off_walls(WIDTH)
            
            distance = abs(body1.position - body2.position)
            min_distance = (body1.radius + body2.radius)
            if distance <= min_distance:
                body1.collide(body2)
            
        # screen.fill(BACKGROUND_COLOR)
        screen.blit(background_image, (0,0))
        
        # pygame.draw.circle(screen, body1.color, (int(body1.position), HEIGHT // 2), body1.radius) # replace HEIGHT with body1.radius
        # pygame.draw.circle(screen, body2.color, (int(body2.position), HEIGHT // 2), body2.radius)
        
        draw(body1, screen, object_mars_image)
        draw(body2, screen, object_saturno_image)
        
        
        
        mouse_pos = pygame.mouse.get_pos()
        for button_rect in buttons.values():
            if button_rect[0].collidepoint(mouse_pos):
                pygame.draw.rect(screen, DARK_GRAY, button_rect[0], border_radius=10)
            else:
                pygame.draw.rect(screen, GRAY, button_rect[0], border_radius=10)
            
            
        for button in buttons.values():   
            draw_button_velocity(button[0], name=button[1])   
        
        
        draw_velocity_text(screen, font, body1, name='Left', x=20, y=20)
        draw_velocity_text(screen, font, body2, name = 'Right', x=WIDTH-180, y=20)
            
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
