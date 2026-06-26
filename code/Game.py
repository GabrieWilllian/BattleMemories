import pygame

from code.Menu import Menu

class Game:
    def __init__(self):
        # Texto que vai aparecer no terminal.
        pygame.init()
        # Criando a janela onde o jogo vai roda/aparecer.
        # window - é uma variável que vai receber a tela.
        # O tamanho da tela é uma tupla
        self.window = pygame.display.set_mode((1280, 720))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()



            ##verifica todos os eventos.
            #for event in pygame.event.get():
                ##Se o evento for do tipo pygame.QUIT
                #if event.type == pygame.QUIT:
                  #  pygame.quit() # Fecha a janela
                    #quit() # Encerra o pygame
