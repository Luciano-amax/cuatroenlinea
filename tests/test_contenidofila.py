from src.anexo import contenidofila

def test_tablero_contenidofila():
        tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
  ]

        assert [1,0,0,0,0,0,0] == contenidofila(3,tablero)
