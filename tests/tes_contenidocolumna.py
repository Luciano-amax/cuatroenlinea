from src.anexo import contenidoColumna

def test_contcolumnas():
    tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
  ]

columnas=[0,0,1,1,1,1] == contenidoColumna(1,tablero)
