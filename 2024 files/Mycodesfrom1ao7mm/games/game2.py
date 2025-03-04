import pygame
import sys

# Definição de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 40
PACMAN_COLOR = (255, 255, 0)
GHOST_COLOR = (255, 0, 0)
WALL_COLOR = (0, 0, 255)
GRID_COLOR = (255, 255, 255)

# Definição do labirinto
MAZE = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W............WW...........W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW",
    "WoWWWW.WWWWW.WW.WWWWW.WWWtW",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW",
    "W........................W",
    "W.WW.WWWWWWWWWWWWWWW.WW.WW",
    "W.WW.WW..............WW.WW",
    "W......WW.WWGGWW.WW.W.....W",
    "WWWWWW.WW.WWWWW.WW.W.WWWWWW",
    "WWWWWW.WW.WWWWW.WW.W.WWWWWW",
    "WWWWWW.WW........WW.W.WWWWWW",
    "WWWWWW.WW.WWWWW.WW.W.WWWWWW",
    "WWWWWW.WW.WWWWW.WW.W.WWWWWW",
    "W............WW...........W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW",
    "Wo..W.......P..P.......W..W",
    "WWW.W.WWWWWWWWWWWWWW.W.WWWW",
    "W......WW.WWGGWW.WW......W",
    "W.WWWWWWW.WWWWW.WWWWWWWW.W",
    "W.WWWWWWW.WWWWW.WWWWWWWW.W",
    "W........................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Classe do Pac-Man
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(PACMAN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Classe do Fantasma
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(GHOST_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, target):
        dx = target[0] - self.rect.x
        dy = target[1] - self.rect.y
        if abs(dx) > abs(dy):
            if dx > 0:
                self.rect.x += GRID_SIZE
            else:
                self.rect.x -= GRID_SIZE
        else:
            if dy > 0:
                self.rect.y += GRID_SIZE
            else:
                self.rect.y -= GRID_SIZE

# Função para desenhar o labirinto
def draw_maze(screen):
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            if cell == "W":
                pygame.draw.rect(screen, WALL_COLOR, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            else:
                pygame.draw.rect(screen, GRID_COLOR, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pac-Man")

    pacman = Pacman(1 * GRID_SIZE, 1 * GRID_SIZE)
    ghost = Ghost(10 * GRID_SIZE, 10 * GRID_SIZE)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(pacman)
    all_sprites.add(ghost)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.move(-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT]:
            pacman.move(GRID_SIZE, 0)
        if keys[pygame.K_UP]:
            pacman.move(0, -GRID_SIZE)
        if keys[pygame.K_DOWN]:
            pacman.move(0, GRID_SIZE)

        # Atualiza o movimento do fantasma em direção ao Pac-Man
        ghost.update((pacman.rect.x, pacman.rect.y))

        screen.fill((0, 0, 0))
        draw_maze(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()