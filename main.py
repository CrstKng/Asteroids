# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print(pygame.get_init())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)

    fps_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill(color)
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        fps_clock.tick(60)
        dt += fps_clock.tick(60) / 1000
        print(player.position)
        print(player.rotation)
        pygame.display.flip()



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
