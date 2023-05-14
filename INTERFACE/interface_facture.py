#sélectionner la destination 

#Interface de connexion personnel et client 

import pygame 
import os 
from mysql.connector import connect
from button import ButtonRectangle
from class_input import Input
import pygame_gui
pygame.font.init()
pygame.init()

#Connected sur Mysql
bdd=connect(host="localhost",user="root",password="root",database="agence")

#definir les fonctions de saisir client
def f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password):
    cursor=bdd.cursor()
    sql="INSERT INTO clients(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.execute(sql,(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password))
    bdd.commit()

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

TEXT_FACTURE = FONT.render('Facture : ',1,BLACK)

TEXT_PRENOM = FONT.render('PRENOM : ',1,BLACK)

#CONNEXION = pygame.Rect(WIDTH/2 , 320, 150,30)
TEXT_CONNEXION = FONT.render('SE CONNECTER',1, WHITE )


TEXT_DD = FONT.render('Date départ : ',1,BLACK)

TEXT_PASSWORD = FONT.render('MOT DE PASSE : ',1,BLACK)

TEXT_DR = FONT.render('Date retour : ',1,BLACK)

TEXT_BUDGET = FONT.render('Budget : ',1,BLACK)

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
UI_REFRESH_RATE = CLOCK.tick(60) / 100000

#se_connecter =pygame.draw.rect(WINDOW,BLUE,CONNEXION)

SE_CONNECTER = ButtonRectangle(WIDTH/2,600,150,30,BLUE,'SE CONNECTER',None,WHITE)


def draw_window_2():
    if pygame.display.get_init() and pygame.display.get_surface():
    # la surface d'affichage est toujours ouverte, vous pouvez modifier la surface pygame ici
    

        WINDOW_3.fill(WHITE)
    
    SE_CONNECTER.draw(WINDOW_3)

    WINDOW_3.blit(TEXT_FACTURE,(10,25))
    WINDOW_3.blit(TEXT_PRENOM,(15,135 ))
    WINDOW_3.blit(TEXT_CONNEXION,(250  , 607))
    WINDOW_3.blit(TEXT_DD,(15,235))
    WINDOW_3.blit(TEXT_DR,(15,335))
    WINDOW_3.blit(TEXT_BUDGET,(15,435))
    WINDOW_3.blit(TEXT_PASSWORD,(15,535))

    

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
        
    pygame.quit()

if __name__ == '__main__':
    main()

