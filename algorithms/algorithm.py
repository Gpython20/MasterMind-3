import random

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
print(balls_code)

colours=[]
colours.append('y')
colours.append('r')
colours.append('p')
colours.append('b')
colours.append('g')
colours.append('o')
print(colours)

#save the balls
balls=[]
for i in range(4):
    balls.append(0)
position=[]


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
    print("w: ", white, "b: ",black)


result=0
raw=0
i=0
while(result!=1 and raw <10):
    if(i<4):
        choice = input()
        balls[i]=choice
        i=i+1
        print(balls)
    else:
        i=0
        raw=raw+1
        result=check()
        reply()

print(raw)