import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos+576, 900))


pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

background_surface = pygame.image.load('Assets/images/background-day.png').convert()
background_surface = pygame.transform.scale2x(background_surface)

floor_surface = pygame.image.load('Assets/images/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_surface, (0,0))
    floor_x_pos -=1
    draw_floor()
    if(floor_x_pos<=-576):
        floor_x_pos=0
    

    pygame.display.update()
    clock.tick(120)