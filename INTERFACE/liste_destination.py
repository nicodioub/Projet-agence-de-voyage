#Liste destination 

#interface_modif_pro


#Interface apres connexion au compte client 
# on doit avoir un historique des voyages et pouvoir 
import pygame 
import os 
from button import ButtonRectangle
from button import Button_image
from class_input import Input
import pygame_gui
pygame.init()
import interface_details_client as detail
pygame.font.init()


# On peut essayer de faire des fenetres qui se croisent ca devraitt marcher normalement 

WHITE = (255 , 255 , 255)
BEIGE = (249,228,183)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE =  (44,117,255)
GRIS = (206,206,206)
FPS=60 # On pourrait utiliser le time clock pour que les images se superposent et s'échangent 


LONGUEUR, LARGEUR = 300, 600
WIDTH,HEIGHT = 450,650

IMAGE_MOY_LONG = 100
IMAGE_MOY_LARG = 50
IMAGE_MOYENNE_HAUTEUR =350
FONT = pygame.font.SysFont(None,20)


WINDOW = pygame.display.set_mode((LONGUEUR, LARGEUR))
pygame.display.set_caption("Liste destination")

PARIS= ButtonRectangle(1, 1,298,35,WHITE,'',None,WHITE)
TEXT_PARIS = FONT.render('PARIS  ',1, BLACK )

TOKYO= ButtonRectangle(1, 36,298,35,GRIS,'',None,WHITE)
TEXT_TOKYO = FONT.render('TOKYO ',1, BLACK )

NYC= ButtonRectangle(1, 71 ,298,35,WHITE,'',None,WHITE)
TEXT_NYC = FONT.render('NEW YORK CITY',1, BLACK )

DUBAI= ButtonRectangle(1, 106,298,35,GRIS,'',None,WHITE)
TEXT_DUBAI = FONT.render('DUBAI',1, BLACK )

LONDON= ButtonRectangle(1, 141,298,35,WHITE,'',None,WHITE)
TEXT_LONDON = FONT.render('LONDON',1, BLACK )

LOS_ANGELES= ButtonRectangle(1, 176,298,35,GRIS,'',None,WHITE)
TEXT_LOS_ANGELES = FONT.render('LOS ANGELES',1, BLACK )

HONG_KONG= ButtonRectangle(1, 211,298,35,WHITE,'',None,WHITE)
TEXT_HONG_KONG = FONT.render('HONG KONG',1, BLACK )

SINGAPOUR= ButtonRectangle(1, 246,298,35,GRIS,'',None,WHITE)
TEXT_SINGAPOUR = FONT.render('SINGAPOUR',1, BLACK )

SYDNEY= ButtonRectangle(1, 281,298,35,WHITE,'',None,WHITE)
TEXT_SYDNEY = FONT.render('SYDNEY',1, BLACK )

ROME= ButtonRectangle(1, 316,298,35,GRIS,'',None,WHITE)
TEXT_ROME = FONT.render('ROME',1, BLACK )

BARCELONE= ButtonRectangle(1, 351,298,35,WHITE,'',None,WHITE)
TEXT_BARCELONE = FONT.render('BARCELONE',1, BLACK )

MIAMI= ButtonRectangle(1, 386,298,35,GRIS,'',None,WHITE)
TEXT_MIAMI = FONT.render('MIAMI',1, BLACK )

SHANGAI= ButtonRectangle(1, 421,298,35,WHITE,'',None,WHITE)
TEXT_SHANGAI = FONT.render('SHANGAI',1, BLACK )

MOSCOU= ButtonRectangle(1, 456,298,35,GRIS,'',None,WHITE)
TEXT_MOSCOU = FONT.render('MOSCOU',1, BLACK )

TORONTO= ButtonRectangle(1, 491,298,35,WHITE,'',None,WHITE)
TEXT_TORONTO = FONT.render('TORONTO',1, BLACK )

BERLIN= ButtonRectangle(1, 526,298,35,GRIS,'',None,WHITE)
TEXT_BERLIN = FONT.render('BERLIN',1, BLACK )

VIENNE= ButtonRectangle(1, 561,298,35,WHITE,'',None,WHITE)
TEXT_VIENNE = FONT.render('VIENNE',1, BLACK )

NEXT_1= ButtonRectangle(1, 561,298,35,WHITE,'',None,WHITE)
TEXT_NEXT = FONT.render('NEXT -->',1, RED )



BACK= ButtonRectangle(1, 435,298,35,BLUE,'',None,WHITE)
TEXT_BACK = FONT.render('<-- BACK',1, RED )



# WINDOW 3 

MELBOURNE= ButtonRectangle(1, 1,298,35,WHITE,'',None,WHITE)
TEXT_MELBOURNE = FONT.render('MELBOURNE  ',1, BLACK )

MUMBAI= ButtonRectangle(1, 36,298,35,GRIS,'',None,WHITE)
TEXT_MUMBAI = FONT.render('TOKYO ',1, BLACK )

ZURICH= ButtonRectangle(1, 71 ,298,35,WHITE,'',None,WHITE)
TEXT_ZURICH = FONT.render('NEW YORK CITY',1, BLACK )

SAN_FRANCISCO= ButtonRectangle(1, 106,298,35,GRIS,'',None,WHITE)
TEXT_SAN_FRANCISCO = FONT.render('DUBAI',1, BLACK )

BUENOS_AIRES= ButtonRectangle(1, 141,298,35,WHITE,'',None,WHITE)
TEXT_BUENOS_AIRES = FONT.render('LONDON',1, BLACK )

AMSTERDAM= ButtonRectangle(1, 176,298,35,GRIS,'',None,WHITE)
TEXT_AMSTERDAM = FONT.render('LOS ANGELES',1, BLACK )

