import pygame
pygame.init()
def jogo(window):
    jogo = True

    # ===== Loop principal =====
    while jogo:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                jogo = False
                estado = 'cabo'

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
    return estado