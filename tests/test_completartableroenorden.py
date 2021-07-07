from src.anexo import completarTableroEnOrden

def test_completartableroenorden():
    tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
  ]

    secuencia = [1,2,3,1,4]

    tablero2 = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [2,0,0,0,0,0,0],
   [1,2,1,1,0,0,0],
  ]

    assert completarTableroEnOrden(secuencia,tablero) == tablero2
