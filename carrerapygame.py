import pygame
import sys



class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/img0.png")
        imagen_redimensionada = pygame.image.load("images/img26.png")
        self.runner = pygame.transform.scale(imagen_redimensionada, (30,60))
        
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.__screen.blit(self.background,(0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                hayGanador = True
            
     
     
     
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()