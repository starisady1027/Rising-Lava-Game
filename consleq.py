import pygame
import os

width, height = (500, 900)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rising Lava")

FPS = 60
white = (255,255,255)
sky = (51,215,255)
cloud_image = pygame.image.load(os.path.join("cloud.png"))
cloud = pygame.transform.scale(cloud_image, (150,100))
stone_platform_position = (200,300)
stone_platform_image = pygame.image.load(os.path.join("stone_platform.png"))
stone_platform = pygame.transform.scale(stone_platform_image, (150,100))
lava_position = (200,600)
lava_image = pygame.image.load(os.path.join("lava.png"))
lava = pygame.transform.scale(lava_image, (500,300))

def draw_screen():
    screen.fill(sky)
    screen.blit(cloud, (100,100))
    screen.blit(stone_platform, stone_platform_position)
    screen.blit(lava, lava_position)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_screen()
main()