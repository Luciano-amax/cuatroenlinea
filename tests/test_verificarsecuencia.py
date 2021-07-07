from src.anexo import VerificarSecuencia

def test_verificarsecuencia():
    s1 = [1,2,3,4,5,1,2,3]
    s2 = [1,2,3,4,5,21]
    assert VerificarSecuencia(s1) == True
    assert VerificarSecuencia(s2) == False
