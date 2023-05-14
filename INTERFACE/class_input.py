import pygame 
import pygame_gui
import sys 
pygame.freetype.init()
pygame.init()

WIDTH,HEIGHT = 1200,600
class Input:
    def __init__(self, x, y, width, height,WIDTH,HEIGHT,WINDOW):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_entry = None
        self.CLOCK = pygame.time.Clock()
        self.WINDOW = WINDOW
        self.WHITE = (255,255,255) 

        self.MANAGER  = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.UI_REFRESH_RATE = self.CLOCK.tick(60) / 100000



    def draw_rectangle(self):
        self.text_entry = pygame_gui.elements.UITextEntryLine(
            self.rect, manager= self.MANAGER, object_id="#main_text_entry")

    def get_input(self):
        input_value = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry"):
                    input_value = event.text
                    return input_value

                self.MANAGER.process_events(event)

            self.MANAGER.update(self.UI_REFRESH_RATE)

            self.MANAGER.draw_ui(self.WINDOW)
            pygame.display.update()


#Test1 = Input(200, 100,400, 50,100,200,WINDOW =  pygame.display.set_mode((WIDTH,HEIGHT)))
#Test1.draw_rectangle()
#user_input = Test1.get_input()
#print("User input:", user_input)


