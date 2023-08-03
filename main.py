import pygame
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 64)
running = True

number = 1

def draw_background():
    screen.fill("black")
    #Putting circle here too I guess?
    pygame.draw.circle(screen, "white", (640, 360), 310, width=3)
    pygame.draw.line(screen, "white", (640, 50), (640, 670), width=3)
    pygame.draw.line(screen, "white", (330, 360), (950, 360), width=3)
    return

def draw_number():
    global number
    coords = [(640+155, 360-155), (640+155, 360+155), (640-155, 360+155), (640-155, 360-155)]
    font.render_to(screen, coords[number-1], str(number), "white")
    return

def update_number():
    global number
    if number < 4:
        number += 1
    else:
        number = 1
    return

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_background()
    draw_number()
    update_number()

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
