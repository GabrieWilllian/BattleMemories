import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        #Carrega a imagem
        self.surf = pygame.image.load('./assets/Background/Battleground1/Bright/Battleground1.png')
        #Criando um retangulo invisivel
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        # Carrega a música
        pygame.mixer_music.load('./assets/music/623427__zhr__medieval-various-music.mp3')
        # Toca a música
        # O parametro (-1) faz a música tocar em loop
        pygame.mixer_music.play(-1)

        while True:
            # Atualizando a imagem que vai aparecer
            self.window.blit(source=self.surf, dest=self.rect)

            #Escreve o texto no menu inicial
            self.menu_text(text_size=200, text="Battle Memories", text_color=(255, 255, 255), text_center_pos=((WIN_WIDTH / 2), 300))

            #Controla o texto NEW GAME e EXIT
            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=80, text=MENU_OPTION[i], text_color=(255, 255, 255), text_center_pos=((WIN_WIDTH / 2), 750 + 100 * i))


            pygame.display.flip()


            #verifica todos os eventos.
            for event in pygame.event.get():
                #Se o evento for do tipo pygame.QUIT
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha a janela
                    quit() # Encerra o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect:  Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
