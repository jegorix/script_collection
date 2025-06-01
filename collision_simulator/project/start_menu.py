import pygame
from visualisation import WIDTH, HEIGHT, FONT_PATH
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulator menu")
menu_running = True

font_button = pygame.font.SysFont(FONT_PATH, 40)
start_button_rect = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
exit_button_rect = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
start_text = font_button.render("START", True, (255, 255, 255))
exit_text = font_button.render("EXIT", True, (255, 255, 255))

font_input_box = pygame.font.SysFont(FONT_PATH, 32)
input_box = pygame.Rect(WIDTH // 2 - 100, 100, 200, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''


def handle_numbers(number):
    print(number * 10)


def draw_button(button, button_text):
    pygame.draw.rect(screen, (70, 130, 180), button, border_radius=15)
    button_rect = button_text.get_rect(center=button.center)
    screen.blit(button_text, button_rect)
     
    


def simulator_menu():
    global menu_running, color, text, active
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    running = True
                    menu_running = False
                    
                if exit_button_rect.collidepoint(mouse_pos):
                    menu_running = False
                    running = False
                    
                if input_box.collidepoint(mouse_pos):
                    active = not active
                else:
                    active = False
                    
                color = color_active if active else color_inactive
             
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.isdigit():
                            handle_numbers(float(text))
                            text = ''
                        else:
                            print("Error! Please type number")
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if event.unicode.isdigit():
                            text += event.unicode                                     
                            
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, border_radius=15)
        text_input_box = font_input_box.render(text, True, (255, 255, 255))
        screen.blit(text_input_box, (input_box.x + 30, input_box.y + 10))
        input_box.w = max(200, text_input_box.get_width() + 60)
        
        
        draw_button(start_button_rect, start_text)
        draw_button(exit_button_rect, exit_text)
    

        pygame.display.flip()
        
    return running
    