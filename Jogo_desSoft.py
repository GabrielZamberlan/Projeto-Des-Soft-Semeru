import pygame
from tela_menu import menu
from tela_jogo import jogo

pygame.init()

WIDTH = 1000
HEIGHT = 536
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Semeru')

state = 'menu'
while state != 'sair':
    if state == 'menu':
        state = menu(window)
    elif state == 'jogo':
        state = jogo(window)
    else:
        state = 'sair'

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

