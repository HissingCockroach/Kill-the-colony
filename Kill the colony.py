import os
import random
import sys
import time
import pygame

def image_from_url(url):
    try:
        from urllib2 import urlopen
        from cStringIO import StringIO as inout
    except ImportError:
        from urllib.request import urlopen
        from io import BytesIO as inout
    myurl = urlopen(url)
    return inout(myurl.read())





Bug_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/9705abeb-8eab-4379-afe2-b8355bcd6b4f_zps86fb3a66.jpg?t=1382655213')
Flyswatter_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/Flyswatter_zps8c0c501f.png')
Hit_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/683a3bd2-c45d-4770-b5f1-66bdef066628_zpsf94850e3.jpg?t=1384560988')
Splat_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/Splat_zpsbdf5c74a.png')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BROWN = (139,69,19)
BROWN2 = (218,165,32)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((900,700),0,32)
pygame.display.set_caption('Kill The Colony')
clock = pygame.time.Clock()
u = True
d = False
level = 2
score = 0
splat_image = pygame.image.load(image_from_url(Splat_URL))
bug_image = pygame.image.load(image_from_url(Bug_URL))
Flyswatter = pygame.image.load(image_from_url(Flyswatter_URL))
Flyswatterhit = pygame.image.load(image_from_url(Hit_URL))
myfont = pygame.font.SysFont("Lucida Console", 30)
myfont2 = pygame.font.SysFont("Lucida Console", 100)
myfont3 = pygame.font.SysFont("Comic Sans MS", 80)
place = [(800,298) , (800,200) , (800,80) , (800,500)]
setplace = random.choice(place)
Flyswatter_strike = pygame.transform.rotate(Flyswatter, 180)
label = myfont.render("Play", 1 , BLACK)
label4 = myfont.render("Quit", 1, BLACK)
label3 = myfont3.render("Kill The Colony", 1, YELLOW)
label2 = myfont2.render("GAME OVER", 1, RED)
wat = 0
flyswatter_rect = Flyswatter.get_rect(topleft=(-25,298))
bug_rect = bug_image.get_rect(topleft=(setplace))
hit = False
l = False
strike = False
p = False
while True:
    DISPLAYSURF.fill(WHITE)
    key = pygame.key.get_pressed()

    if l and key[pygame.K_UP]:
        flyswatter_rect.y -= level
    if l and key[pygame.K_DOWN]:
        flyswatter_rect.y += level
    if l and key[pygame.K_SPACE]:
        strike = True
        Flyswatter_strike = pygame.transform.rotate(Flyswatter, 290)
        
        DISPLAYSURF.blit(Flyswatter_strike, flyswatter_rect)
    if not key[pygame.K_SPACE]:
        DISPLAYSURF.blit(Flyswatter, flyswatter_rect)
    DISPLAYSURF.blit(bug_image, bug_rect)

    if l and not hit:
        bug_rect.x -= level

    if p == False:
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(label3, (150,100))
        DISPLAYSURF.blit(label, (360,550))
        DISPLAYSURF.blit(label4, (360,580))
        Flyswatter_hit = pygame.transform.rotate(Flyswatterhit, 290)
        DISPLAYSURF.blit(Flyswatter_hit, (250,200))
        if key[pygame.K_UP]:
            u = True
            d = False
        if u:
            pygame.draw.rect(DISPLAYSURF, BLACK, (350, 550, 80, 30,), 10)
            if key[pygame.K_RETURN]:
                p = True
                l = True
                
        if key[pygame.K_DOWN]:
            d = True
            u = False
        if d:
            pygame.draw.rect(DISPLAYSURF, BLACK, (350, 580, 80, 30,), 10)
            if key[pygame.K_RETURN]:
                pygame.quit()
    
    if key[pygame.K_SPACE] and flyswatter_rect.colliderect(bug_rect):
        place = [(800,500) , (800,80) , (800,200) , (800,298)]
        setplace = random.choice(place)
        bug_rect = bug_image.get_rect(topleft=(setplace))
        level += 0.5
        score += 1
        Flyswatter_hit = pygame.transform.rotate(Flyswatterhit, 290)
        DISPLAYSURF.blit(Flyswatter_hit, flyswatter_rect)
        DISPLAYSURF.blit(bug_image, bug_rect)

        

    if p:    
        scoreboard = myfont.render('Score: {}'.format(score), 1 , BLACK)
        DISPLAYSURF.blit(scoreboard, (10,10))
        
    if bug_rect.x <= -25:
            l = False
            t = True
            a = True
            if t and a:
                label = myfont.render("Play Again", 1 , BLACK)
                DISPLAYSURF.blit(label2, (200,350))
                DISPLAYSURF.blit(label, (370,550))
                DISPLAYSURF.blit(label4, (430,580))
            if key[pygame.K_UP]:
                u = True
                d = False
                
            if u:
                pygame.draw.rect(DISPLAYSURF, BLACK, (360, 550, 220, 30,), 10)
                if key[pygame.K_RETURN]:
                    bug_rect = bug_image.get_rect(topleft=(setplace))
                    flyswatter_rect = Flyswatter.get_rect(topleft=(-25,298))
                    level = 2
                    score = 0
                    p = True
                    l = True
                    t = False
                    a = False
            if key[pygame.K_DOWN]:
                d = True
                u = False
            if d:
                pygame.draw.rect(DISPLAYSURF, BLACK, (430, 580, 80, 30,), 10)
                if key[pygame.K_RETURN]:
                    pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
