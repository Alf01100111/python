import pygame
pygame.init()
screen = pygame.dysplay.set_mode([800,600])
keep_going = True
pic = picgame.image.load("CrazySmile.bmp")
while keep_going:
    for event in pygame.event.get():
        keep_going = False
    screen.blit(pic, (100,100))
    pygame.display.update()
   
pygame.quit() #Quit
  
