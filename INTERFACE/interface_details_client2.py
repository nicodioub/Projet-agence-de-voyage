#sélectionner la destination 

#Interface de connexion personnel et client 
from mysql.connector import connect
import pygame 
import os 
from button import ButtonRectangle
from class_input import Input
import pygame_gui
pygame.init()

pygame.font.init()

#Connected sur Mysql
bdd=connect(host="localhost",user="root",
            password="root",database="agence")

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

NOM = Input(WIDTH/2 - 100, 75, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_NOM = FONT.render('Nom : ',1,BLACK)

PRENOM = Input(WIDTH/2 - 100, 155, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_PRENOM = FONT.render('PRENOM : ',1,BLACK)

PASSWORD = Input(WIDTH/2 - 100, 550, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_PASSWORD = FONT.render('MOT DE PASSE : ',1,BLACK)

#CONNEXION = pygame.Rect(WIDTH/2 , 320, 150,30)
TEXT_CONNEXION = FONT.render('SE CONNECTER',1, WHITE )

DATE_DEPART = Input(WIDTH/2 - 100, 250, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_DD = FONT.render('Date départ : ',1,BLACK)

DATE_RETOUR = Input(WIDTH/2 - 100, 355, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_DR = FONT.render('Date retour : ',1,BLACK)

BUDGET = Input(WIDTH/2 - 100, 450, 200, 30,WIDTH,HEIGHT,WINDOW_3)
TEXT_BUDGET = FONT.render('Budget : ',1,BLACK)

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
UI_REFRESH_RATE = CLOCK.tick(60) / 100000

#se_connecter =pygame.draw.rect(WINDOW,BLUE,CONNEXION)

SE_CONNECTER = ButtonRectangle(WIDTH/2,600,150,30,BLUE,'SE CONNECTER',None,WHITE)


def draw_window_2():
    WINDOW_3.fill(WHITE)
    
    SE_CONNECTER.draw(WINDOW_3)

    WINDOW_3.blit(TEXT_NOM,(WIDTH/2 - 100,55))
    WINDOW_3.blit(TEXT_PRENOM,(WIDTH/2 - 100,135 ))
    WINDOW_3.blit(TEXT_CONNEXION,(WIDTH/2 + 18  , 607))
    WINDOW_3.blit(TEXT_DD,(WIDTH/2 - 100,235))
    WINDOW_3.blit(TEXT_DR,(WIDTH/2 - 100,335))
    WINDOW_3.blit(TEXT_BUDGET,(WIDTH/2 - 100,435))
    WINDOW_3.blit(TEXT_PASSWORD,(WIDTH/2 - 100,550))


    NOM.draw_rectangle()
    NOM_input = NOM.get_input()
    print("Nom :", NOM_input)

    PRENOM.draw_rectangle()
    PRENOM_input = PRENOM.get_input()
    print("PRENOM :", PRENOM_input)

    


    DATE_DEPART.draw_rectangle()
    DATE_DEPART_input = DATE_DEPART.get_input()
    print("Date départ :", DATE_DEPART_input)
 
    DATE_RETOUR.draw_rectangle()
    DATE_RETOUR_input = DATE_RETOUR.get_input()
    print("Date Retour :", DATE_RETOUR_input)

    BUDGET.draw_rectangle()
    BUDGET_input = BUDGET.get_input()
    print("BUDGET :", BUDGET_input)

    PASSWORD.draw_rectangle()
    PASSWORD_input = PASSWORD.get_input()
    f_ajouteclient(None,NOM_input,PRENOM_input,None,None,DATE_DEPART_input,DATE_RETOUR_input,None,None,PASSWORD_input)
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

