#Interface de connexion personnel et client 

import pygame 
import os 
from button import ButtonRectangle
from class_input import Input
import pygame_gui
import interface_historique_client as histo
import sys
pygame.init()
pygame.font.init()


input_value = ''

id = 'nico'
passs = 'dioub'

FPS = 60

WIDTH,HEIGHT = 450,450
LONGUEUR, LARGEUR = 1200, 600


FONT = pygame.font.SysFont(None,20)
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("id connexion client ")


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (16,52,166)

LOGIN = Input(WIDTH/2 - 100, 125, 200, 30,WIDTH,HEIGHT,WINDOW)
TEXT_LOGIN = FONT.render('Login : ',1,WHITE)

#CONNEXION = pygame.Rect(WIDTH/2 , 320, 150,30)
TEXT_CONNEXION = FONT.render('SE CONNECTER',1, WHITE )

PASSWORD = Input(WIDTH/2 - 100, 225, 200, 30,WIDTH,HEIGHT,WINDOW)
TEXT_PASSWORD = FONT.render('Password : ',1,WHITE)

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
UI_REFRESH_RATE = CLOCK.tick(60) / 100000

#se_connecter =pygame.draw.rect(WINDOW,BLUE,CONNEXION)

CONNEXION_BUTTON = ButtonRectangle(WIDTH/2,320,150,30,BLUE,'SE CONNECTER',None,WHITE)


def draw_window_2():
    global a ,b
    WINDOW.fill(BLACK)
    
    CONNEXION_BUTTON.draw(WINDOW)

    WINDOW.blit(TEXT_LOGIN,(WIDTH/2 - 100,110))
    WINDOW.blit(TEXT_PASSWORD,(WIDTH/2 - 100,210 ))
    WINDOW.blit(TEXT_CONNEXION,(WIDTH/2 + 15  , 327))

    

    LOGIN.draw_rectangle()

    pygame.display.update()


    user_input = LOGIN.get_input()
    #print("User input:", user_input)
    a = user_input
    
    PASSWORD.draw_rectangle()
    user_input2 = PASSWORD.get_input()
    #print("User input:", user_input2)
    b = user_input2    

    
    pygame.display.update() 
   

   
def main():
    # initialisation des variables
    clock = pygame.time.Clock()
    authenticated = False

    # boucle principale pour l'interface de connexion
    while not authenticated:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_window_2()

        # vérification des identifiants
        if a == id and b == passs:
            authenticated = True

    # appel de la fonction pour l'interface client
    while  authenticated:
        pygame.init()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW = pygame.display.set_mode((LONGUEUR,LARGEUR))
        histo.main()


    pygame.quit()


if __name__ == '__main__':
    main()

