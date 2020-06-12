import pygame
from os import path
pygame.init()
WIDTH = 1000
HEIGHT = 520

def jogo(window):
    estado = 'jogo'
    # Estabelece a pasta que contem as figuras e sons.
    img_dir = path.join(path.dirname(_file_), 'img')

    # Dados gerais do jogo.
    TITULO = 'Exemplo de Pulo com obstáculos'
    WIDTH = 480 # Largura da tela
    HEIGHT = 600 # Altura da tela
    TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
    PLAYER_WIDTH = TILE_SIZE
    PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
    FPS = 60 # Frames por segundo

    # Imagens
    PLAYER_IMG = 'player_img'

    BLACK = (0, 0, 0)
    GRAVITY = 5
    JUMP_SIZE = 0.7*TILE_SIZE
    # Define a velocidade em x
    SPEED_X = 5


    # Define os tipos de tiles
    BLOCK = 0
    PLATF = 1
    EMPTY = -1

    # Define o mapa com os tipos de tiles
    MAP = [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, PLATF, PLATF, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY, EMPTY],
        [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
        [EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
        [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
        [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    ]

    # Define estados possíveis do jogador
    STILL = 0
    JUMPING = 1
    FALLING = 2

    # Class que representa os blocos do cenário
    class Tile(pygame.sprite.Sprite):

        # Construtor da classe.
        def _init_(self, tile_img, row, column):
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite._init_(self)

            # Aumenta o tamanho do tile.
            tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

            # Define a imagem do tile.
            self.image = tile_img
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()

            # Posiciona o tile
            self.rect.x = TILE_SIZE * column
            self.rect.y = TILE_SIZE * row


    # Classe Jogador que representa o herói
    class Player(pygame.sprite.Sprite):

        # Construtor da classe.
        def _init_(self, player_img, row, column, platforms, blocks):

            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite._init_(self)

            # Define estado atual
            # Usamos o estado para decidir se o jogador pode ou não pular
            self.state = STILL

            # Ajusta o tamanho da imagem
            player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

            # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
            self.image = player_img
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()

            # Guarda os grupos de sprites para tratar as colisões
            self.platforms = platforms
            self.blocks = blocks

            # Posiciona o personagem
            # row é o índice da linha embaixo do personagem
            self.rect.x = column * TILE_SIZE
            self.rect.bottom = row * TILE_SIZE

            # Inicializa velocidades
            self.speedx = 0
            self.speedy = 0

            # Define altura no mapa
            # Essa variável sempre conterá a maior altura alcançada pelo jogador
            # antes de começar a cair
            self.highest_y = self.rect.bottom

        # Metodo que atualiza a posição do personagem
        def update(self):
            # Vamos tratar os movimentos de maneira independente.
            # Primeiro tentamos andar no eixo y e depois no x.

            # Tenta andar em y
            # Atualiza a velocidade aplicando a aceleração da gravidade
            self.speedy += GRAVITY
            # Atualiza o estado para caindo
            if self.speedy > 0:
                self.state = FALLING
            # Atualiza a posição y
            self.rect.y += self.speedy

            # Atualiza altura no mapa
            if self.state != FALLING:
                self.highest_y = self.rect.bottom

            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para baixo
                if self.speedy > 0:
                    self.rect.bottom = collision.rect.top
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL
                # Estava indo para cima
                elif self.speedy < 0:
                    self.rect.top = collision.rect.bottom
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL

            # Tratamento especial para plataformas
            # Plataformas devem ser transponíveis quando o personagem está pulando
            # mas devem pará-lo quando ele está caindo. Para pará-lo é necessário que
            # o jogador tenha passado daquela altura durante o último pulo.
            if self.speedy > 0:  # Está indo para baixo
                collisions = pygame.sprite.spritecollide(self, self.platforms, False)
                # Para cada tile de plataforma que colidiu com o personagem
                # verifica se ele estava aproximadamente na parte de cima
                for platform in collisions:
                    # Verifica se a altura alcançada durante o pulo está acima da
                    # plataforma.
                    if self.highest_y <= platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        # Atualiza a altura no mapa
                        self.highest_y = self.rect.bottom
                        # Para de cair
                        self.speedy = 0
                        # Atualiza o estado para parado
                        self.state = STILL

            # Tenta andar em x
            self.rect.x += self.speedx
            # Corrige a posição caso tenha passado do tamanho da janela
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH - 1
            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            # O personagem não colide com as plataformas quando está andando na horizontal
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para a direita
                if self.speedx > 0:
                    self.rect.right = collision.rect.left
                # Estava indo para a esquerda
                elif self.speedx < 0:
                    self.rect.left = collision.rect.right

        # Método que faz o personagem pular
        def jump(self):
            # Só pode pular se ainda não estiver pulando ou caindo
            if self.state == STILL:
                self.speedy -= JUMP_SIZE
                self.state = JUMPING


    # Carrega todos os assets de uma vez.
    def load_assets(img_dir):
        assets = {}
        assets[PLAYER_IMG] = pygame.image.load('assets/img/personagem_sprite.png').convert_alpha()
        assets[BLOCK] = pygame.image.load('assets/img/tile-block.png').convert()
        assets[PLATF] = pygame.image.load('assets/img/tile-wood.png').convert()
        return assets


    

    clock = pygame.time.Clock()


    assets = load_assets(img_dir)

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks)

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == BLOCK:
                    blocks.add(tile)
                elif tile_type == PLATF:
                    platforms.add(tile)
    all_sprites.add(player)

    jogorodando = True

    while jogorodando:
        clock.tick(FPS)
        for event in pygame.event.get():

                # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                jogorodando = False
                estado = 'cabo'

                # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

                # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

            # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        all_sprites.draw(window)

            # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

 
    return estado