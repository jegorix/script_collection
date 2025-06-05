import pygame
from start_menu import font_button, draw_button
from config import WIDTH, HEIGHT
import sys

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pause: Collision Simulator")
pause_menu_running = True

def make_button(btn_text, y_pos):
    button = pygame.Rect(WIDTH // 2 - 100, y_pos, 200, 50)
    button_text = font_button.render(btn_text, True, (255, 255, 255))
    return button, button_text

continue_button = make_button('CONTINUE', 100)
restart_button = make_button('RESTART', 200)
exit_button = make_button('EXIT', 300)

def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_button[0].collidepoint(mouse_pos):
                   return 'continue'
                
                elif restart_button[0].collidepoint(mouse_pos):
                    return 'restart'
   
                elif exit_button[0].collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'continue'

                
        screen.fill((30, 30, 30))
        
        draw_button(continue_button[0], continue_button[1])
        draw_button(restart_button[0], restart_button[1])
        draw_button(exit_button[0], exit_button[1])
                
        pygame.display.flip()