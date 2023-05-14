import pygame

pygame.init()

# Récupérer les dimensions de l'écran
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Initialiser la fenêtre Pygame en plein écran
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Afficher une image de fond
background = pygame.image.load("IMAGE/AVION.jpg")
background = pygame.transform.scale(background, (screen_width/2, screen_height/2))
screen.blit(background, (100, 100))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
