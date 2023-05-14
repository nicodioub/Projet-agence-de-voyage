import pygame 
import os 
from button import ButtonRectangle
from button import Button_image
from class_input import Input
import pygame_gui
import Interface_Agence_de_voyage as IAV
import interface_identifiant_de_connexion as iic
import interface_id_pro as iip
import interface_details_client as idc
import liste_destination as liste_des
import interface_historique_client as histo
pygame.font.init()
pygame.init()



# On peut essayer de faire des fenetres qui se croisent ca devraitt marcher normalement 


FPS=60 # On pourrait utiliser le time clock pour que les images se superposent et s'échangent 

IMAGE_MOYENNE_HAUTEUR =350
WHITE = (255,255,255)
LONGUEUR, LARGEUR = 1200, 600
WIDTH,HEIGHT = 450,450
WIDTH_LISTE,HEIGHT_LISTE = 300,600
WIDTH_DETAILS,HEIGHT_DETAILS = 450,650
WINDOW_1 = pygame.display.set_mode((LONGUEUR, LARGEUR))

image_path_paris = pygame.image.load(os.path.join('IMAGE/Paris.jpg')).convert_alpha()
PARIS = Button_image(1,IMAGE_MOYENNE_HAUTEUR,image_path_paris,LONGUEUR/3 - 2,LARGEUR/3,1)

image_path_loupe = pygame.image.load(os.path.join('IMAGE/search image.png')).convert_alpha()
SEARCH_OBJECT_IMAGE = Button_image(810,160,image_path_loupe,20,20,1)

image_path_2 = pygame.image.load(os.path.join('IMAGE/id_pro.jpg')).convert_alpha()

image_path = pygame.image.load(os.path.join('IMAGE/identifiant.webp')).convert_alpha()
IDENTIFIANT_CLIENT = Button_image(1140,20,image_path,50,50,1)
IDENTIFIANT_PRO = Button_image(1090,20,image_path_2,50,50,1)

NEXT_1= ButtonRectangle(1, 561,298,35,WHITE,'',None,)
pygame.display.set_caption("Agence Tout-Risque")



def main_x():

    clock = pygame.time.Clock()
    run = True 
    while run : 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # Fonction permettant de quitter la fenêtre 
                run = False 
            if PARIS.draw(WINDOW_1):
                run = False 
                WINDOW = pygame.display.set_mode((WIDTH_DETAILS,HEIGHT_DETAILS))
                idc.main()

            if IDENTIFIANT_CLIENT.draw(WINDOW_1):
                run = False 
                WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
                iic.main()  
                 

            if IDENTIFIANT_PRO.draw(WINDOW_1):
                run = False 
                WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
                iip.main()

            if SEARCH_OBJECT_IMAGE.draw(WINDOW_1) :
                run = False 
                WINDOW = pygame.display.set_mode((WIDTH_LISTE,HEIGHT_LISTE))
                liste_des.main()
            
            
        
            
        
        IAV.draw_window_1()
    pygame.quit()

if __name__ == '__main__':
    main_x()

