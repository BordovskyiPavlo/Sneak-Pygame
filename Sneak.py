import pygame , random
from pygame.locals import *
pygame.init()
col ,row ,size = 15 , 15 ,40
time = 3

#screen
gamescreen = pygame.display.set_mode((col*size,row*size))
background = pygame.Surface((col*size,row*size))
background.fill((255,255,255))

pygame.display.set_caption("Hello Sneak")
clock = pygame.time.Clock()
online = True
gameover = False
Black = (0,0,0)

#direction
LEFT,RIGHT,UP,DOWN = 1,2,3,4
direction = RIGHT
update = direction

body = [(col//2, row//2)]
step = (1,0)
length = 1
score = length
for i in range (1, col):
    pygame.draw.line(background,(128,128,128),(i*size-1,0),(i*size-1,row*size),2)
for i in range (1, row):
    pygame.draw.line(background,(128,128,128),(0,i*size-1),(col*size,i*size-1),2)

def random_position(body):
    while True:
        position = random.randrange(col),random.randrange(row)
        if position not in body:
            break
    return position
food = random_position(body)
def eat_food(length,time):
    length += 1
    time += 0.5

def spawn_food(body):
    global food
    food = random_position(body)

def score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, Black)
    gamescreen.blit(text, (15, 15))
def game_over(body):
    for i in range(1,length):
        if body[0] == body[i]:
            pygame.quit()

def control_length(body):
    while len(body) > length:
        del body[-1]
        gamescreen.blit(background,(0,0))
        pygame.draw.rect(gamescreen,(255,0,255), (food[0]*size, food[1]*size,size ,size))
        for i, pos in enumerate(body):
            color = (255, 0, 0) if i == 0 else (0, 192, 0) if (i % 2) == 0 else (255, 128, 0)
            pygame.draw.rect(gamescreen, color, (pos[0] * size, pos[1] * size, size, size))
        game_over(body)
        pygame.display.flip()
while online:
    clock.tick(time)
    score(length)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            online = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_a:
                update = LEFT
            elif event.key == pygame.K_d:
                update = RIGHT
            elif event.key == pygame.K_w:
                update = UP
            elif event.key == pygame.K_s:
                update = DOWN
            if update == LEFT and direction != RIGHT:
                direction = LEFT
            if update == RIGHT and direction != LEFT:
                direction = RIGHT
            if update == UP and direction != DOWN:
                direction = UP
            if update == DOWN and direction != UP:
                direction = DOWN
            if direction == LEFT:
                step = (-1, 0)
            if direction == RIGHT:
                step = (1, 0)
            if direction == UP:
                step = (0, -1)
            if direction == DOWN:
                step = (0, 1)
    body.insert(0, body[0][:])
    body[0] = (body[0][0] + step[0]), (body[0][1] + step[1])
    pygame.display.update()
    if body[0] == food:
        food = random_position(body)
        length += 1
        time += 0.5
        pygame.display.update()
    control_length(body)