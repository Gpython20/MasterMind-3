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
for i in range(6):
    ball = random.randint(0, 7)
    while(contains(ball,i,balls_code)):
        ball=random.randint(0,7)
    balls_code.append(ball)




colours=[]
colours.append('y')
colours.append('r')
colours.append('p')
colours.append('b')
colours.append('g')
colours.append('o')
colours.append('t')
colours.append('l')

#save the balls
balls=[]
for i in range(6):
    balls.append(0)
position=[]

#replies
reply_list = []

def check():
    for i in range (6):
        if(colours[balls_code[i]]!=balls[i]):
            return 0
    return 1

def reply():
    black=0
    white=0
    for i in range(6):
        if(balls[i]==colours[balls_code[i]]):
            black=black+1
        else:
            for j in range (6):
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
    colourLilac = ' - l'
    colourLilac_render = font.render(colourLilac, 1, (0, 0, 0))
    colourTurquoise = ' - t'
    colourTurquoise_render = font.render(colourTurquoise, 1, (0, 0, 0))
    game_type = 'Poziom: Trudny'
    attempt = 'Ilosc prob: '
    game_type_render = font.render(game_type, 1, (0, 0, 0))
    attempt_render = font.render(attempt, 1, (0, 0, 0))

    # Yellow
    pygame.draw.circle(screen, (255, 255, 10), (75, 568), 10)
    screen.blit(colourYellow_render, (75, 580))
    # Red
    pygame.draw.circle(screen, (255, 0, 0), (125, 568), 10)
    screen.blit(colourRed_render, (125, 580))
    # Pink
    pygame.draw.circle(screen, (204, 0, 102), (175, 568), 10)
    screen.blit(colourPink_render, (175, 580))
    # Blue
    pygame.draw.circle(screen, (0, 15, 117), (235, 568), 10)
    screen.blit(colourBlue_render, (235, 580))
    # Green
    pygame.draw.circle(screen, (0, 153, 0), (285, 568), 10)
    screen.blit(colourGreen_render, (285, 580))
    # Orange
    pygame.draw.circle(screen, (255, 153, 51), (335, 568), 10)
    screen.blit(colourOrange_render, (335, 580))
    # Lilac
    pygame.draw.circle(screen, (255,153,255), (385, 568), 10)
    screen.blit(colourLilac_render, (385, 580))
    # Turquoise
    pygame.draw.circle(screen, (102, 178, 255), (440, 568), 10)
    screen.blit(colourTurquoise_render, (440, 580))

    h_d = 508
    h_m_1 = 515
    h_m_2 = 500

    for i in range(10):
        pygame.draw.circle(screen, (110, 110, 110), (200, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (245, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (290, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (335, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (380, h_d), 14)
        pygame.draw.circle(screen, (110, 110, 110), (425, h_d), 14)

        h_d = h_d - 44

        pygame.draw.circle(screen, (110, 110, 110), (97, h_m_1), 5)
        pygame.draw.circle(screen, (110, 110, 110), (77, h_m_1), 5)
        pygame.draw.circle(screen, (110, 110, 110), (57, h_m_1), 5)
        pygame.draw.circle(screen, (110, 110, 110), (77, h_m_2), 5)
        pygame.draw.circle(screen, (110, 110, 110), (97, h_m_2), 5)
        pygame.draw.circle(screen, (110, 110, 110), (57, h_m_2), 5)
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
        if (position[i - 3] == 't'):
            pygame.draw.circle(screen, (102, 178, 255), (position[i - 2], position[i - 1]), 15)
        if (position[i - 3] == 'l'):
            pygame.draw.circle(screen, (255,153,255), (position[i - 2], position[i - 1]), 15)

    x_check= 57
    y_check= 500
    controll=0
    height=0
    for i in range (floor):
        for j in range(reply_list[2*i]):
            pygame.draw.circle(screen, (0, 0, 0), (x_check, y_check), 6)
            controll = controll + 1
            if (controll == 1):
                x_check = 77
            elif (controll == 2):
                x_check = 97
            elif (controll == 3):
                height=1
                y_check = y_check + 17
                x_check = 57
            elif (controll == 4):
                x_check = 77
            elif (controll == 5):
                x_check = 97

        for j in range(reply_list[2*i+1]):
            pygame.draw.circle(screen, (255, 255, 255), (x_check, y_check), 6)
            controll = controll + 1
            if (controll == 1):
                x_check = 77
            elif (controll == 2):
                x_check = 97
            elif (controll == 3):
                height=1
                y_check = y_check + 17
                x_check = 57
            elif (controll == 4):
                x_check = 77
            elif (controll == 5):
                x_check = 97

        if(height==1):
            y_check=y_check-17
        y_check=y_check-44
        x_check=57
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
                if(i%6==0):
                    full=1
                x_balls=x_balls+45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n=n+3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                choice = 'g'
                i=i+1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                choice = 'b'
                i=i+1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                choice = 'p'
                i=i+1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                choice = 'r'
                i=i+1
                if (i % 6 == 0):
                    full = 1
                x_balls=x_balls+45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n=n+3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                choice = 'o'
                i=i+1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i%6)-1]=choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                choice = 't'
                i = i + 1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i % 6) - 1] = choice

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                choice = 'l'
                i = i + 1
                if (i % 6 == 0):
                    full = 1
                x_balls = x_balls + 45
                position.append(choice)
                position.append(x_balls)
                position.append(y_balls)
                n = n + 3
                balls[(i % 6) - 1] = choice

        if(full==1):
            result=check()
            if (result==1):
                import won_game.py
                won_game.fun()
                end=1
            elif(i==60 and result==0):
                import lost_game.py
                lost_game.fun()
                end=1
            else:
                y_balls=508-(math.floor(i/6))*44
                x_balls=200-45
                floor=floor+1
                reply_current=reply()
                reply_list.append(reply_current[0])
                reply_list.append(reply_current[1])
            full=0


        if(result==0 and i!=60 and end==0):
            screen_table(screen,n,floor)

        pygame.display.flip()


screen = pygame.display.set_mode((520, 620))
table = pygame.image.load('..\graphics\_table_screen.jpg')
screen.blit(table,(0,0))
pygame.display.flip()
# Positions of the balls
y_balls = 508
x_balls = 200-45
#Number of balls
n=0
#Number of floors
floor=0
result=0
start(x_balls,y_balls,n,floor,result)