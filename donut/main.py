import pygame
import math

pygame.init()

green = (0, 255, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 1000

x_start, y_start = 0, 0

x_seperator = 10
y_seperator = 20

rows = HEIGHT // y_seperator
columns = WIDTH // x_seperator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
#display_surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
font = pygame.font.SysFont('Arial', 18, bold=True)


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, green)
    screen.blit(text, (x_start, y_start))
    display_surface.blit(text, (x_start, y_start))

run = True
while run:

    screen.fill((black))

    z = [0] * screen_size
    b = [' '] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_seperator - y_seperator:
        y_start = 0

    for i in range(len(b)):
        A += 0.000002
        B += 0.000001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_seperator
        else:
            y_start += y_seperator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_seperator

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
