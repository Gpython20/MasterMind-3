import pygame
import math
import sys

win = pygame.image.load('..\graphics\win.jpg')
pygame.init()
screen= pygame.display.set_mode((520,620))
def fun():
    delta = 0.0
    clock = pygame.time.Clock()
    start=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.blit(win, (0, 0))
        if(start==0):
            pygame.mixer.music.load('..\music\_fanfare.mp3')
            pygame.mixer.music.play(0)
            start=1

        pygame.display.flip()

fun()