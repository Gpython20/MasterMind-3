import pygame
import math
import sys


mainScreen = pygame.image.load('..\graphics\main_screen.jpg')

instruction = pygame.image.load('..\graphics\instruction.jpg')
startGame = pygame.image.load('..\graphics\levels_screen.jpg')
author = pygame.image.load('..\graphics\_author_screen.jpg')
pygame.init()
screen= pygame.display.set_mode((520,620))
choice=0

#Balls
y_d=350
y_g=200
y_h=math.floor((y_d+y_g)/2)
y1=y_d
y2=y_d
y3=y_d
y4=y_d
y5=y_d
kierunek1=1
kierunek2=1
kierunek3=1
kierunek4=1
kierunek5=1
s2=0
s3=0
s4=0
s5=0
delta = 0.0
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        #Main menu
        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_i:
            choice='i'

        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
            choice='s'

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            choice='a'

        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            choice=0

        #Start game menu
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            choice = 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            choice = 2

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            choice = 3


    if(choice=='i'):
        screen.blit(instruction, (0, 0))
    elif(choice==0):
        screen.blit(mainScreen, (0, 0))
        #Balls
        delta += clock.tick() / 1400.0
        while delta > 1 / 320.0:
            if (y1 <y_g ):
                kierunek1 = 0
            if (y1 > y_d):
                kierunek1 = 1
            if (kierunek1 == 0):
                y1 += 1
            if (kierunek1 == 1):
                y1 -= 1
            if (y1 == y_h):
                s2 = 1
            if (s2 == 1):
                if (y2 < y_g):
                    kierunek2 = 0
                if (y2 > y_d):
                    kierunek2 = 1
                if (kierunek2 == 0):
                    y2 += 1
                if (kierunek2 == 1):
                    y2 -= 1
            if (y2 == y_h):
                s3 = 1
            if (s3 == 1):
                if (y3 < y_g):
                    kierunek3 = 0
                if (y3 > y_d):
                    kierunek3 = 1
                if (kierunek3 == 0):
                    y3 += 1
                if (kierunek3 == 1):
                    y3 -= 1

            if (y3 == y_h):
                s4 = 1
            if (s4 == 1):
                if (y4 < y_g):
                    kierunek4 = 0
                if (y4 > y_d):
                    kierunek4 = 1
                if (kierunek4 == 0):
                    y4 += 1
                if (kierunek4 == 1):
                    y4 -= 1

            if (y4 == y_h):
                s5 = 1
            if (s5 == 1):
                if (y5 < y_g):
                    kierunek5 = 0
                if (y5 > y_d):
                    kierunek5 = 1
                if (kierunek5 == 0):
                    y5 += 1
                if (kierunek5 == 1):
                    y5 -= 1


            delta -= 1 / 320.0
        pygame.draw.circle(screen, (255, 255, 10), (50, y1), 35)
        pygame.draw.circle(screen, (255, 0, 0), (155, y2), 35)
        pygame.draw.circle(screen, (204, 0, 102), (260, y3), 35)
        pygame.draw.circle(screen, (0, 15, 117), (365, y4), 35)
        pygame.draw.circle(screen, (15, 112, 51), (470, y5), 35)


    elif(choice=='s'):
        screen.blit(startGame,(0,0))
    elif (choice == 1):
        import easy
        easy.start()
    elif (choice == 2):
        import hard_game
        hard_game.start()
    elif (choice == 3):
        import AI
        AI.start()
    elif (choice == 'a'):
        screen.blit(author, (0, 0))

    pygame.display.flip()