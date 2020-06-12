import pygame
from os import path
pygame.init()
WIDTH = 1000
HEIGHT = 520

def jogo(window):
    img_dir = path.join(path.dirname(__file__), 'img')
    TILE_SIZE = 40
    PLAYER_WIDTH = TILE_SIZE
    PLAYER_HEIGHT = int(TILE_SIZE*1.5)
    GRAVITY = 5
    JUMP_SIZE = TILE_SIZE
    SPEED_X = 5
    #vazio = 0
    #bloco = 1
    #plataforma = 2
    MAP = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    class Tile(pygame.sprite.Sprite):

        # Construtor da classe.
        def __init__(self, tile_img, row, column):
            pygame.sprite.Sprite.__init__(self)

            tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))


            self.image = tile_img
            self.rect = self.image.get_rect()

            self.rect.x = TILE_SIZE * column
            self.rect.y = TILE_SIZE * row


    class mable(pygame.sprite.Sprite):

        def __init__(self, player_img, row, column, platforms, blocks):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.state = "parado"
            player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            self.image = player_img
            self.rect = self.image.get_rect()
            self.blocks = blocks
            self.rect.x = column * TILE_SIZE
            self.rect.bottom = row * TILE_SIZE
            self.speedx = 0
            self.speedy = 5
            self.highest_y = self.rect.bottom
            self.platforms = platforms
        def update(self):
            if self.speedy > 0:
                self.state = "caindo"
            if self.state == "caindo":
                self.speedy = GRAVITY
            self.rect.y += self.speedy
            if self.state != "caindo":
                self.highest_y = self.rect.bottom
            
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            for collision in collisions:
                if self.speedy > 0:
                    self.rect.bottom = collision.rect.top
                    self.speedy = 0
                    self.state = "parado"
                elif self.speedy < 0:
                    self.rect.top = collision.rect.bottom
                    self.speedy = 0
                    self.state = "parado"
            if self.speedy > 0:  
                collisions = pygame.sprite.spritecollide(self, self.platforms, False)
                for platform in collisions:
                    if self.highest_y <= platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        self.highest_y = self.rect.bottom
                        self.speedy = 0
                        self.state = "parado"
            
            self.rect.x += self.speedx
            
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH - 1
            if self.rect.left < 0:
                self.rect.left = 0
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            for collision in collisions:
                if self.speedx > 0:
                    self.rect.right = collision.rect.left
                elif self.speedx < 0:
                    self.rect.left = collision.rect.right

        def jump(self):
            if self.state == "parado":
                self.speedy -= JUMP_SIZE
                self.state = "pulando"
    def load_assets(img_dir):
        assets = {}
        assets[0] = pygame.image.load('assets/img/personagem_sprite.png').convert_alpha()
        assets[1] = pygame.image.load('assets/img/tile-block.png').convert()
        assets[2] = pygame.image.load('assets/img/tile-wood.png').convert()
        return assets
    assets = load_assets(img_dir)
    jogorodando = True
    clock = pygame.time.Clock()
    FPS = 30
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    player = mable(assets[0], 5, 2, platforms, blocks)
    
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type != 0:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == 1:
                    blocks.add(tile)
                elif tile_type == 2:
                    platforms.add(tile)
    all_sprites.add(player)
    while jogorodando:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                jogorodando = False
                estado = 'cabo'
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
        
        window.fill((0, 0, 0))
        all_sprites.draw(window)
        all_sprites.update()
        pygame.display.flip()
        pygame.display.update() 
 
    pygame.quit() 
    return estado