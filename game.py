import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos+576, 900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0

background_surface = pygame.image.load('Assets/images/background-day.png').convert()
background_surface = pygame.transform.scale2x(background_surface)

floor_surface = pygame.image.load('Assets/images/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('Assets/images/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('Assets/images/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [400, 600, 800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement=0
                bird_movement-=12
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())



    screen.blit(background_surface, (0,0))

    bird_movement+=gravity
    bird_rect.centery+=bird_movement
    screen.blit(bird_surface, bird_rect)

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    floor_x_pos -=1
    draw_floor()
    if(floor_x_pos<=-576):
        floor_x_pos=0
    

    pygame.display.update()
    clock.tick(120)