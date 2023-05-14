import pygame # a été remplacé par class input 
import sys 
import pygame_gui
pygame.init()

pygame.init()

WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text input in pygame")

WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()

MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
UI_REFRESH_RATE = CLOCK.tick(60) / 100000
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((250, 175), (300, 50)),
    manager=MANAGER,
    object_id='#main_text_entry'
)

def get_input_value():
    input_value = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == "#main_text_entry"):
                input_value = event.text
                return input_value
                
            MANAGER.process_events(event)

        MANAGER.update(UI_REFRESH_RATE)

        WINDOW.fill(WHITE)
        MANAGER.draw_ui(WINDOW)
        pygame.display.update()

def main(): 
    input_value = get_input_value()
    print(f"Input value is: {input_value}")

if __name__ == '__main__':
    main()
