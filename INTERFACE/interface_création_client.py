#sélectionner la destination 

#Interface de connexion personnel et client 

import pygame 
import os 
from button import ButtonRectangle
from class_input import Input
import pygame_gui
pygame.init()
pygame.font.init()

input_value = ''

id = 'nico'
passs = 'dioub'

FPS = 60

WIDTH,HEIGHT = 450,650

FONT = pygame.font.SysFont(None,20)
WINDOW_3 = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("info client ")


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (16,52,166)

NOM = Input(WIDTH/2 - 100, 75, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_NOM = FONT.render('Nom : ',1,BLACK)

PRENOM = Input(WIDTH/2 - 100, 155, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_PRENOM = FONT.render('Prénom : ',1,BLACK)

#CONNEXION = pygame.Rect(WIDTH/2 , 320, 150,30)
TEXT_CONNEXION = FONT.render('Créer utiisateur',1, WHITE )

LOGIN = Input(WIDTH/2 - 100, 250, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_LOGIN = FONT.render('Login : ',1,BLACK)

PASSWORD = Input(WIDTH/2 - 100, 355, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_PASSWORD = FONT.render('Password : ',1,BLACK)

EMAIL = Input(WIDTH/2 - 100, 450, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_EMAIL = FONT.render('Email : ',1,BLACK)

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
UI_REFRESH_RATE = CLOCK.tick(60) / 100000

#se_connecter =pygame.draw.rect(WINDOW,BLUE,CONNEXION)

SE_CONNECTER = ButtonRectangle(WIDTH/2,520,150,30,BLUE,'SE CONNECTER',None,WHITE)


def draw_window_2():
    WINDOW_3.fill(WHITE)
    
    SE_CONNECTER.draw(WINDOW_3)

    WINDOW_3.blit(TEXT_NOM,(WIDTH/2 - 100,55))
    WINDOW_3.blit(TEXT_PRENOM,(WIDTH/2 - 100,135 ))
    WINDOW_3.blit(TEXT_CONNEXION,(WIDTH/2 + 15  , 527))
    WINDOW_3.blit(TEXT_LOGIN,(WIDTH/2 - 100,235))
    WINDOW_3.blit(TEXT_PASSWORD,(WIDTH/2 - 100,335))
    WINDOW_3.blit(TEXT_EMAIL,(WIDTH/2 - 100,435))


    NOM.draw_rectangle()
    NOM_input = NOM.get_input()
    print("Nom :", NOM_input)

    PRENOM.draw_rectangle()
    PRENOM_input = PRENOM.get_input()
    print("Prénom :", PRENOM_input)

    LOGIN.draw_rectangle()
    LOGIN_input = LOGIN.get_input()
    print("Login :", LOGIN_input)

    PASSWORD.draw_rectangle()
    PASSWORD_input = PASSWORD.get_input()
    print("Password :", PASSWORD_input)

    EMAIL.draw_rectangle()
    EMAIL_input = EMAIL.get_input()
    print("Email :", EMAIL_input)

    #if user_input == id and user_input2 == passs:
     #   run = False 
    



    pygame.display.update() 


def main():

    clock = pygame.time.Clock()
    run = True 
    while run : 
        clock.tick(FPS)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : 
                run = False 
                #Action lorsque l'on appuie sur le bouton SE CONNECTER 
            if SE_CONNECTER.draw(WINDOW_3):
                print('Connexion is succesful')

             
        

        draw_window_2()
        #if user_input == id and user_input2 == passs:
                #run = False
    pygame.quit()

if __name__ == '__main__':
    main()

