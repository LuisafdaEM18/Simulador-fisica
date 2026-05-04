import pygame
from config import *
from physics import cumple_loop

def pantalla2(screen):
    running = True
    clock = pygame.time.Clock()

    input_text = ""
    resultado = ""

    while running:
        screen.fill(WHITE)

        font = pygame.font.SysFont(None, 32)

        texto = font.render("Ingresa altura (m): " + input_text, True, BLACK)
        screen.blit(texto, (50, 100))

        resultado_texto = font.render(resultado, True, BLUE)
        screen.blit(resultado_texto, (50, 200))

        instrucciones = font.render("Enter = probar | ESC = volver", True, BLACK)
        screen.blit(instrucciones, (50, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        h = float(input_text)
                        if cumple_loop(h, R):
                            resultado = "Funciona: completa el loop"
                        else:
                            resultado = "No funciona: falta altura"
                    except:
                        resultado = "Entrada inválida"

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                elif event.key == pygame.K_ESCAPE:
                    return "pantalla1"

                else:
                    input_text += event.unicode

        pygame.display.flip()
        clock.tick(60)