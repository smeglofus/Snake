import time
import pygame
from random import randrange
from player_name import *
from scoreboard import Scoreboard, save_score

pygame.init()

clock = pygame.time.Clock()
WEIGHT_OF_FOOD = [10, 10]
SNAKE_LIST = []
LENGHT_OF_SNAKE = 1
SNAKE_SPEED = 25
DYSPLAY_WIDTH = 800
DYSPLAY_HEIGHT = 600
font_style = pygame.font.SysFont(None, 35)
dysplay = pygame.display.set_mode((DYSPLAY_WIDTH, DYSPLAY_HEIGHT))
pygame.display.set_caption("Smeglofův had")
game_over = False

# ouradnice hada
x1 = DYSPLAY_WIDTH / 2
y1 = DYSPLAY_HEIGHT / 2
x1_change = 0
y1_change = 0
FOODX = randrange(0, DYSPLAY_WIDTH - 20)
FOODY = randrange(0, DYSPLAY_HEIGHT - 20)

# ----------------------------------------------------------------------Block of functions

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dysplay.blit(mesg, [DYSPLAY_WIDTH / 2, DYSPLAY_HEIGHT / 2])
def make_had(snake_list):
    for cor in snake_list:
        pygame.draw.rect(dysplay, "green", [cor[0], cor[1], 10, 10])
def write_score(lenght_of_snake):
    score = font_style.render(f"Score: {lenght_of_snake-1}", True, "white")
    dysplay.blit(score, [20,20])
def ask_name():
  app = Player()
  app.mainloop()
def show_scoreboard():
    scoreboard = Scoreboard()
    scoreboard.mainloop()

# pokud se had dostane za hranice okna, nastává konec hry
def colision_with_wall():
    global  game_over
    if x1 >= DYSPLAY_WIDTH or x1 < 0 or y1 >= DYSPLAY_HEIGHT or y1 < 0:
        save_score(LENGHT_OF_SNAKE,message)
        game_over = True
def eat_and_grow(x,y):
    global LENGHT_OF_SNAKE,FOODX,FOODY
    pygame.draw.rect(dysplay, "red", [x, y, 10, 10])
    if x1 in range(x-10, x+10) and y1 in range(y-10, y+10):
        FOODX = randrange(0, DYSPLAY_WIDTH - 20)
        FOODY = randrange(0, DYSPLAY_HEIGHT - 20)
        LENGHT_OF_SNAKE += 1
    grow()
def move():
    # souradnice hada
    global x1,y1,x1_change,y1_change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    colision_with_wall()
    x1 += x1_change
    y1 += y1_change
    dysplay.fill("black")
def grow():
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    SNAKE_LIST.append(snake_head)
    if len(SNAKE_LIST) > LENGHT_OF_SNAKE:
        del SNAKE_LIST[0]
    make_had(SNAKE_LIST)
# ------------------------------------------------------------------------------------

#ask_name()

while not game_over:
    move()
    eat_and_grow(FOODX,FOODY)
    write_score(LENGHT_OF_SNAKE)
    pygame.display.update()
    clock.tick(SNAKE_SPEED)

message("Konec hry","red")
pygame.display.update()
time.sleep(1)

#show_scoreboard()

pygame.quit()
quit()