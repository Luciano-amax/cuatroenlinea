from src.anexo import tableroVacio

def test_tablero_vacio_tiene_6filas_y_7columnas():
    tablero  = tableroVacio()
    assert len(tablero) == 6
    
def test_tablero_vacio_tiene_7columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) == 7