SEOUL= ButtonRectangle(1, 211,298,35,WHITE,'',None,WHITE)
TEXT_SEOUL = FONT.render('HONG KONG',1, BLACK )

MUNICH= ButtonRectangle(1, 246,298,35,GRIS,'',None,WHITE)
TEXT_MUNICH = FONT.render('SINGAPOUR',1, BLACK )

MONTE_CARLO= ButtonRectangle(1, 281,298,35,WHITE,'',None,WHITE)
TEXT_MONTE_CARLO = FONT.render('SYDNEY',1, BLACK )

CAPE_TOWN= ButtonRectangle(1, 316,298,35,GRIS,'',None,WHITE)
TEXT_CPAE_TOWN = FONT.render('ROME',1, BLACK )

MADRID= ButtonRectangle(1, 351,298,35,WHITE,'',None,WHITE)
TEXT_MADRID = FONT.render('BARCELONE',1, BLACK )

ATHENE= ButtonRectangle(1, 386,298,35,GRIS,'',None,WHITE)
TEXT_ATHENE = FONT.render('MIAMI',1, BLACK )

ABIDJAN= ButtonRectangle(1, 421,298,35,WHITE,'',None,WHITE)
TEXT_ABIDJAN = FONT.render('SHANGAI',1, BLACK )


def draw_window_45():
    WINDOW.fill(BEIGE)

    PARIS.draw(WINDOW)
    WINDOW.blit(TEXT_PARIS,(120,10))

    TOKYO.draw(WINDOW)
    WINDOW.blit(TEXT_TOKYO,(120,45))

    NYC.draw(WINDOW)
    WINDOW.blit(TEXT_NYC,(80,80))

    DUBAI.draw(WINDOW)
    WINDOW.blit(TEXT_DUBAI,(120,115))

    LONDON.draw(WINDOW)
    WINDOW.blit(TEXT_LONDON,(110,150))

    LOS_ANGELES.draw(WINDOW)
    WINDOW.blit(TEXT_LOS_ANGELES,(100,185))

    HONG_KONG.draw(WINDOW)
    WINDOW.blit(TEXT_HONG_KONG,(120,220))

    SINGAPOUR.draw(WINDOW)
    WINDOW.blit(TEXT_SINGAPOUR,(110,255))

    SYDNEY.draw(WINDOW)
    WINDOW.blit(TEXT_SYDNEY,(120,290))

    ROME.draw(WINDOW)
    WINDOW.blit(TEXT_ROME,(120,325))

    BARCELONE.draw(WINDOW)
    WINDOW.blit(TEXT_BARCELONE,(120,360))

    MIAMI.draw(WINDOW)
    WINDOW.blit(TEXT_MIAMI,(120,395))

    SHANGAI.draw(WINDOW)
    WINDOW.blit(TEXT_SHANGAI,(120,430))

    MOSCOU.draw(WINDOW)
    WINDOW.blit(TEXT_MOSCOU,(120,475))

    TORONTO.draw(WINDOW)
    WINDOW.blit(TEXT_TORONTO,(120,510))

    BERLIN.draw(WINDOW)
    WINDOW.blit(TEXT_BERLIN,(120,545))

    NEXT_1.draw(WINDOW)
    WINDOW.blit(TEXT_NEXT,(120,580))

    pygame.display.update() 

def draw_window_35():
    WINDOW.fill(BEIGE)
    MELBOURNE.draw(WINDOW)
    WINDOW.blit(TEXT_MELBOURNE,(120,10))

    MUMBAI.draw(WINDOW)
    WINDOW.blit(TEXT_MUMBAI,(120,45))

    ZURICH.draw(WINDOW)
    WINDOW.blit(TEXT_ZURICH,(80,80))

    SAN_FRANCISCO.draw(WINDOW)
    WINDOW.blit(TEXT_SAN_FRANCISCO,(120,115))

    BUENOS_AIRES.draw(WINDOW)
    WINDOW.blit(TEXT_BUENOS_AIRES,(110,150))

    AMSTERDAM.draw(WINDOW)
    WINDOW.blit(TEXT_LOS_ANGELES,(100,185))

    SEOUL.draw(WINDOW)
    WINDOW.blit(TEXT_SEOUL,(120,220))

    MUNICH.draw(WINDOW)
    WINDOW.blit(TEXT_MUNICH,(110,255))

    MONTE_CARLO.draw(WINDOW)
    WINDOW.blit(TEXT_MONTE_CARLO,(120,290))

    CAPE_TOWN.draw(WINDOW)
    WINDOW.blit(TEXT_CPAE_TOWN,(120,290))

    MADRID.draw(WINDOW)
    WINDOW.blit(TEXT_MADRID,(120,325))

    ATHENE.draw(WINDOW)
    WINDOW.blit(TEXT_ATHENE,(120,360))

    ABIDJAN.draw(WINDOW)
    WINDOW.blit(TEXT_ABIDJAN,(120,395))

    VIENNE.draw(WINDOW)
    WINDOW.blit(TEXT_VIENNE,(120,545))

    BACK.draw(WINDOW)
    WINDOW.blit(TEXT_BACK,(120,430))

    

    pygame.display.update() 

def main():

    clock = pygame.time.Clock()
    run = True 
    while run : 
        clock.tick(FPS)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : 
                run = False 

            if PARIS.draw(WINDOW):
                run = False 
                WINDOW_1 = pygame.display.set_mode((WIDTH, HEIGHT))
                detail.main()

            #if NEXT_1.draw(WINDOW):
                #run = False 
                #draw_window_35()

            #if BACK.draw(WINDOW):
               # run = False 
                #draw_window_45()
            
             
        

        draw_window_45()
        #if user_input == id and user_input2 == passs:
                #run = False
    pygame.quit()

if __name__ == '__main__':
    main()