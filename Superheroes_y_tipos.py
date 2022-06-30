from enum import Enum

class Superheroe_Type():

    def from_str(x, clase):

        superheroe = x.upper()
        e = None
        for tp in clase:
            if superheroe == tp.name:
                e = tp
                break

        if type(e) != Superheroe_Type:
            raise TypeError("Invalid type for attribute tipo superheroe")

        return e


class Humano(Superheroe_Type, Enum):
    MUTANTE = 1
    HOMO_SUPERIOR = 0

class No_humano(Superheroe_Type,Enum):
    ASGARDIANO = 1
    KREE = 0
