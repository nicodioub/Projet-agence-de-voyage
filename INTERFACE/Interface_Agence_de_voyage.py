# Interface d'acceuil
import pygame 
import os 
from button import ButtonRectangle
from button import Button_image
from class_input import Input
import pygame_gui
pygame.init()
pygame.font.init()


# On peut essayer de faire des fenetres qui se croisent ca devraitt marcher normalement 

WHITE = (255 , 255 , 255)
BEIGE = (249,228,183)
BLACK = (0,0,0)
BLUE =  (44,117,255)
FPS=60 # On pourrait utiliser le time clock pour que les images se superposent et s'échangent 


LONGUEUR, LARGEUR = 1200, 600

IMAGE_MOY_LONG = 100
IMAGE_MOY_LARG = 50
IMAGE_MOYENNE_HAUTEUR =350


WINDOW = pygame.display.set_mode((LONGUEUR, LARGEUR))
pygame.display.set_caption("Agence Tout-Risque")

SEARCH_BAR = Input(200,150,600,40,LONGUEUR,LARGEUR,WINDOW) #(x,y,longueur,largeur)

image_path_loupe = pygame.image.load(os.path.join('IMAGE/search image.png')).convert_alpha()
SEARCH_OBJECT_IMAGE = Button_image(810,160,image_path_loupe,20,20,1)



TOKYO_IMAGE = pygame.image.load(os.path.join('IMAGE/Tokyo.jpg')).convert_alpha()
TOKYO = pygame.transform.smoothscale(TOKYO_IMAGE,(LONGUEUR/3 - 2,LARGEUR/3))

THAILAND_IMAGE = pygame.image.load(os.path.join('IMAGE/thaipic2.jpg')).convert_alpha()
THAILAND = pygame.transform.smoothscale(THAILAND_IMAGE,(LONGUEUR/3 - 2,LARGEUR/3)).convert_alpha()

image_path_paris = pygame.image.load(os.path.join('IMAGE/Paris.jpg')).convert_alpha()
PARIS = Button_image(1,IMAGE_MOYENNE_HAUTEUR,image_path_paris,LONGUEUR/3 - 2,LARGEUR/3,1)

AGENCE_FONT = pygame.font.SysFont(None,40)
RESEARCH_BAR_FONT = pygame.font.SysFont(None,30)
RESEARCH_BAR_TEXT = 'Rechercher une destination...'

RESEARCH_TEXT = RESEARCH_BAR_FONT.render(RESEARCH_BAR_TEXT,1,BLACK)
TEXT_AGENCE = AGENCE_FONT.render(" Agencetourisque.com",1, BLACK )

image_path_id_client = pygame.image.load(os.path.join('IMAGE/identifiant.webp')).convert_alpha()
image_path_id_pro = pygame.image.load(os.path.join('IMAGE/id_pro.jpg')).convert_alpha()

IDENTIFIANT_CLIENT = Button_image(1140,20,image_path_id_client,50,50,1)
IDENTIFIANT_PRO = Button_image(1090,20,image_path_id_pro,50,50,1)


def draw_window_1():

    WINDOW.fill((BEIGE))

    WINDOW.blit(TOKYO,(803, IMAGE_MOYENNE_HAUTEUR))
    WINDOW.blit(THAILAND,(LONGUEUR/3 + 2,IMAGE_MOYENNE_HAUTEUR))
    PARIS.draw(WINDOW)
    

    SEARCH_OBJECT_IMAGE.draw(WINDOW)
    IDENTIFIANT_CLIENT.draw(WINDOW)
    IDENTIFIANT_PRO.draw(WINDOW)

    WINDOW.blit(RESEARCH_TEXT,(210,159))
 
    WINDOW.blit(TEXT_AGENCE,(0,5))

    #SEARCH_BAR.draw_rectangle()
    #user_input = SEARCH_BAR.get_input()
    #print("User input:", user_input)


    pygame.display.update()
   

def main():

    clock = pygame.time.Clock()
    run = True 
    while run : 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # Fonction permettant de quitter la fenêtre 
                run = False 
            if IDENTIFIANT_CLIENT.draw(WINDOW):
                print('Connexion is succesful')
            if IDENTIFIANT_PRO.draw(WINDOW):
                print('ouf')
        
            
        
        draw_window_1()
    pygame.quit()
if __name__ == '__main__':
    main()