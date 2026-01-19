def interpretar_instruccion(texto):
    texto = texto.lower()

    if "procesar" in texto or "limpiar" in texto:
        return {"action": "procesar_base"}

    if "borrar" in texto or "vaciar" in texto:
        for col in ["a", "b", "c", "d", "e"]:
            if f"columna {col}" in texto:
                return {"action": "vaciar_columna", "column": col.upper()}

    return None

