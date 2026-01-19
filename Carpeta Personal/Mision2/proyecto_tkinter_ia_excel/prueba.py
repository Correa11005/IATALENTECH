import tkinter as tk

root = tk.Tk()
root.title("VENTANA DE PRUEBA")
root.geometry("400x300")

label = tk.Label(root, text="Tkinter funciona correctamente", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()



    