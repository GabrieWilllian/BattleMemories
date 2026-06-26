import pygame

#Texto que vai aparecer no terminal.
print("Start Setup")
pygame.init()
#Criando a janela onde o jogo vai roda/aparecer.
#window - é uma variável que vai receber a tela.
#O tamanho da tela é uma tupla
window = pygame.display.set_mode((1280, 720))
print("Start End")

print("Loop Start")
#Estou criando um loop para a janela se manter aberta.
while True:
    #verifica todos os eventos.
    for event in pygame.event.get():
        #Se o evento for do tipo pygame.QUIT
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela
            quit() # Encerra o pygame
