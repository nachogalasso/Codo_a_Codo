# Comando para importar modulos
# import module
# print(module.counter)

# podemos usar el from para indicar de dónde queremos traer la información
# from module import suml, prodl

# zeros = [0 for i in range(5)]
# ones =[1 for i in range(5)]

# print(suml(zeros))
# print(prodl(ones))

# para acceder al path podemos usar
# import sys, luego podemos acceder a la ruta
# from sys import path
# luego tenemos que agregarle al nueva ruta con path.append('..\\nuevaruta')
# para iniciar un package no tenemos que olvidar de ponder dentro de la carpeta el __init.py__
# luego también podemos importar utilizando la ruta de acceso de los objetos como por ej
# import extra.iota esto quiere decir que tenemos que importar iota de la carpeta extra
# otra de las maneras es utilizar from extra.iota import funI
# podemos seguir la ruta utilizando la notación de punto

# Vamos a probar PYGAME
"""
import pygame
 
run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False
"""

# PIP
# con pip --version vemos la versión que tenemos instalada en nuestro ordenador. Tenemos que usar el CDM de windows
# con pip help accedemos al listado de comandos que podemos utilizar
# con pip install nombre del paquete, instalamos los paquetes que necesitamos
# con pip install -U hacemos un upgrade
# con pip install package_name==package_version podemos indicarle que version queremos instalar
# con pip uninstall package_name desinstalamos el paquete que ya no queremos usar

from random import randint
    
for i in range(2):
   print(randint(1, 2), end='')