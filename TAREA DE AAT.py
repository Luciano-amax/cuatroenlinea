def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]
def contenidoColumna(num, tablero):
    columna = []
    for fila in tablero:
        celda = fila[num -1]
        columna.append(celda)
    return columna
    
            
def soltarFichaEnColumna(ficha,columna,tablero):
    for fila in range(6,0,-1):
        if tablero[fila-1][columna-1]==0:
            tablero[fila-1][columna-1]=ficha
            return
    

def completarTableroEnOrden(secuencia,tablero):
    ficha = 1
    for juga in secuencia:
        soltarFichaEnColumna(ficha,juga,tablero)
        if ficha==1:
            ficha=2
        else:
            ficha=1
    return tablero


def dibujarTablero(tablero):
    for fila in range(0,6,1):
        for columna in range(0,6,1):
            celda=tablero[fila][columna]
            if(celda):
                print(celda,end='')
            else:
                print(end='')
        print()


def VerificarSecuencia(secuencia):
    for ver in secuencia:
        if(ver < 1 or ver > 7):
            print("¡La secuncia ingresada es invalida !")
            return False
    return True

        
secuencia = [1,2,3,1,4,6]

tablero = []
if (VerificarSecuencia(secuencia)):
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)

print(contenidoColumna(1, tablero))
