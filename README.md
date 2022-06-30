# Examen_Extraord_Superheroes
He incluido también la extensión del juego; adjunto un csv creado al lanzar el main. Al final he dejado las clases y las herencias como estaban, por que si me pongo a separarlo todo, es muy seguro que estropee el codigo, que ahora funciona perfectamente.

#clase SerVivo

 ```
 class SerVivo():

    def __init__(self, est):
        self._energia = est

    def is_vivo(self):
        return self._energia > 0

    def die(self):
        self._energia = 0

    def get_energia(self):
        return self._energia

    def set_energia(self, x):
        self._energia = x
        
  ```
  
  #clase Organización: 
  
   ```
   from enum import Enum
from re import S
import string

class Organizacion: 
    def __init__(self, x, y):
        if type(x) != str:
            raise TypeError("Invalid type for attribute nombre")
        if type(y) != list:
            raise TypeError("Invalid type for attribute superheroes")
        if not y:
             raise ValueError("Invalid value for attribute superheroes")
        self.__nombre = x
        self.__superheroes= y

    def get_nombre(self): 
        return self.__nombre

    def get_superheroes(self): 
        return self.__superheroes

    def set_superheroes(self,x):
        self.__superheroes = x

    #Los nombres no se pueden cambiar, pero los superheroes pueden salir o entrar a distintas organizaciones, lo que es lógico. 

    def is_undefeated(self):
        x = False
        for i in range(len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                x = True
                break 
        return x

    def surrender(self): 
        for superheroe in self.__superheroes: 
            superheroe.die()

    def __str__(self): 
        tp = ""
        for superheroe in self.__superheroes: 
            tp += str(superheroe.get_identificador()) + ". Alias: " + superheroe.get_alias() + ", Tipo:" +  superheroe.get_tipo().name + ", Coste:" + str(superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n"

        return tp

    def __repr__(self):
        tr = ""
        for superheroe in self.__superheroes:
            tr += superheroe.get_identificador() + "\t" + superheroe.get_tipo() + "\t" + superheroe.get_movimientos() + "\n"

    def get_super_undefeated(self):
        sup_vivos = []
        for i in range(0, len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                sup_vivos.append(self.__superheroes[i])

        return sup_vivos
           
  ```
  
  #clase Escenarios 
  
``` 
from enum import Enum

class TipoEscenario(Enum):
    sanctum_sanctorum = [10000, 10, 10, 100]
    stark_tower = [20000, 20, 25, 200]
    xavier_school = [80000, 30, 40, 300]

class Escenarios(): 

    def __init__(self,x,y,a,b):
        self.__monedas = x
        self.__miermbros_ekip = y
        self.__movimientos = a
        self.__energia_vital = b
    
    def get_monedas(self): 
        return self.__monedas

    def get_miembros_ekip(self): 
        return self.__miermbros_ekip

    def get_movimientos(self): 
        return self.__movimientos

    def get_energia_vital(self): 
        return self.__energia_vital

    def from_str(x):

        escenario = x.lower()
        e = None

        for tp in TipoEscenario:
            if escenario == tp.name: 
                a = tp.value
                e = Escenarios(a[0], a[1], a[2], a[3])
                break
        
        if type(e) != Escenarios:
            raise TypeError("Invalid type for attribute nombre")

        return e
        
    #Son 3 escenarios preestablecidos que no se pueden cambiar
    
``` 


#clase Superheroes: sé que no es correcto el poner todas las clases que de las que hereda superheroes (excepto SerVivo) en el mismo documento, pero es como me manejo mejor. No me atrevo a cambiarlo, por si hago algo mal y estropeo el código, que ahro funciona perfectamente. 

``` 
from enum import Enum
import random
from Escenarios import Escenarios
from SerVivo import SerVivo


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


class Superheroes(SerVivo):

    numero_superheroes = 0

    def __init__(self,alias,identidad,tipo, esc):
        self.__identificador = Superheroes.numero_superheroes
        self.__alias = alias
        self.__identidadSecreta = identidad
        self.__movimientos = []
        self.__tipo = tipo
        if type(tipo) != No_humano and type(tipo) != Humano:
            raise TypeError("Invalid type for attribute tipo")

        if tipo.value and type(tipo) == No_humano:
            self.__parrilla_poderes = [2, 7, random.randint(1, 8),random.randint(3, 8), random.randint(1, 8), random.randint(3, 7)]

        elif not tipo.value and type(tipo) == No_humano:
            self.__parrilla_poderes = [4, 5, random.randint(1, 8),random.randint(3, 8), random.randint(1, 8), random.randint(3, 7)]

        elif tipo.value and type(tipo) == Humano:
            self.__parrilla_poderes = [random.randint(3, 8), random.randint(1, 7), random.randint(2, 6),random.randint(2, 6), 1, random.randint(1, 8)]

        else:
            self.__parrilla_poderes = [random.randint(2, 6), random.randint(1, 7), random.randint(2, 6),random.randint(2, 6), random.randint(1, 7), 4]

        if type(esc) != Escenarios: 
            raise TypeError("Invalid type for attribute tipo")
        self.__coste = (esc.get_monedas()/esc.get_miembros_ekip())*(sum(self.__parrilla_poderes)/30)
        self._energia = (esc.get_energia_vital()*self.__parrilla_poderes[3])

        Superheroes.numero_superheroes += 1

        #Identificar al siguiente superheroe en su posicion en la lista
        
    def get_identificador(self): 
        return self.__identificador

    def get_alias(self): 
        return self.__alias

    def get_movimientos(self): 
        return self.__movimientos

    def get_tipo(self): 
        return self.__tipo

    def get_parrillapoderes(self): 
        return self.__parrilla_poderes

    def get_coste(self): 
        return self.__coste

    def set_movimientos(self,x):
        for movimiento in x:
            if movimiento.get_tipo().value: 
                movimiento.set_daño((movimiento.get_daño()/10)*(0.8*self.__parrilla_poderes[1] + 0.25*self.__parrilla_poderes[2] + 0.75*self.__parrilla_poderes[5] + self.__parrilla_poderes[4]))
            else: 
                movimiento.set_daño((movimiento.get_daño()/10)*(self.__parrilla_poderes[0] + 0.75*self.__parrilla_poderes[2] + 0.25*self.__parrilla_poderes[5] + 0.2*self.__parrilla_poderes[1]))
            self.__movimientos.append(movimiento)

    def fight_defense(self, daño): 
        self._energia = self._energia - daño
        if self._energia <= 0:
            self.die()
            self._energia = 0

    def fight_attack(self, obj, ronda):
        obj.fight_defense(self.__movimientos[ronda].get_daño())

    def __str__(self):
        return str(self.get_identificador()) + "| Alias: " + self.get_alias() + "| Tipo:" + self.get_tipo().name + "| Coste:" + str(self.get_coste()) + "| Energia:" + str(self.get_energia()) + "\n"

``` 


