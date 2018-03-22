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


balls_code=[]
for i in range(4):
    balls_code.append(-1)

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

combinations=[]

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
    game_type = 'AI'
    attempt = 'Ilosc prob: '
    game_type_render = font.render(game_type, 1, (0, 0, 0))
    attempt_render = font.render(attempt, 1, (0, 0, 0))

    x = 120
    for i in range(4):
        if(balls_code[i]==-1):
            pygame.draw.circle(screen, (110, 110, 110), (x, 580), 15)
        else:
            if (balls_code[i] == 0):
                pygame.draw.circle(screen, (255, 255, 10), (x, 580), 15)
            elif (balls_code[i] == 1):
                pygame.draw.circle(screen, (255, 0, 0), (x, 580), 15)
            elif (balls_code[i] == 2):
                pygame.draw.circle(screen, (204, 0, 102), (x, 580), 15)
            elif (balls_code[i] == 3):
                pygame.draw.circle(screen, (0, 15, 117), (x, 580), 15)
            elif (balls_code[i] == 4):
                pygame.draw.circle(screen, (0, 153, 0), (x, 580), 15)
            elif (balls_code[i] == 5):
                pygame.draw.circle(screen, (255, 153, 51), (x, 580), 15)
        x = x + 90


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



def generate_permutations(base,k):
    if(k==0):
        combinations.append(base[:])
    else:
        for i in range(k+1):
            base[i],base[k]=base[k],base[i]
            generate_permutations(base,k-1)
            base[i], base[k] = base[k], base[i]

def create_combinations():
    base=['y','r','p','b']
    generate_permutations(base,3)
    base = ['y', 'r', 'p', 'g']
    generate_permutations(base, 3)
    base = ['y', 'r', 'g', 'b']
    generate_permutations(base, 3)
    base = ['y', 'g', 'p', 'b']
    generate_permutations(base, 3)
    base = ['g', 'r', 'p', 'b']
    generate_permutations(base, 3)
    base = ['y', 'r', 'p', 'o']
    generate_permutations(base, 3)
    base = ['y', 'r', 'o', 'b']
    generate_permutations(base, 3)
    base = ['y', 'o', 'p', 'b']
    generate_permutations(base, 3)
    base = ['o', 'r', 'p', 'b']
    generate_permutations(base, 3)
    base = ['y', 'r', 'g', 'o']
    generate_permutations(base, 3)
    base = ['y', 'g', 'p', 'o']
    generate_permutations(base, 3)
    base = ['g', 'r', 'p', 'o']
    generate_permutations(base, 3)
    base = ['y', 'g', 'o', 'b']
    generate_permutations(base, 3)
    base = ['g', 'r', 'o', 'b']
    generate_permutations(base, 3)
    base = ['g', 'o', 'p', 'b']
    generate_permutations(base, 3)

def compare(combination,lastanswer):
    black = 0
    white = 0
    for i in range(4):
        if (combination[i] == lastanswer[i]):
            black = black + 1
        else:
            for j in range(4):
                if (combination[i] == lastanswer[j]):
                    white = white + 1
    return black, white

def get_computer_answer(white,black,lastanswer):
    ans = []
    ans.append(0)
    ans.append(0)
    ans.append(0)
    ans.append(0)
    if(white==-1 and black == -1):
        ans[0]='y'
        ans[1] = 'r'
        ans[2] = 'p'
        ans[3] = 'b'
    else:
        comp_res = []
        new_comb=[]
        for i in range(len(combinations)):
            comp_res = compare(combinations[i],lastanswer)
            if(comp_res[0]==black and comp_res[1]==white):
                new_comb.append(combinations[i])
        combinations.clear()
        for i in range(len(new_comb)):
            combinations.append(new_comb[i])
        r=random.randint(0,len(combinations)-1)
        ans=combinations[r]
    return ans


clock = pygame.time.Clock()

def sleep():
    delta = 0.0
    while delta < 1.0 / 1.0:
        delta+=clock.tick()/1400.0

def start(x_balls,y_balls,n,floor,result):
    font=pygame.font.SysFont("dejavusans",25)
    choice = 0
    end=0
    i=0
    full=0
    reply_current = []
    reply_current.append(0)
    reply_current.append(0)
    i=0
    black=-1
    white=-1
    create_combinations()
    ans = []
    code=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                balls_code[code]=0
                code=code+1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                balls_code[code]=1
                code = code + 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                balls_code[code]=2
                code = code + 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                balls_code[code]=3
                code = code + 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                balls_code[code]=4
                code = code + 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                balls_code[code]=5
                code = code + 1
        if(code==4):
            break
        screen_table(screen, n, floor)
        pygame.display.flip()



    for k in range(10):
        sleep()
        ans=get_computer_answer(white,black,ans)

        for q in range(4):
            x_balls = x_balls + 75
            position.append(ans[q])
            position.append(x_balls)
            position.append(y_balls)
            n = n + 3
            balls[q]=ans[q]
            i=i+1

        full=1
        if(full==1):
            result=check()
            if (result==1):
                y_balls = 508 - (math.floor(i / 4)) * 44
                x_balls = 125
                floor = floor + 1
                reply_current = reply()
                reply_list.append(reply_current[0])
                reply_list.append(reply_current[1])
                black = reply_current[0]
                white = reply_current[1]
                screen_table(screen, n, floor)
                pygame.display.flip()
                sleep()
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
                black=reply_current[0]
                white=reply_current[1]


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