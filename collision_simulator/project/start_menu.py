import pygame
from visualisation import WIDTH, HEIGHT, FONT_PATH
from validators import is_float
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

object_values = []

action_font = pygame.font.SysFont(FONT_PATH, 36)

actions_text = [
    'Enter weight of the first object:',
    'Enter velocity of the first object:',
    'Enter weight of the second object:',
    'Enter velocity of the second object:', 
    'Object data successfully readed!' 
]
entered = 0



cursor_visible = True
cursor_timer = 0
clock = pygame.time.Clock()

def draw_action_text(count):
    for index, text in enumerate(actions_text):
        if index == count:
            text_surface = action_font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (WIDTH // 2 - 180, 30))
        elif count >= len(actions_text):
            text_surface = action_font.render(actions_text[-1], True, (255, 255, 255))
            screen.blit(text_surface, (WIDTH // 2 - 180, 30))
        
            


def handle_numbers(number):
    print(number * 10)
    
    
def draw_cursor(active, visible, box, text_box):
    if active and visible:
        cursor_x = box.x + 30 + text_box.get_width() + 2
        cursor_y = box.y + 10
        cursor_height = font_input_box.get_height()
        pygame.draw.line(screen, (255, 255, 255), (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)


def draw_button(button, button_text):
    pygame.draw.rect(screen, (70, 130, 180), button, border_radius=15)
    button_rect = button_text.get_rect(center=button.center)
    screen.blit(button_text, button_rect)
    
    
def draw_input_form(text):
    text_input_box = font_input_box.render(text, True, (255, 255, 255))
    screen.blit(text_input_box, (input_box.x + 30, input_box.y + 10))
    input_box.w = max(200, text_input_box.get_width() + 60)
    return text_input_box
    
    


def simulator_menu():
    global menu_running, color, text, active, entered, object_values
    
    while menu_running:  
        global cursor_timer, cursor_visible
        dt = clock.tick(30)
        cursor_timer += dt
        if cursor_timer >= 500:
            cursor_visible = not cursor_visible
            cursor_timer = 0
        
        
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
                        if is_float(text):
                            entered += 1
                            object_values.append(float(text))
                            text = ''
                        else:
                            print("Error! Please type number")
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if event.unicode.isdigit() or event.unicode == '.':
                            text += event.unicode                                     
                            
        screen.fill((30, 30, 30))
        draw_action_text(entered)
        
        if entered < 4:
            pygame.draw.rect(screen, color, input_box, border_radius=15)
            text_input_box = draw_input_form(text)
            draw_cursor(active, cursor_visible, input_box, text_input_box)
        else:
            text_surface = action_font.render("You're ready to start!", True, (255, 255, 255))
            screen.blit(text_surface, (input_box.x - 20, input_box.y))
        

        draw_button(start_button_rect, start_text)
        draw_button(exit_button_rect, exit_text)
    

        pygame.display.flip()
        
    return object_values
    