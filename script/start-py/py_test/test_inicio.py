from src.inicio import Inicio


def test_iniciando_sistema():
    # Given
    teste_entrada = True
    # When
    iniciando = Inicio(teste_entrada)
    teste_saida = iniciando.inicio

    # Then
    assert teste_entrada == teste_saida
