import time
import pygame
from random import randrange
import datetime


dysplay_width = 800
dysplay_height = 600

pygame.init()
dysplay = pygame.display.set_mode((dysplay_width,dysplay_height))
pygame.display.set_caption("Smeglofův had")
game_over = False


snake_list = []
lenght_of_snake = 1
#souradnice hada
x1 = dysplay_width/2
y1 = dysplay_height/2

x1_change = 0
y1_change = 0



#souradnice jídla
foodx = randrange(0, dysplay_width - 20)
foody = randrange(0, dysplay_height - 20)


snake_speed = 25
font_style = pygame.font.SysFont(None,50)
clock = pygame.time.Clock()
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dysplay.blit(mesg, [dysplay_width/2, dysplay_height/2])
def had(snake_list):
    for cor in snake_list:
        pygame.draw.rect(dysplay, "green", [cor[0],cor[1], 10, 10])
def score(lenght_of_snake):
    score = font_style.render(f"Score: {lenght_of_snake-1}", True, "white")
    dysplay.blit(score, [20,20])

jmeno = input("Zadej své jméno, dáme to pak do tabulky vítězů.: ")
while not game_over:
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
    if x1 >= dysplay_width or x1 < 0 or y1 >= dysplay_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dysplay.fill("black")

    if x1 in range(foodx-10, foodx+10) and y1 in range(foody-10, foody+10):
        foodx = randrange(0, dysplay_width - 20)
        foody = randrange(0, dysplay_height - 20)
        lenght_of_snake += 1
    pygame.draw.rect(dysplay, "red", [foodx, foody, 10, 10])
    print(lenght_of_snake)
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > lenght_of_snake:
        del snake_list[0]
    print(snake_list)
    had(snake_list)
    score(lenght_of_snake)

    pygame.display.update()
    clock.tick(snake_speed)
    print(snake_head)

#zjistí datum a napíše do tabulky jméno, čas a body
now = datetime.datetime.now().strftime("%m/%d/%Y")

message("Konec hry","red")
with open('score.txt', 'a') as f:
    f.write(f"{jmeno},{lenght_of_snake-1},{now} \n")

pygame.display.update()
time.sleep(2)

pygame.quit()
quit()