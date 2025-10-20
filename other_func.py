import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def create_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen