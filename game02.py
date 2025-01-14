import pygame
pygame.init()

bg = pygame.display.set_mode((480,360))
pygame.display.set_caption("마우스로 컨트롤 쌈@뽕하게 하기.")
x_pos = 0
y_pos = 0
play = True
while play :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            play = False
        if event.type == pygame.MOUSEMOTION :
            x_pos,y_pos= pygame.mouse.get_pos()
            pygame.draw.circle(bg,(1,0,255),(x_pos, y_pos),7)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                bg.fill((0,0,0))
    pygame.display.update()
pygame.quit()
