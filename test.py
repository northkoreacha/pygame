import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("game 01")

x_pos = background.get_size() [0] // 2
y_pos = background.get_size() [1] // 2
to_x=0
to_y=0


play = True
while play :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            play == False
            pygame.quit()
        if event.type== pygame.KEYDOWN : 
            if event.key == pygame.K_UP:
                to_y= -0.1
            if event.key == pygame.K_RIGHT:
                print('right')
                to_x=0.1
            if event.key == pygame.K_DOWN:
                print('down')
                to_y= 0.1
            if event.key == pygame.K_LEFT:
                print('left')
                to_x=-0.1
        if event.type== pygame.KEYUP : 
            if event.key == pygame.K_UP:
                to_y= 0
            if event.key == pygame.K_RIGHT:
                print('right')
                to_x= 0
            if event.key == pygame.K_DOWN:
                print('down')
                to_y= 0
            if event.key == pygame.K_LEFT:
                print('left')
                to_x= 0
        if event.type== pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                y_pos-=10
        if event.type== pygame.KEYUP :
            if event.key == pygame.K_SPACE:
                y_pos+=10
            
    x_pos += to_x
    y_pos += to_y
   
    background.fill((0,0,255))
    pygame.draw.circle(background, (0,255,0),(x_pos,y_pos), 8)
    pygame.display.update()
