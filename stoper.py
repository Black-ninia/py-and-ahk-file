from time import sleep
import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((50, 30))

pygame.display.set_caption("super odliczanie")

'https://www.tiktok.com/@black_ninia?lang=pl-PL'

#import webbrowser as wb
#wb.open('https://www.tiktok.com/@black_ninia?lang=pl-PL') 

#image = pygame.image.load('helmet.png')
running = True
running2 = False 
m = 0
s = 0
            

while running:
   screen.fill((167, 184, 86))
   
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
           print('zatrzymano stoper obecny pomiar:')
   
   pygame.display.update()
   
   sleep(1.0)
   s = s + 1
   if s == 60:
     s = 0
     m = m + 1
     print(m)
     print("minut")
     print(s)
     print('sekund')
     min = True
   else:
     print(m)
     print('minut')
     print(s)
     print('sekund') 

while not running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = True
