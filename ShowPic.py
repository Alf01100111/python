import pygame
pygame.init()
screen = pygame.dysplay.set_mode([800,600])
keep_going = True
pic = picgame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()
speedx = 5
speedy = 5

while keep_going:                        #Игровой цикл
    for event in pygame.event.get():
        keep_going = False
    picx += speedx                       #Передвинуть картинку
    picy += speedy
    
    if picx <= 0 or picx + pic.get_width() >= 800:  #проверка на коллизию с левой и правой стеной
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy
        
    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    timer.tick(60)                       #ограничить фпс 60
   
pygame.quit() #Quit
  
