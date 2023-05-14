import pygame 
pygame.font.init()
import pygame_gui
pygame.init()


class Button_image(): 
    def __init__(self,x,y,image,width,height,scale ):
        self.width = width
        self.height = height
        self.image = pygame.transform.smoothscale(image,(int(width*scale),int(height*scale))) 
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft =  (x,y)

    def draw(self,surface): 

        action = False 
        #get mouse position 

        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions 
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True 
                action = True 
        if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False 

        #draw button on screen 

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action 
    

import pygame

class ButtonRectangle():
    def __init__(self, x, y, width, height, color, text='', font=None, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.clicked = False

    def draw(self, surface):
        # Check mouseover and clicked conditions
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        if pygame.display.get_init() and pygame.display.get_surface():
    # la surface d'affichage est toujours ouverte, vous pouvez modifier la surface Pygame ici
            pygame.draw.rect(surface, self.color, self.rect)

        # Draw button on screen
        
        if self.font:
            font_surface = self.font.render(self.text, True, self.text_color)
            font_rect = font_surface.get_rect(center=self.rect.center)
            surface.blit(font_surface, font_rect)

        return action
