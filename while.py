import math

i=1
while(i!=0):    
    print('La Arepa')
    print('***************')
    print('Digita 0. para salir.')
    print('digita 1. paara calcular la raiz cuadrada de un numero.')
    print('digita 2. para calcular la potencia 2 de un numero') 
    i = int(input());   
    if(i==0):
        break
    elif(i==1):
        number= int(input('Dijita un numero: '))
        if(number<0):
            print(f"La raiz de: {number} es: {math.sqrt(number *(-1))}i")
        else:
            print(f"La raiz de: {number} es: {math.sqrt(number)}")
    elif(i==2):
        number2 = int(input('Digite un numero: '))
        print(f"La potencia cuadrada de:{number2} es: {int(math.pow(number2))}")
    else:
        print("Digitaste una opción incorrecta.")

    