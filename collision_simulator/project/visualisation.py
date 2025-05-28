import pygame
import sys


def draw_velocity_text(screen, font, body, HEIGHT, name, y_offset=30, x = 0, y = 0, padding = 10):
    lines = [
        f'{name} body:',
        f'Weight: {body.mass}kg',
        f'Speed: {body.velocity // 10:.2f}m/s'
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
    pygame.init()
    WIDTH, HEIGHT = (700, 400)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('consolas', 18, bold=True)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # quit()
                
        body1.move(dt)
        body2.move(dt)
        
        body1.bounce_off_walls(WIDTH)
        body2.bounce_off_walls(WIDTH)
        
        if abs(body1.position - body2.position) <= body1.radius + body2.radius:
            body1.collide(body2)
            
        screen.fill((255, 255, 255))
        
        pygame.draw.circle(screen, body1.color, (int(body1.position), HEIGHT // 2), body1.radius) # replace HEIGHT with body1.radius
        pygame.draw.circle(screen, body2.color, (int(body2.position), HEIGHT // 2), body2.radius)
        
        draw_velocity_text(screen, font, body1, HEIGHT, name='Left', x=20, y=20)
        draw_velocity_text(screen, font, body2, HEIGHT, name = 'Right', x=WIDTH-205, y=20)
            
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
