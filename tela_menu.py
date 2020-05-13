import pygame

pygame.init()

# ----- Gera tela principal
def menu(window):
    WIDTH = 1000
    HEIGHT = 536
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # ----- Inicia estruturas de dados
    game = True

    # ----- Inicia assets
    image = pygame.image.load('assets/img/imagem_menu.png').convert()
    font = pygame.font.SysFont(None, 100)
    text = font.render('Semeru', True, (0, 0, 0))

    # ===== Loop principal =====
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
        
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = 'sair'
            if event.type == pygame.KEYUP:
                state = 'jogo'
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        window.blit(image, (0, 0))
        window.blit(text, (150, 100))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    return state
