from math import pi
class Cercle:
    def __init__(self,rayon):
        self.rayon=rayon
    @property
    def rayon(self):
        return self.__rayon
    @rayon.setter
    def rayon(self, value):
        if value<0:
            raise ValueError("valeru negative")
        self.__rayon=value
    @property
    def perimetre(self):
        return self.__rayon*2*pi
    @property
    def surface(self):
        return pi * (self.__rayon ** 2)

