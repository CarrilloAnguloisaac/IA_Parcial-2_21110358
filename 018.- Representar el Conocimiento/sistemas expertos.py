# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:39:13 2023

@author: EliteDesk
"""

def sistema_experto(clima, temperatura):
    if clima == "soleado":
        if temperatura >= 25:
            return "Juega al tenis"
        else:
            return "No juegues al tenis, hace demasiado frío"
    elif clima == "lluvioso":
        return "No juegues al tenis, está lloviendo"
    else:
        return "Datos de entrada no válidos"

# Ejemplo de uso del sistema experto
clima = input("¿Cómo está el clima? (soleado/lluvioso): ").lower()
temperatura = int(input("¿Cuál es la temperatura en grados Celsius? "))

resultado = sistema_experto(clima, temperatura)
print(resultado)
