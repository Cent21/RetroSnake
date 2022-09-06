import pygame
import random
from pygame import mixer

pygame.init()
width, height =1280, 720
game_screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption("MinimalSnake")
#IMAGES
bg = pygame.image.load("bg.png").convert_alpha()
foodimg = pygame.image.load("food.png").convert_alpha()
pauseimg = pygame.image.load("pausemenu.png").convert_alpha()
closeicon = pygame.image.load("closeicon.png").convert_alpha()
panel = pygame.image.load("panel.png").convert_alpha()
menuimg = pygame.image.load("mainmenu.png").convert_alpha()
gameoverimg = pygame.image.load("gameover.png").convert_alpha()


closeiconnewrect = closeicon.get_rect(topleft = (1230,10))
ypos = 300
ypos1 = 0
ypos2 = 0

#sound
mixer.music.load("bgmusic.mp3")
mixer.music.play(-1)


#SnakeCoordinates
x, y = 200, 200
delta_x, delta_y =20, 0

#Food Coordinates
food_x, food_y = random.randrange(0, width)//20*20,random.randrange(50, height)//20*20

body_list = [(x, y)]

clock = pygame.time.Clock()
game_over = False
menu = True
pause = False
font = pygame.font.SysFont("Mochiy Pop One", 60)

def snake():

    global x, y, food_x, food_y, game_over, pause
    x = (x + delta_x)%width
    y = (y + delta_y)%height

    if((x,y) in body_list):
        game_over =True

        return
    body_list.append((x,y))

#SnakeisEatingzzzzz
    if(food_x == x and food_y == y):
        munchsound = mixer.Sound("munch.mp3")
        munchsound.play()
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, width) // 20 * 20, random.randrange(50, height) // 20 * 20
    else:
        del body_list[0]


#bg,score,GRAPHICS
    game_screen.blit(bg, (0, 50))
    score = font.render("Score: "+ str(len(body_list) -1), True, (190, 81, 8))
    game_screen.blit(score, [10,10])

#FOODgraphics
    game_screen.blit(foodimg, (food_x, food_y))

#SNAKE UI
    for (i,j) in body_list:
        pygame.draw.rect(game_screen, (255, 255, 255), [i, j, 20, 20])
        game_screen.blit(panel, (0, 0))
        game_screen.blit(closeicon, (1230, 10))
        game_screen.blit(score, [10, 10])
    pygame.display.update()


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and closeiconnewrect.collidepoint(pos):
                    pygame.quit()
                    quit()
            game_screen.blit(pauseimg,(0,0))
            pygame.display.update()
            clock.tick(5)


while True:
    while menu:
        game_screen.blit(menuimg, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and closeiconnewrect.collidepoint(pos):
                    pygame.quit()
                    quit()
        #MovingSnakeInMenuGrpahics
        pygame.draw.rect(game_screen, (255, 255, 255), [80, ypos, 40, 450])
        pygame.draw.rect(game_screen, (255, 255, 255), [1150, ypos1, 40, 450])
        ypos += 7
        ypos1 -= 8
        if ypos > 720: ypos = -500
        if ypos1 < -500: ypos1 = 720
        clock.tick(35)
        pygame.display.update()


    while game_over:
        game_screen.blit(gameoverimg, (0, 0))
        score = font.render("Score: " + str(len(body_list)), True, (243, 1, 116))
        game_screen.blit(score, [550, 290])
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    body_list = [(200, 200)]
                    game_over = False
                    menu = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and closeiconnewrect.collidepoint(pos):
                    pygame.quit()
                    quit()
        # pygame.draw.rect(game_screen, (255,255,255), [ypos, 180, 450, 20])
        # pygame.draw.rect(game_screen, (244, 1, 118), [ypos1, 550, 450, 20])
        pygame.draw.rect(game_screen, (255, 255, 255), [1150, ypos2, 20, 450])

        # ypos += 7
        # ypos1 -= 8
        ypos2 -= 8
        # if ypos > 1280: ypos = -500
        # if ypos1 < -500: ypos1 = 1280
        if ypos2 < -500: ypos2 = 720
        clock.tick(15)
        pygame.display.update()




    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                if(delta_x != 20):
                    delta_x = -20
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if (delta_x != -20):
                    delta_x = 20
                delta_y = 0
            elif (event.key == pygame.K_UP):
                delta_x = 0
                if (delta_y != 20):
                    delta_y = -20
            elif (event.key == pygame.K_DOWN):
                delta_x = 0
                if (delta_y != -20):
                    delta_y = 20
            elif (event.key == pygame.K_SPACE):
                pause()
        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and closeiconnewrect.collidepoint(pos):
                pygame.quit()
                quit()



    snake()
    clock.tick(10)

