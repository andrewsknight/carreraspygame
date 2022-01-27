import pygame, sys

width = 640
height = 480
#Para hacer aparecer una pantalla
screen = pygame.display.set_mode((width, height))
#Para darle color a la pantalla
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo básico de pygame")

pygame.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    #Refresca la imagen, Muy importante.
    pygame.display.flip()      
pygame.quit()
            
