import pygame
from config import *
from physics import altura_minima

def pantalla1(screen):
    running = True
    clock = pygame.time.Clock()
    x = 50

    while running:
        screen.fill(WHITE)

        # Dibujar pista (simple)
        pygame.draw.line(screen, BLACK, (50, 400), (300, 400), 5)
        pygame.draw.circle(screen, BLACK, (400, 350), 100, 5)

        # Carrito (animación simple)
        pygame.draw.circle(screen, RED, (x, 380), 10)
        x += 2
        if x > WIDTH:
            x = 50

        # Texto
        font = pygame.font.SysFont(None, 28)

        h_min = altura_minima(R)

        text1 = font.render(f"Altura: {H_CORRECTA:.2f} m", True, BLACK)
        text2 = font.render(f"Radio: {R:.2f} m", True, BLACK)
        text3 = font.render(f"Altura mínima: {h_min:.2f} m", True, BLACK)
        text4 = font.render("El carrito completa el loop", True, GREEN)

        screen.blit(text1, (20, 20))
        screen.blit(text2, (20, 50))
        screen.blit(text3, (20, 80))
        screen.blit(text4, (20, 110))

        # Evento salir o cambiar pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "pantalla2"

        pygame.display.flip()
        clock.tick(60)