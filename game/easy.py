import pygame
import sys
import random
import math

pygame.init()

def contains(ball,n,balls_code):
    for i in range (n):
        if(ball==balls_code[i]):
            return 1
    return 0

#draw the balls
balls_code=[]
ball=0
for i in range(4):
    ball = random.randint(0, 5)
    while(contains(ball,i,balls_code)):
        ball=random.randint(0,5)
    balls_code.append(ball)




colours=[]
colours.append('y')
colours.append('r')
colours.append('p')
colours.append('b')
colours.append('g')
colours.append('o')

#save the balls
balls=[]
for i in range(4):
    balls.append(0)
position=[]

#replies
reply_list = []

def check():
    for i in range (4):
        if(colours[balls_code[i]]!=balls[i]):
            return 0
    return 1

def reply():
    black=0
    white=0
    for i in range(4):
        if(balls[i]==colours[balls_code[i]]):
            black=black+1
        else:
            for j in range (4):
                if(balls[i]==colours[balls_code[j]]):
                    white=white+1
    return black,white


def screen_table(screen,n,floor):
    screen.blit(table, (0, 0))
    font = pygame.font.SysFont("dejavusans", 25)
    colourRed = ' - r'
    colourRed_render = font.render(colourRed, 1, (0, 0, 0))
    colourBlue = ' - b'
    colourBlue_render = font.render(colourBlue, 1, (0, 0, 0))
    colourPink = ' - p'
    colourPink_render = font.render(colourPink, 1, (0, 0, 0))
    colourYellow = ' - y'
    colourYellow_render = font.render(colourYellow, 1, (0, 0, 0))
    colourGreen = ' - g'
    colourGreen_render = font.render(colourGreen, 1, (0, 0, 0))
    colourOrange = ' - o'
    colourOrange_render = font.render(colourOrange, 1, (0, 0, 0))
    game_type = 'Poziom: Latwy'
    attempt = 'Ilosc prob: '
    game_type_render = font.render(game_type, 1, (0, 0, 0))
    attempt_render = font.render(attempt, 1, (0, 0, 0))

    # Yellow
    pygame.draw.circle(screen, (255, 255, 10), (75, 580), 15)
    screen.blit(colourYellow_render, (90, 575))
    # Red
    pygame.draw.circle(screen, (255, 0, 0), (145, 580), 15)
    screen.blit(colourRed_render, (160, 575))
    # Pink
    pygame.draw.circle(screen, (204, 0, 102), (215, 580), 15)
    screen.blit(colourPink_render, (230, 575))
    # Blue
    pygame.draw.circle(screen, (0, 15, 117), (285, 580), 15)
    screen.blit(colourBlue_render, (300, 575))
    # Green
    pygame.draw.circle(screen, (0, 153, 0), (355, 580), 15)
    screen.blit(colourGreen_render, (370, 575))
    # Orange
    pygame.draw.circle(screen, (255, 153, 51), (425, 580), 15)
    screen.blit(colourOrange_render, (440, 575))

    h_d = 508
    h_m_1 = 515
    h_m_2 = 500

    for i in range(10):
        pygame.draw.circle(screen, (110, 110, 110), (200, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (275, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (350, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (425, h_d), 14)
        h_d = h_d - 44

        pygame.draw.circle(screen, (110, 110, 110), (87, h_m_1), 5)
        pygame.draw.circle(screen, (110, 110, 110), (67, h_m_1), 5)
        pygame.draw.circle(screen, (110, 110, 110), (67, h_m_2), 5)
        pygame.draw.circle(screen, (110, 110, 110), (87, h_m_2), 5)
        h_m_1 = h_m_1 - 44
        h_m_2 = h_m_2 - 44


    screen.blit(game_type_render, (70, 37))
    screen.blit(attempt_render, (300, 37))
    attempt_number = str(floor)
    attempt_number_render = font.render(attempt_number, 1, (0, 0, 0))
    screen.blit(attempt_number_render, (400, 37))

    for i in range (n):
        if (position[i-3] == 'y'):
            pygame.draw.circle(screen, (255, 255, 10), (position[i-2], position[i-1]), 15)
        if (position[i- 3] == 'r'):
            pygame.draw.circle(screen, (255, 0, 0), (position[i-2], position[i - 1]), 15)
        if (position[i- 3] == 'g'):
            pygame.draw.circle(screen, (0, 153, 0), (position[i-2], position[i - 1]), 15)
        if (position[i- 3] == 'b'):
            pygame.draw.circle(screen, (0, 15, 117), (position[i-2], position[i - 1]), 15)
        if (position[i- 3] == 'p'):
            pygame.draw.circle(screen, (204, 0, 102), (position[i-2], position[i - 1]), 15)
        if (position[i- 3] == 'o'):
            pygame.draw.circle(screen, (255, 153, 51), (position[i-2], position[i - 1]), 15)

    x_check= 67
    y_check= 500
    controll=0
    height=0
    for i in range (floor):
        for j in range(reply_list[2*i]):
            pygame.draw.circle(screen, (0, 0, 0), (x_check, y_check), 6)
            controll = controll + 1
            if (controll == 1):
                x_check = 87
            elif (controll == 2):
                height=1
                y_check = y_check + 17
                x_check = 67
            elif (controll == 3):
                x_check = 87

        for j in range(reply_list[2*i+1]):
            pygame.draw.circle(screen, (255, 255, 255), (x_check, y_check), 6)
            controll = controll + 1
            if (controll == 1):
                x_check = 87
            elif (controll == 2):
                height=1
                y_check = y_check + 17
                x_check = 67
            elif (controll == 3):
                x_check = 87

        if(height==1):
            y_check=y_check-17
        y_check=y_check-44
        x_check=67
        height=0
        controll=0



def start(x_balls,y_balls,n,floor,result):
    font=pygame.font.SysFont("dejavusans",25)
    choice = 0
    end=0
    i=0
    full=0
    reply_current = []
    reply_current.append(0)
    reply_current.append(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                choice = 'y'
                i=i+1
                if(i%4==0):
                    full=1
                x_balls=x_balls+75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n=n+3
                balls[(i%4)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                choice = 'g'
                i=i+1
                if (i % 4 == 0):
                    full = 1
                x_balls = x_balls + 75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%4)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                choice = 'b'
                i=i+1
                if (i % 4 == 0):
                    full = 1
                x_balls = x_balls + 75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%4)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                choice = 'p'
                i=i+1
                if (i % 4 == 0):
                    full = 1
                x_balls = x_balls + 75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%4)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                choice = 'r'
                i=i+1
                if (i % 4 == 0):
                    full = 1
                x_balls=x_balls+75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n=n+3
                balls[(i%4)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                choice = 'o'
                i=i+1
                if (i % 4 == 0):
                    full = 1
                x_balls = x_balls + 75
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%4)-1]=choice


        if(full==1):
            result=check()
            if (result==1):
                import won_game.py
                won_game.fun()
                end=1
            elif(i==40 and result==0):
                import lost_game.py
                lost_game.fun()
                end=1
            else:
                y_balls=508-(math.floor(i/4))*44
                x_balls=125
                floor=floor+1
                reply_current=reply()
                reply_list.append(reply_current[0])
                reply_list.append(reply_current[1])
            full=0


        if(result==0 and i!=40 and end==0):
            screen_table(screen,n,floor)

        pygame.display.flip()


screen = pygame.display.set_mode((520, 620))
table = pygame.image.load('..\graphics\_table_screen.jpg')
screen.blit(table,(0,0))
pygame.display.flip()
# Positions of the balls
y_balls = 508
x_balls = 125
#Number of balls
n=0
#Number of floors
floor=0
result=0
start(x_balls,y_balls,n,floor,result)