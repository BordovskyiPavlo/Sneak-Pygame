import pygame , random
from pygame.locals import *
pygame.init()
col , row ,size = 16 , 16 ,50
time = 3
gamescreen = pygame.display.set_mode((col*size,row*size))
pygame.display.set_caption("Hello Sneak")
clock = pygame.time.Clock()
background = pygame.Surface((col*size,row*size))
background.fill((255,255,255))
for i in range (1, col):
    pygame.draw.line(background,(128,128,128),(i*size-1,0),(i*size-1,row*size),2)
for i in range (1, row):
    pygame.draw.line(background,(128,128,128),(0,i*size-1),(col*size,i*size-1),2)
def random_position(body):
    while True:
        position = random.randrange(col),random.randrange(row)
        if position not in body:
            break
    return  position
body = [(col//2, row//2)]
step = (1,0)
length = 1
food = random_position(body)
time = 3
online = True
def game_over(body):
    for i in range(1,length):
        if body[0] == body[i]:
            pygame.quit()
while online:
    clock.tick(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            online = False
        if event.type == pygame.KEYDOWN:
            permission = {"a": True, "d": True, "w": True, "s": True}
            if event.key == pygame.K_a and permission["a"]:
                permission = {"a": True, "d": False, "w": True, "s": True}
                step = (-1, 0)
            if event.key == pygame.K_d and permission["d"]:
                permission = {"a": False, "d": True, "w": True, "s": True}
                step = (1, 0)
            if event.key == pygame.K_w and permission["w"]:
                permission = {"a": True, "d": True, "w": True, "s": False}
                step = (0, -1)
            if event.key == pygame.K_s and permission["s"]:
                permission = {"a": True, "d": True, "w": False, "s": True}
                step = (0, 1)
    body.insert(0,body[0][:])
    body[0] = (body[0][0] + step[0]) % col, (body[0][1] + step[1]) % row
    if body[0] == food:
        food = random_position(body)
        length+= 1
        time+= 0.5
    while len(body) > length:
        del body[-1]
        gamescreen.blit(background,(0,0))
        pygame.draw.rect(gamescreen,(255,0,255), (food[0]*size, food[1]*size,size ,size))
        for i, pos in enumerate(body):
            color = (255, 0, 0) if i == 0 else (0, 192, 0) if (i % 2) == 0 else (255, 128, 0)
            pygame.draw.rect(gamescreen, color, (pos[0] * size, pos[1] * size, size, size))
        game_over(body)
        pygame.display.flip()