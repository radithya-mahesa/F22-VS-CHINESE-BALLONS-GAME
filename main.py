import pygame
import random
import math
from pygame import mixer
import os
os.chdir('D:/MAHARDHIKA/AKU SUKA NGODING/Ular Piton/F22 VS CHINEESE BALOONS')

mixer.init()
pygame.init()
mixer.music.load('soundtrack.wav')
mixer.music.play(-1)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('F22 vs Chinese Spy Baloons')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

background=pygame.image.load('bg.jpg')

pesawatimg=pygame.image.load('f22.png')

balonimg=[]
balonX=[]
balonY=[]
balonspeedX=[]
balonspeedY=[]

no_of_balons=1

for i in range(no_of_balons):

    balonimg.append(pygame.image.load('balon.png'))
    balonX.append(random.randint(100,300))
    balonY.append(random.randint(5,10))
    balonspeedX.append(-1)
    balonspeedY.append(130)

score=0


missileimg=pygame.image.load('missile.png')
check=False
missileX=330
missileY=450

pesawatX=300
pesawatY=380
changeX=0
running=True

font=pygame.font.SysFont('Arial',32,'bold')

def score_text():
    img=font.render(f'Score={score}',True, 'white')
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont('Arial',64,'bold')

def gameover():
    img_gameover = font_gameover.render('GAME OVER',True, 'red')
    screen.blit(img_gameover,(245,250))

while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                changeX=-2
            if event.key==pygame.K_d:
                changeX=2
            if event.key==pygame.K_SPACE:
                if check is False:
                    missileSound=mixer.Sound('missile_launch.wav')
                    missileSound.play()
                    check=True
                    missileX=pesawatX+30

        if event.type==pygame.KEYUP:
                changeX=0
    pesawatX+=changeX #pesawatX=pesawatX-changeX
    if pesawatX<=0:
        pesawatX=0
    elif pesawatX>=600:
        pesawatX=600
    for i in range(no_of_balons):
        if balonY[i]>400:
            for j in range(no_of_balons):
                balonY[j]=2000
            gameover()
            break
        balonX[i]+=balonspeedX[i]
        if balonX[i]<=0:
            balonspeedX[i]=1.5
            balonX[i]+=balonspeedY[i]
        if balonX[i]>=600:
            balonspeedX[i]=-1.5
            balonY[i]+=balonspeedY[i]

        distance = math.sqrt(math.pow(missileX-balonX[i],2)+math.pow(missileY-balonY[i],2))
        if distance < 47:
            explosionSound=mixer.Sound('explosion.wav')
            explosionSound.play()
            missileY = 480
            check = False
            balonX[i] = random.randint(0,300)
            balonY[i] = random.randint(30,150)
            score+=1
        screen.blit(balonimg[i], (balonX[i], balonY[i]))
        
    if missileY<=0:
        missileY=450
        check=False
    if check:
        screen.blit(missileimg, (missileX, missileY))
        missileY-=3 

    screen.blit(pesawatimg, (pesawatX, pesawatY))
    score_text()
    pygame.display.update()