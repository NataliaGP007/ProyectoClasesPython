"""
Desarrollar un algoritmo que pida el nombre del usuario, el día, mes y año actual y el día, mes y año de nacimiento del
usuario. En  base a esos datos el algoritmo indica el signo zodiacal, la edad en horas y el número de la suerte del
usuario.

Autor: Natalia Gutiérrez Pineda.
"""

#Clase publica
class Numerologia:
    #Esta clase indica  la edad, signo sodiacal y numero de la suerte del usuario.

    #Atributos
    __nombre = str(" ")
    __anioNacimiento = int(0)
    __mesNacimiento = int(0)
    __diaNacimiento = int(0)
    __anioActual = int(0)
    __mesActual = int(0)
    __diaActual = int(0)
    __edad = int(0)
    __edadHoras = int(0)
    __signoZodiacal = str(" ")
    __numeroSuerte = int(0)

    #Metodos de instancia
    def calcularEdad(self, anioActual, mesActual, diaActual, anioNacimiento, mesNacimiento, diaNacimiento):
        # Este metodo calculará la edad del usuario.
        self.__anioActual = anioActual
        self.__mesActual = mesActual
        self.__diaActual = diaActual
        self.__anioNacimiento = anioNacimiento
        self.__mesNacimiento = mesNacimiento
        self.__diaNacimiento = diaNacimiento
        self.__edad = self.__anioActual - self.__anioNacimiento
        if (self.__mesActual < self.__mesNacimiento) or (
                self.__mesActual == self.__mesNacimiento and self.__diaActual < diaNacimiento):
            self.__edad = self.__edad - 1

        return self.__edad

    def convertirEdadEnHoras(self):
        # Este metodo convertirá la edad en años del usuario a horas a partir de la equivalencia de años a horas.
        return self.__edad * 8760

    def identificarSignoZodiacal(self):
        # Este metodo identificará el signo zodiacal del usuario.
        if (self.__mesNacimiento == 12 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 1 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Capricornio'
        if (self.__mesNacimiento == 1 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 2 and self.__diaNacimiento <= 19):
            self.__signoZodiacal = 'Acuario'
        if (self.__mesNacimiento == 2 and self.__diaNacimiento >= 20) or (self.__mesNacimiento == 3 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Piscis'
        if (self.__mesNacimiento == 3 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 4 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Aries'
        if (self.__mesNacimiento == 4 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 5 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = 'Tauro'
        if (self.__mesNacimiento == 5 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 6 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Géminis'
        if (self.__mesNacimiento == 6 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 7 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Cáncer'
        if (self.__mesNacimiento == 7 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 8 and self.__diaNacimiento <= 23):
            self.__signoZodiacal = 'Leo'
        if (self.__mesNacimiento == 8 and self.__diaNacimiento >= 24) or (self.__mesNacimiento == 9 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Virgo'
        if (self.__mesNacimiento == 9 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 10 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Libra'
        if (self.__mesNacimiento == 10 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 11 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = 'Escorpio'
        if (self.__mesNacimiento == 11 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 12 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = 'Sagitario'
        return self.__signoZodiacal

    def calcularNumeroSuerte (self):
        # Este metodo calculará el numero de la suerte del usuario.
        while self.__anioNacimiento > 0:
            self. __numeroSuerte = self. __numeroSuerte + self.__anioNacimiento % 10
            self.__anioNacimiento = self.__anioNacimiento // 10

        while self.__numeroSuerte > 9:
                self.__numeroSuerte = self.__numeroSuerte - 9

        return self.__numeroSuerte

from abc import ABC

#Clase abstracta
class Abstracta(ABC):

    #Metodos static
    @staticmethod
    def calcularEdad(anioActual, mesActual, diaActual, anioNacimiento, mesNacimiento, diaNacimiento):
        # Este metodo calculará la edad del usuario en horas.
        edad = anioActual - anioNacimiento
        if (mesActual < mesNacimiento) or (mesActual == mesNacimiento and diaActual < diaNacimiento):
            edad = edad - 1
        return edad * 8760

    @staticmethod
    def identificarSignoZodiacal(mesNacimiento, diaNacimiento):
        #Este metodo identificará el signo zodiacal del usuario.
        signoZodiacal = " "
        if (mesNacimiento == 12 and diaNacimiento >= 22) or (mesNacimiento == 1 and diaNacimiento <= 20):
            signoZodiacal = 'Capricornio'
        if (mesNacimiento == 1 and diaNacimiento >= 22) or (mesNacimiento == 2 and diaNacimiento <= 19):
            signoZodiacal = 'Acuario'
        if (mesNacimiento == 2 and diaNacimiento >= 20) or (mesNacimiento == 3 and diaNacimiento <= 20):
            signoZodiacal = 'Piscis'
        if (mesNacimiento == 3 and diaNacimiento >= 21) or (mesNacimiento == 4 and diaNacimiento <= 20):
            signoZodiacal = 'Aries'
        if (mesNacimiento == 4 and diaNacimiento >= 21) or (mesNacimiento == 5 and diaNacimiento <= 20):
            signoZodiacal = 'Tauro'
        if (mesNacimiento == 5 and diaNacimiento >= 21) or (mesNacimiento == 6 and diaNacimiento <= 21):
            signoZodiacal = 'Géminis'
        if (mesNacimiento == 6 and diaNacimiento >= 22) or (mesNacimiento == 7 and diaNacimiento <= 22):
            signoZodiacal = 'Cáncer'
        if (mesNacimiento == 7 and diaNacimiento >= 23) or (mesNacimiento == 8 and diaNacimiento <= 23):
            signoZodiacal = 'Leo'
        if (mesNacimiento == 8 and diaNacimiento >= 24) or (mesNacimiento == 9 and diaNacimiento <= 22):
            signoZodiacal = 'Virgo'
        if (mesNacimiento == 9 and diaNacimiento >= 23) or (mesNacimiento == 10 and diaNacimiento <= 22):
            signoZodiacal = 'Libra'
        if (mesNacimiento == 10 and diaNacimiento >= 23) or (mesNacimiento == 11 and diaNacimiento <= 22):
            signoZodiacal = 'Escorpio'
        if (mesNacimiento == 11 and diaNacimiento >= 23) or (mesNacimiento == 12 and diaNacimiento <= 21):
            signoZodiacal = 'Sagitario'
        
        return signoZodiacal

    @staticmethod
    def calcularNumeroSuerte (anioNacimiento):
        # Este metodo calculará el numero de la suerte del usuario.
        numeroSuerte = 0
        while anioNacimiento > 0:
            numeroSuerte = numeroSuerte + anioNacimiento % 10
            anioNacimiento = anioNacimiento // 10

        while numeroSuerte > 9:
                numeroSuerte = numeroSuerte - 9

        return numeroSuerte

#Clase main
class Main:
    if __name__ == "__main__":
        #Instancia
        numero = Numerologia()
        abstracta = Abstracta()
        print(numero.calcularEdad(2022, 4, 1, 2003, 7, 27))
        print(numero.convertirEdadEnHoras())
        print(numero.identificarSignoZodiacal())
        print(numero.calcularNumeroSuerte())
        print(abstracta.calcularEdad(2022, 4, 1, 2003, 7, 27))
        print(abstracta.identificarSignoZodiacal(7, 27))
        print(abstracta.calcularNumeroSuerte(2003))
        
