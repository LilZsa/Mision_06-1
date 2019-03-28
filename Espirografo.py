# Autor: Roberto Emmanuel González Muñoz
# Dibuja la curva generada por un espirógrafo. Los valores
# de r, R y l, se leen en la función main y los manda como parámetros a la función dibujar.

import random
import math
import pygame   # Librería de pygame


# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)





# Estructura básica de un programa que usa pygame para dibujar

def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


        # Borrar pantalla
        ventana.fill(BLANCO)


        # Dibujar, aquí haces todos los trazos que requieras
        k = r / R
        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, AZUL, (x + ANCHO // 2, ALTO // 2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) + l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((2 - k) * math.cos(a) + l * k * math.cos(((2 - k) / k) * a))))
            y = int(R * (((2 - k) * math.sin(a) + l * k * math.sin(((2 - k) / k) * a))))
            pygame.draw.circle(ventana, NEGRO, (x + ANCHO // 2, ALTO // 2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((2 - k) * math.cos(a) + l * k * math.cos(((2 - k) / k) * a))))
            y = int(R * (((2 - k) * math.sin(a) - l * k * math.sin(((2 - k) / k) * a))))
            pygame.draw.circle(ventana, VERDE_BANDERA, (x + ANCHO // 2, ALTO // 2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) + l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, AZUL, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, BLANCO, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k*2 * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k*2 * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, NEGRO, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k*2 * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k*2 * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, AZUL, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R*2 * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, BLANCO, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R*2 * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 - y), 1)

        for angulo in range(0, 360 * r // math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R*2 * (((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a))))
            y = int(R*2 * (((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a))))
            pygame.draw.circle(ventana, NEGRO, (x + ANCHO//2, ALTO//2 - y), 1)

        for radio in range(10, ALTO // 2, 10):
            pygame.draw.circle(ventana, AZUL, ((ANCHO//2), (ALTO//2)), radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps



    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    radio1 = int(input("Valor del radio interior: "))
    radio2 = int(input("Valor del radio exterior: "))
    ele = float(input("Valor de l: "))
    dibujar(radio1, radio2, ele)


# Llamas a la función principal
main()


