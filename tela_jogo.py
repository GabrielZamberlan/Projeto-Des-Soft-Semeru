import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 536
def jogo(window):
    personagem_width = 50
    personagem_hight = 60
    mable_img = pygame.image.load('assets/img/personagem_sprite.png').convert_alpha()
    mable_img = pygame.transform.scale(mable_img, (personagem_width, personagem_hight))

    # ----- Inicia estruturas de dados
    # Definindo os novos tipos
    class mable(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0

        def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx

            # Mantem dentro da tela
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
    jogo = True
    clock = pygame.time.Clock()
    FPS = 30

    all_sprites = pygame.sprite.Group()
    # Criando o jogador
    player = mable(mable_img)
    all_sprites.add(player)
    # ===== Loop principal =====
    while jogo:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                jogo = False
                estado = 'cabo'
        all_sprites.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
    return estado