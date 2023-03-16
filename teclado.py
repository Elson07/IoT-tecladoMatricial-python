from machine import Pin
from time import sleep

Filas = [32,33,18,5]
for i in range(4):
    Pin(Filas[i],Pin.OUT)

Columnas = [26,27,12,13]

Col1=Pin(Columnas[0],Pin.IN,Pin.PULL_DOWN)
Col2=Pin(Columnas[1],Pin.IN,Pin.PULL_DOWN)
Col3=Pin(Columnas[2],Pin.IN,Pin.PULL_DOWN)
Col4=Pin(Columnas[3],Pin.IN,Pin.PULL_DOWN)

def lectura(FILAS, CARACTERES):
    EnFilas = Pin(FILAS,Pin.OUT)
    EnFilas.on()
    if(Col1.value()==1):
        return CARACTERES[0]
    if(Col2.value()==1):
        return CARACTERES[1]
    if(Col3.value()==1):
        return CARACTERES[2]
    if(Col4.value()==1):
        return CARACTERES[3]
    EnFilas.off()
try:
    
    while True:
        valor1 = lectura(Filas[0],["1","2","3","A"])
        valor2 = lectura(Filas[1],["4","5","6","B"])
        valor3 = lectura(Filas[2],["7","8","9","C"])
        valor4 = lectura(Filas[3],["*","0","#","D"])
        
        if valor1 != None:
            return valor1
            sleep(0.3)
        elif valor2 != None:
            return valor2
            sleep(0.3)
        elif valor3 != None:
            return valor3
            sleep(0.3)
        elif valor4 != None:
            return valor4
            sleep(0.3)
        
except KeyboardInterrupt:
    print("\nFim do programa")
        