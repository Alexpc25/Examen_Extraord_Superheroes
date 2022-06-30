from enum import Enum

class Movimiento_Type(Enum):
    ATAQUE = 1
    DEFENSA = 0


class Movimientos_General():
    def __init__(self, x, a, daño):
        self.__nombre = x
        self.__tipo = a
        self.__daño = daño

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_daño(self):
        return self.__daño

    def set_daño(self, daño):
        self.__daño = daño


class Movimientos_Especifico(Movimientos_General):
    def __init__(self, x, a, daño, superheroe):
        super().__init__(x, a, daño)
        self.__superheroe = superheroe

    def get_superheroe(self):
        return self.__superheroe