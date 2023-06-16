import pygame
import os
import random
from threading import Thread

pygame.init()

WIDTH, HEIGHT = (500, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rising Lava")


CLONELIST = []
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
START_PLR_Y = 600
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
        self.newRect = pygame.Rect(random.randint(100,300), random.randint(360,400), width, height)

    def draw(self):
        CLONELIST.append(self.rect)
    
    def drawNew(self):
        CLONELIST.append(self.newRect)

        



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

    def loop(self, player, plr,):
        self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.move(self.x_vel, self.y_vel)
        SCREEN.blit(plr, (player.rect.x, player.rect.y))
        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.fall_count = 0
        self.y_vel *= -1

def vertical_collision(player, dy):
    for sto in CLONELIST:
        if player.rect.colliderect(sto):
            if dy > 0:
                player.rect.bottom = sto.top
                player.landed()
            elif dy < 0:
                player.rect.top = sto.bottom
                player.hit_head()

def horizontal_collision(player, dx):
    player.move(dx, 0)
    player.update()
    collided_object = []
    for obj in CLONELIST:
        if player.rect.colliderect(obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def moveHandler(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    collide_left = horizontal_collision(player, -VELOCITY)
    collide_right = horizontal_collision(player, VELOCITY)
    if keys[pygame.K_a] and player.rect.x > 0 and not collide_left:
        player.move_left(VELOCITY)
    if keys[pygame.K_d] and player.rect.x + player.rect.width < WIDTH and not collide_right:
        player.move_right(VELOCITY)

    vertical_collision(player, player.y_vel)

def drawClone():
    clone = pygame.Rect(random.randint(100,300), 150, 150, 30)
    CLONELIST.append(clone)


def Draw(player, stone):
    basic_background()
    stone.draw()
    stone.drawNew()
    for sto in CLONELIST:
        pygame.draw.rect(SCREEN, GRAY, sto)
    global plr_image_scaled
    player.loop(player, plr_image_scaled)
    pygame.display.update()




def main():
    plr = player(START_PLR_X, START_PLR_Y, 40, 80)
    Stone = stone(START_STONE_X, START_STONE_Y, 150, 30)
    clock = pygame.time.Clock()
    counter = 0
    run = False
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and plr.jump_count < 1:
                    plr.jump()
        moveHandler(plr)
        Draw(plr, Stone)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d]:
            run = True
        if run:
            counter += 1
            if counter > 100:
                drawClone()
                counter = 0
            for sto in CLONELIST:
                sto.y += 2



if __name__ == "__main__":
    main()