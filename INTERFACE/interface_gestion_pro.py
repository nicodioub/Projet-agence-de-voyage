#Interface apres connexion au compte client 
# on doit avoir un historique des voyages et pouvoir 
import pygame 
import os 
from mysql.connector import connect
from button import ButtonRectangle
from button import Button_image
from class_input import Input
import pygame_gui
import Interface_Agence_de_voyage as IAV
import partie1 as fonction
import main_

pygame.font.init()
pygame.init()

# On peut essayer de faire des fenetres qui se croisent ca devraitt marcher normalement 

#Connected sur Mysql
bdd=connect(host="localhost",user="root",password="root",database="agence")

def f_suppclient(cli_id):
    cursor=bdd.cursor()
    sql="DELETE FROM clients WHERE cli_id="+str(cli_id)
    cursor.execute(sql)
    bdd.commit()   

def f_afficheclient(cli_id):
    cursor = bdd.cursor()
    sql = ""


WHITE = (255 , 255 , 255)
BEIGE = (249,228,183)
BLACK = (0,0,0)
BLUE =  (44,117,255)
FPS=60 # On pourrait utiliser le time clock pour que les images se superposent et s'échangent 
FONT = pygame.font.SysFont(None,20)

LONGUEUR, LARGEUR = 1200, 600

CREATION_CLIENT = ButtonRectangle(1,320,150,30,BLACK,'Historique',None,WHITE)
TEXT_CREA_CLIENT = FONT.render('Création client  ',1, WHITE )

MODIFICATION_CLIENT = pygame.Rect(1,120,150,30)
TEXT_MODIF = FONT.render('Modification client',1, WHITE )

SECURITE = ButtonRectangle(1, 220,150,30,BLACK,'Sécurité',None,WHITE)
TEXT_SECURITE = FONT.render('Sécurité ',1, WHITE )

DECONNEXION  = ButtonRectangle(1, 520,150,30,BLACK,'Sécurité',None,WHITE)
TEXT_DECONNEXION = FONT.render('Déconnexion ',1, WHITE )

ACCEUIL  = ButtonRectangle(1, 35,150,30,BLACK,'Sécurité',None,WHITE)
TEXT_ACCEUIL = FONT.render('Acceuil ',1, WHITE )

NOTIFICATIONS  = ButtonRectangle(1, 420,150,30,BLACK,'Sécurité',None,WHITE)
TEXT_NOTIFICATIONS = FONT.render('Notifications ',1, WHITE )


WINDOW = pygame.display.set_mode((LONGUEUR, LARGEUR))
pygame.display.set_caption("Compte client")

MENU = pygame.Rect(0,0,150,30)
TEXT_AGENCE = FONT.render(" MENU",1, BLACK )

def afficher_clients2(WINDOW):
    cursor = bdd.cursor()
    sql = "SELECT * FROM clients"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:        
        ID  = ("ID", row[0])

def draw_window_9():
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW,BLACK,MENU,2)
    pygame.draw.rect(WINDOW,BLACK,MODIFICATION_CLIENT)

    CREATION_CLIENT.draw(WINDOW)

    ACCEUIL.draw(WINDOW)
    WINDOW.blit(TEXT_ACCEUIL,(30,45))
    WINDOW.blit(TEXT_AGENCE,(20,15))
    SECURITE.draw(WINDOW)

    WINDOW.blit(TEXT_SECURITE,(30,225))
    WINDOW.blit(TEXT_CREA_CLIENT,(30,328))
    WINDOW.blit(TEXT_MODIF,(20,127))

    NOTIFICATIONS.draw(WINDOW)
    WINDOW.blit(TEXT_NOTIFICATIONS,(30,425))

    DECONNEXION.draw(WINDOW)
    WINDOW.blit(TEXT_DECONNEXION,(30,525))


    pygame.display.update() 

def main():

    clock = pygame.time.Clock()
    run = True 
    while run : 
        clock.tick(FPS)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : 
                run = False 
            
            # Afficher les clients 
            if event.type == pygame.MOUSEBUTTONDOWN:  # vérifie si l'utilisateur a cliqué sur l'écran
                mouse_pos = pygame.mouse.get_pos()  # récupère la position de la souris
                if MODIFICATION_CLIENT.collidepoint(mouse_pos):  # vérifie si la position de la souris est sur le rectangle "Voyage à venir"
                    fonction.afficher_clients(WINDOW)

            

            if ACCEUIL.draw(WINDOW):
                run = False 
                main_.main_x()

            


        draw_window_9()
        #if user_input == id and user_input2 == passs:
                #run = False
    pygame.quit()
if __name__ == '__main__':
    main()