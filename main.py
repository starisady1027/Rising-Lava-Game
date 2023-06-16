import pygame
import os
import random

pygame.init()

WIDTH, HEIGHT = (500, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rising Lava")

FPS = 60
VELOCITY = 5
GRAVITY = 1
GRAY = (129, 134, 135)
jumpHeight = 20
white = (255,255,255)
sky = (51,215,255)
cloud_image = pygame.image.load(os.path.join("cloud.png"))
cloud = pygame.transform.scale(cloud_image, (150,100))
START_STONE_X = 170
START_STONE_Y = 600
start_stone_platform_image = pygame.image.load(os.path.join("stone_platform.png"))
start_stone_platform = pygame.transform.scale(start_stone_platform_image, (150,100))
lava_position = (-50,720)
lava_image = pygame.image.load(os.path.join("lava.png"))
lava = pygame.transform.scale(lava_image, (600,300))
START_PLR_X = 225
START_PLR_Y = 580
plr_image = pygame.image.load(os.path.join("player.png"))
plr_image_scaled = pygame.transform.scale(plr_image, (40,80))

def basic_background():
    SCREEN.fill(sky)
    SCREEN.blit(cloud, (100,100))
    SCREEN.blit(cloud, (250,300))
    SCREEN.blit(lava, lava_position)


class stone():
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.newRect = pygame.Rect(random.randint(100,240), random.randint(350,400), width, height)

    def draw(self, offset_y):
        self.rect.y -= offset_y
        pygame.draw.rect(SCREEN, GRAY, self.rect)
    
    def drawNew(self, offset_y):
        self.newRect.y -= offset_y
        pygame.draw.rect(SCREEN, GRAY, self.newRect)



class player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.fall_count = 0
        self.jump_count = 0

    def jump(self):
        self.y_vel = -GRAVITY * 10
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, velocity):
        self.x_vel = -velocity
    
    def move_right(self, velocity):
        self.x_vel = velocity

    def loop(self, player, plr, offset_y):
        self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.move(self.x_vel, self.y_vel)
        SCREEN.blit(plr, (player.rect.x, player.rect.y + offset_y))
        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.fall_count = 0
        self.y_vel *= -1

def collision(player, stone, dy):
    stones = [stone.rect, stone.newRect]
    for sto in stones:
        if player.rect.colliderect(sto):
            if dy > 0:
                player.rect.bottom = sto.top
                player.landed()
            elif dy < 0:
                player.rect.top = sto.bottom
                player.hit_head()


def moveHandler(player, stone):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    if keys[pygame.K_a] and player.rect.x > 0:
        player.move_left(VELOCITY)
    if keys[pygame.K_d] and player.rect.x + player.rect.width < WIDTH:
        player.move_right(VELOCITY)

    collision(player, stone, player.y_vel)

def Draw(player, stone, offset_y):
    basic_background()
    stone.draw(offset_y)
    stone.drawNew(offset_y)
    global plr_image_scaled
    player.loop(player, plr_image_scaled, offset_y)
    pygame.display.update()



def main():
    plr = player(START_PLR_X, START_PLR_Y, 40, 80)
    Stone = stone(START_STONE_X, START_STONE_Y, 150, 30)
    clock = pygame.time.Clock()
    offset_y = 0
    scroll_height = 200

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and plr.jump_count < 1:
                    plr.jump()
        Draw(plr, Stone, offset_y)
        moveHandler(plr, Stone)
        print(offset_y)
        if ((plr.rect.top - offset_y <= scroll_height) and plr.y_vel < 0):
            offset_y -= plr.y_vel

if __name__ == "__main__":
    main()