import pygame
from tela_menu import menu
from tela_jogo import jogo

pygame.init()
pygame.mixer.init()

WIDTH = 1000
HEIGHT = 520
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Semeru')

estado = 'menu'
while estado != 'sair':
    if estado == 'menu':
        estado = menu(window)
    elif estado == 'jogo':
        estado = jogo(window)
    else:
        estado = 'sair'

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

