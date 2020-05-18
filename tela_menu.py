import pygame

pygame.init()

# ----- Gera tela principal
def menu(window):
    WIDTH = 1000
    HEIGHT = 536
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # ----- Inicia estruturas de dados
    rodando = True

    # ----- Inicia assets
    image = pygame.image.load('assets/img/imagem_menu.png').convert()
    font = pygame.font.SysFont(None, 100)
    text = font.render('Semeru', True, (0, 0, 0))

    # ===== Loop principal =====
    while rodando:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
        
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = 'sair'
                rodando = False
            if event.type == pygame.KEYUP:
                estado = 'jogo'
                rodando = False


        # ----- Gera saídas
        window.blit(image, (0, 0))
        window.blit(text, (150, 100))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    return estado
