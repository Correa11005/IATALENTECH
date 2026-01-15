# librerias
import re

"""
expresiones regulares en python
problemas reales 
"""

#codigo
print("libreria cargada correctamente")

#ejemplo 1 
texto="mi nombre es 132"
resultado= re.search(r"\d+",texto)
print(resultado.group())