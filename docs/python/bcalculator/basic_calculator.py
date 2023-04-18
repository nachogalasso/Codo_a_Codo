# 1ro tenemos que definir las functions que vamos a necesitar, add, sub, mul, and div
# imprimir las opciones al usuario
# pedir los valores
# llamar a las funciones
# tenemos que usar un bucle while hasta que el usuario decida salir del mismo

# Functions
def add(a, b):
    result = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(result) + '\n')


def sub(a, b):
    result = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(result) + '\n')


def mul(a, b):
    result = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(result) + '\n')


def div(a, b):
    result = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(result) + '\n')
    
while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiply')
    print('D. Division')
    print('E. Exit')

    choices = input('Elige que operación quieres realizar: ')

    if choices == 'a' or choices == 'A':
        print('Addition')
        a = int(input('Ingresa el primer número:'))
        b = int(input('Ingresa el segundo número:'))
        add(a, b)
    elif choices == 'b' or choices == 'B':
        print('Subtraction')
        a = int(input('Ingresa el primer número:'))
        b = int(input('Ingresa el segundo número:'))
        sub(a, b)
    elif choices == 'c' or choices == 'C':
        print('Multiply')
        a = int(input('Ingresa el primer número:'))
        b = int(input('Ingresa el segundo número:'))
        mul(a, b)
    elif choices == 'd' or choices == 'D':
        print('Division')
        a = int(input('Ingresa el primer número:'))
        b = int(input('Ingresa el segundo número:'))
        div(a, b)
    elif choices == 'e' or choices == 'E':
        print('calculos terminado')
        quit()
        