class Inicio:

    def __init__(self, inicio: bool) -> None:
        self.__inicio = inicio

    @property
    def inicio(self) -> bool:
        return self.__inicio
