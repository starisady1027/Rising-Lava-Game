import pygame
import os

width, height = (500, 900)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rising Lava")

FPS = 60
velocity = 5
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
plr = pygame.transform.scale(plr_image, (40,80))

def basic_background(player):
    screen.fill(sky)
    screen.blit(cloud, (100,100))
    screen.blit(start_stone_platform, start_stone_platform_position)
    screen.blit(lava, lava_position)
    screen.blit(plr, (player.x, player.y))
    pygame.display.update()

def playerHandler(keyPressed, player):
    if keyPressed[pygame.K_a]:
        player.x -= velocity
    if keyPressed[pygame.K_d]:
        player.x += velocity
    


def main():
    player = pygame.Rect(225, 580, 40, 80)
    clock = pygame.time.Clock()
    spacePressed = False
    velocity = 5
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_SPACE]:
            spacePressed = True
        if spacePressed:
            player.y -= velocity
            velocity -= gravity
            if velocity < -jumpHeight:
                spacePressed = False
                velocity = jumpHeight
        playerHandler(keyPressed, player)
        basic_background(player)
main()