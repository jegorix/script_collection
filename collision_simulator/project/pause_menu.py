import pygame
from start_menu import font_button, draw_button
from config import WIDTH, HEIGHT

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
    global pause_menu_running
    
    while pause_menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause_menu_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_button[0].collidepoint(mouse_pos):
                    pause_menu_running = False
                
                if restart_button[0].collidepoint(mouse_pos):
                    pause_menu_running = False
                    
                    
                if exit_button[0].collidepoint(mouse_pos):
                    pause_menu_running = False
                    pygame.quit
                    
            elif event.type == pygame.K_SPACE:
                pause_menu_running = False
                return False
                
        screen.fill((30, 30, 30))
        
        draw_button(continue_button[0], continue_button[1])
        draw_button(restart_button[0], restart_button[1])
        draw_button(exit_button[0], exit_button[1])
                
        pygame.display.flip()