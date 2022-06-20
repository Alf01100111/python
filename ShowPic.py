import pygame
pygame.init()
screen = pygame.dysplay.set_mode([600,600])
keep_going = True
pic = picgame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()
speed = 5

while keep_going:
    for event in pygame.event.get():
        keep_going = False
    picx += speed                        #Передвинуть картинку
    picy += speed
    
    if picx <= 0 or picx + pic.get_width() >= 600:  #проверка на коллизию с левой и правой стеной
        speed = -speed
        
    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    timer.tick(60)                       #ограничить фпс 60
   
pygame.quit() #Quit
  
