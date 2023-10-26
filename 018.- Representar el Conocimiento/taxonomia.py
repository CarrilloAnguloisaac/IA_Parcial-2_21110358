# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:16:37 2023

@author: EliteDesk
"""

# Clase base para animales
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Subclases que heredan de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Tweet!"

# Crear instancias de las subclases
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")
mi_pajaro = Pajaro("Tweetie")

# Llamar al método hacer_sonido de las instancias
print(mi_perro.nombre + ": " + mi_perro.hacer_sonido())  # Salida: Buddy: Woof!
print(mi_gato.nombre + ": " + mi_gato.hacer_sonido())    # Salida: Whiskers: Meow!
print(mi_pajaro.nombre + ": " + mi_pajaro.hacer_sonido())  # Salida: Tweetie: Tweet!
