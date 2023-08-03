import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

number = 1

def draw_background():
    # DRAW BACKGROUND CODE HERE
    return

def draw_number():
    global number
    # DRAW NUMBER CODE HERE
    return

def update_number():
    global number
    # UPDATE NUMBER CODE HERE
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
