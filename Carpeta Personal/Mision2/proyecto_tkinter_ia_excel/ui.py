import tkinter as tk
from tkinter import filedialog, messagebox
import re

from processor import ejecutar_accion

archivo_seleccionado = None
label_archivo = None
entrada_instruccion = None


# =========================
# SELECCIONAR ARCHIVO
# =========================
def seleccionar_excel():
    global archivo_seleccionado

    archivo_seleccionado = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel", "*.xlsx")]
    )

    if archivo_seleccionado:
        label_archivo.config(text=archivo_seleccionado)
        messagebox.showinfo("Archivo cargado", "Archivo Excel seleccionado correctamente")


# =========================
# PARSER: UNIR NOMBRES
# =========================
def parse_unir_nombres(texto: str):
    """
    Devuelve (col_nombre, col_apellido, col_destino) o None si no coincide.

    Acepta:
      - unir nombres b c en f
      - unir nombres b y c en f
      - unir nombres b,c->f
      - unir nombre b c a f
      - unir nombres b,c en f
    """
    texto = texto.lower().strip()

    # Normaliza flecha y separadores raros a espacios
    texto_norm = texto.replace("->", " en ").replace(",", " ")

    # Caso simple: "unir nombres b c en f"
    m = re.search(r"\bunir\s+nombres?\s+([a-z])\s+([a-z])\s+(?:en|a)\s+([a-z])\b", texto_norm)
    if m:
        return (m.group(1).upper(), m.group(2).upper(), m.group(3).upper())

    # Caso con "y": "unir nombres b y c en f"
    m = re.search(r"\bunir\s+nombres?\s+([a-z])\s+y\s+([a-z])\s+(?:en|a)\s+([a-z])\b", texto_norm)
    if m:
        return (m.group(1).upper(), m.group(2).upper(), m.group(3).upper())

    return None


# =========================
# EJECUTAR INSTRUCCIÓN
# =========================
def ejecutar_instruccion():
    if not archivo_seleccionado:
        messagebox.showwarning("Advertencia", "Primero seleccione un archivo Excel")
        return

    texto = entrada_instruccion.get().strip()

    if not texto:
        messagebox.showwarning("Advertencia", "Ingrese una instrucción")
        return

    texto_lower = texto.lower().strip()

    try:
        # -------- 1) BORRAR / VACIAR COLUMNA --------
        m_col = re.search(r"\b(borrar|vaciar)\s+columna\s+([a-z])\b", texto_lower)
        if m_col:
            col = m_col.group(2).upper()

            instruccion = {
                "action": "vaciar_columna",
                "column": col
            }

            ejecutar_accion(archivo_seleccionado, instruccion)
            messagebox.showinfo("Éxito", f"Columna {col} vaciada correctamente")
            return

        # -------- 2) UNIR NOMBRES CON COLUMNAS --------
        unir = parse_unir_nombres(texto_lower)
        if unir:
            col_nombre, col_apellido, col_destino = unir

            instruccion = {
                "action": "unir_nombres",
                "col_nombre": col_nombre,
                "col_apellido": col_apellido,
                "col_destino": col_destino
            }

            ejecutar_accion(archivo_seleccionado, instruccion)
            messagebox.showinfo(
                "Éxito",
                f"Nombres unidos ({col_nombre} + {col_apellido} → {col_destino}) correctamente"
            )
            return

        # -------- 3) PROCESAR / LIMPIAR DATOS --------
        if "procesar" in texto_lower or "limpiar datos" in texto_lower:
            instruccion = {"action": "procesar_base"}
            ejecutar_accion(archivo_seleccionado, instruccion)
            messagebox.showinfo("Éxito", "Archivo procesado correctamente")
            return

        # -------- NO RECONOCIDA --------
        messagebox.showerror("Instrucción no reconocida", "No se pudo entender la instrucción")

    except PermissionError:
        messagebox.showerror("Error", "El archivo Excel está abierto.\nCiérrelo e intente nuevamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# APP PRINCIPAL
# =========================
def iniciar_app():
    global label_archivo, entrada_instruccion

    root = tk.Tk()
    root.title("Procesador Excel Unificado")
    root.geometry("650x330")
    root.resizable(False, False)

    # Selección de archivo
    tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=seleccionar_excel,
        width=30
    ).pack(pady=10)

    label_archivo = tk.Label(root, text="Ningún archivo seleccionado", wraplength=600)
    label_archivo.pack(pady=5)

    # Instrucción
    tk.Label(root, text="Escriba la instrucción:").pack(pady=10)

    entrada_instruccion = tk.Entry(root, width=65)
    entrada_instruccion.pack(pady=5)

    tk.Button(
        root,
        text="Ejecutar",
        command=ejecutar_instruccion,
        width=20
    ).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    iniciar_app()

