import pygame
import os

pygame.init()

width, height = (500, 900)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rising Lava")

FPS = 60
velocity = 3
gravity = 1
jumpHeight = 20
white = (255,255,255)
sky = (51,215,255)
cloud_image = pygame.image.load(os.path.join("cloud.png"))
cloud = pygame.transform.scale(cloud_image, (150,100))
start_stone_platform_position = (170,600)
start_stone_platform_image = pygame.image.load(os.path.join("stone_platform.png"))
start_stone_platform = pygame.transform.scale(start_stone_platform_image, (150,100))
lava_position = (-50,720)
lava_image = pygame.image.load(os.path.join("lava.png"))
lava = pygame.transform.scale(lava_image, (600,300))
plr_position = (225,580)
plr_image = pygame.image.load(os.path.join("player.png"))
plr_image_scaled = pygame.transform.scale(plr_image, (40,80))

def basic_background():
    screen.fill(sky)
    screen.blit(cloud, (100,100))
    screen.blit(start_stone_platform, start_stone_platform_position)
    screen.blit(lava, lava_position)
    pygame.display.update()

class player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.dir = "right"
        self.x_vel = 0
        self.y_vel = 0
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, velocity):
        self.x_vel = -velocity
        if self.dir != "left":
            self.dir = "left"
            self.animation_count = 0
    
    def move_right(self, velocity):
        self.x_vel = velocity
        if self.dir != "right":
            self.dir = "right"
            self.animation_count = 0

    def loop(self, fps, player, plr, screen):
        self.move(self.x_vel, self.y_vel)
        screen.blit(plr, (player.x, player.y))

def moveHandler(player):
    keys = pygame.key.getPressed()
    player.x_vel = 0
    if keys[pygame.K_A]:
        player.move_left(velocity)
    if keys[pygame.K_D]:
        player.move_left(velocity)


def main():
    plr = player(225, 580, 40, 80)
    clock = pygame.time.Clock()
    spacePressed = False
    global velocity
    global plr_image_scaled
    global screen
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        player.loop(FPS, plr, plr_image_scaled, screen)
        moveHandler(plr)
        basic_background()

if __name__ == "__main__":
    main()