import re
# ==============================
# FUNCION
# Elimina caracteres no numericos de un documento
#cc75.888.56 = "7588856"
# ==============================
def clean_id(value):
    if value is None: 
        return ""
    return re.sub(r"\D",'',str(value))
# ==============================
#  FUNCION merge _name 
#  Une nombre y apellido en un solo campo 
# ==============================
def merge_name(name, lastname): 
    if name is None:
        name= ""
    if lastname is None:
        lastname= ""
    return f"{name} {lastname}".strip()
