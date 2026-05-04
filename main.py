import pygame
from config import *
from screens.screen1 import pantalla1
from screens.screen2 import pantalla2

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador Montaña Rusa")

pantalla_actual = "pantalla1"

while True:
    if pantalla_actual == "pantalla1":
        pantalla_actual = pantalla1(screen)

    elif pantalla_actual == "pantalla2":
        pantalla_actual = pantalla2(screen)

    elif pantalla_actual == "quit":
        break

pygame.quit()