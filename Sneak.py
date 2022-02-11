import pygame , random
from pygame.locals import *
pygame.init()
col ,row ,size = 15 , 15 ,40
time = 3

#screen
gamescreen = pygame.display.set_mode((col*size,row*size+25))
background = pygame.Surface((col*size,row*size))
background.fill((255,255,255))

pygame.display.set_caption("Hello Sneak")
clock = pygame.time.Clock()
online = True
gameover = False
White = (255,255,255)
Black = (0,0,0)
onlineupdate = True
#direction
LEFT,RIGHT,UP,DOWN = 1,2,3,4
direction = RIGHT
update = direction

score=1
body = [(col//2, row//2)]
step = (1,0)
length = 1

#Score
font = pygame.font.SysFont(None, 25)
text = font.render("Score: " + str(length), True, White)
gamescreen.blit(text, (5, 600))

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

def spawn_food(body):
    global food
    food = random_position(body)
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
    font = pygame.font.SysFont(None, 25)
    if body[0] == food:
        text = font.render("Score: " + str(length), True, Black)
        gamescreen.blit(text, (5, 600))
        spawn_food(body)
        length += 1
        time += 0.5
    if score != length:
        score +=1
        text = font.render("Score: " + str(length), True, White)
        gamescreen.blit(text, (5, 600))
    gamescreen.blit(text, (5, 600))
    pygame.display.update()
    control_length(body)