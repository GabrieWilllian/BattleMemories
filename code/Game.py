import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        # Texto que vai aparecer no terminal.
        pygame.init()
        # Criando a janela onde o jogo vai roda/aparecer.
        # window - é uma variável que vai receber a tela.
        # O tamanho da tela é uma tupla
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()



