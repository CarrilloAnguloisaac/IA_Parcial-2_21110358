# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:41:43 2023

@author: EliteDesk
"""

import numpy as np

def modelo_probabilista_racional(probabilidad_ganar, recompensa_ganar, recompensa_perder):
    utilidad_ganar = probabilidad_ganar * recompensa_ganar
    utilidad_perder = (1 - probabilidad_ganar) * recompensa_perder
    utilidad_total = utilidad_ganar - utilidad_perder
    return utilidad_total

# Ejemplo de uso del modelo
probabilidad_ganar = 0.5  # Probabilidad de ganar (lanzamiento justo de una moneda)
recompensa_ganar = 1  # Recompensa por ganar (por ejemplo, ganar $1)
recompensa_perder = 1  # Recompensa por perder (por ejemplo, perder $1)

utilidad = modelo_probabilista_racional(probabilidad_ganar, recompensa_ganar, recompensa_perder)

if utilidad > 0:
    print("Deberías jugar, la utilidad esperada es positiva.")
elif utilidad < 0:
    print("No deberías jugar, la utilidad esperada es negativa.")
else:
    print("Estás indiferente, la utilidad esperada es cero.")
