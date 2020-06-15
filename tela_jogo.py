import pygame
from time import time
from os import path
#importa as imagens
img_dir = path.join(path.dirname(__file__), 'img')
#define algumas variaveis pricipais
TITULO = 'Semeru'
WIDTH = 1000
HEIGHT = 560
TILE_SIZE = 40 
PLAYER_WIDTH = TILE_SIZE-5
PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
FPS = 60 
PLAYER_IMG = 'player_img'
GRAVITY = 5
JUMP_SIZE = TILE_SIZE

SPEED_X = 10
#define os tipos de tiles do jogo
BLOCK = 0
STAR = 1
LAVA = 2
EMPTY = -1

MAP1 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, STAR, EMPTY],
    [BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]
MAP2 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, STAR, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]
MAP3 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, STAR, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]
STILL = 0
JUMPING = 1
FALLING = 2

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):
        pygame.sprite.Sprite.__init__(self)
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        self.image = tile_img
        self.rect = self.image.get_rect()
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, row, column, platforms, blocks, lava):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL

        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.platforms = platforms
        self.blocks = blocks
        self.lava = lava
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0
        self.highest_y = self.rect.bottom
        self.fase1 = False
        self.fase2 = False
        self.fase3 = False
        self.vivo = True
    def update(self):
        self.speedy += GRAVITY
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.state != FALLING:
            self.highest_y = self.rect.bottom
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = STILL
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = 0
                self.state = STILL
        if self.speedy > 0:
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            for platform in collisions:
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.highest_y = self.rect.bottom
                    self.speedy = 0
                    self.state = STILL
                    self.fase1 = True
                    if state == 'game2':
                        self.fase2 = True
                    if state == 'game3':
                        self.fase3 = True
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
        collisions = pygame.sprite.spritecollide(self, self.lava, False)
        for collision in collisions:
            if self.speedx or self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.vivo = False
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'madeline.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'grama.png')).convert()
    assets[STAR] = pygame.image.load(path.join(img_dir, 'estrela.jpg')).convert_alpha()
    assets[LAVA] = pygame.image.load(path.join(img_dir,'lava.png')).convert()
    assets['BACKGROUND_IMG'] = pygame.image.load(path.join(img_dir, 'FUNDO MONTANHAS.png')).convert()
    return assets


def game_screen1(screen):
    clock = pygame.time.Clock()
    assets = load_assets(img_dir)
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    lava = pygame.sprite.Group()
    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks, lava)
    for row in range(len(MAP1)):
        for column in range(len(MAP1[row])):
            tile_type = MAP1[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == BLOCK:
                    blocks.add(tile)
                elif tile_type == STAR:
                    platforms.add(tile)
                elif tile_type == LAVA:
                    lava.add(tile)
    all_sprites.add(player)
    game = True
    while game :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                state = 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
            if player.vivo == False:
                pygame.quit()
                state = 'quit'
            if player.fase1 == True:
                state = 'game2'
        all_sprites.update()
        screen.blit(assets['BACKGROUND_IMG'], (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    return state
def game_screen2(screen):
    clock = pygame.time.Clock()
    assets = load_assets(img_dir)
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    lava = pygame.sprite.Group()
    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks, lava)
    for row in range(len(MAP2)):
        for column in range(len(MAP2[row])):
            tile_type = MAP2[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == BLOCK:
                    blocks.add(tile)
                elif tile_type == STAR:
                    platforms.add(tile)
                elif tile_type == LAVA:
                    lava.add(tile)
    all_sprites.add(player)
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'quit'
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
            if player.vivo == False:
                pygame.quit()
                state = 'quit'
            if player.fase2 == True:
                state = 'game3'
        all_sprites.update()
        screen.blit(assets['BACKGROUND_IMG'], (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    return state
def game_screen3(screen):
    clock = pygame.time.Clock()
    assets = load_assets(img_dir)
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    lava = pygame.sprite.Group()
    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks, lava)
    for row in range(len(MAP3)):
        for column in range(len(MAP3[row])):
            tile_type = MAP3[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == BLOCK:
                    blocks.add(tile)
                elif tile_type == STAR:
                    platforms.add(tile)
                elif tile_type == LAVA:
                    lava.add(tile)
    all_sprites.add(player)
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'quit'
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
            if player.vivo == False:
                pygame.quit()
                state = 'quit'
            if player.fase3 == True:
                state = 'final'
        all_sprites.update()
        screen.blit(assets['BACKGROUND_IMG'], (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    return state    
def menu(window):
    WIDTH = 1000
    HEIGHT = 520
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    rodando = True
    image = pygame.image.load('img/imagem_menu.png').convert()
    font = pygame.font.SysFont(None, 100)
    text = font.render('Semeru', True, (0, 0, 0))
    font = pygame.font.SysFont(None, 30)
    text2 = font.render('Aperte qualquer tecla para continuar', True, (0,0,0))
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'quit'
                rodando = False
            if event.type == pygame.KEYUP:
                state = 'game1'
                rodando = False

        window.blit(image, (0, 0))
        window.blit(text, (150, 100))
        window.blit(text2, (250, 300))
        pygame.display.update() 

    return state
def final(window):
    WIDTH = 1000
    HEIGHT = 520
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    rodando = True
    imagefinal = pygame.image.load('img/MAPA SEMERU 3 PARTE 4.png').convert()
    font = pygame.font.SysFont(None, 100)
    text = font.render('Semeru', True, (0, 0, 0))
    font = pygame.font.SysFont(None, 30)
    text2 = font.render('Parabéns! Você ganhou', True, (0,0,0))
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'quit'
                rodando = False
        window.blit(imagefinal, (0, 0))
        window.blit(text, (150, 100))
        window.blit(text2, (250, 300))
        pygame.display.update() 

    return state
 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITULO)
state = 'menu'
while state != 'quit':
    if state == 'menu':
        state = menu(screen)
    elif state == 'game1':
        state = game_screen1(screen)
    elif state == 'game2':
        state = game_screen2(screen)
    elif state == 'game3':
        state = game_screen3(screen)
    elif state == 'final':
        state = final(screen)
    else:
        state = 'quit'
pygame.quit()