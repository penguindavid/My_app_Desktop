from tkinter import *
from tkinter import messagebox

# ----------------------------
# Funcciones de la app
# ----------------------------

# -----------------------------
# ventana principal de la app
# -----------------------------

ventana_principal = Tk()
ventana_principal.title("David Macías")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="ivory4")

# ----------------------------
# Frame 1
# ----------------------------
frame_1 = Frame(ventana_principal, bg="ivory3", width=780, height=240)
frame_1.place(x=10, y=10)

titulo = Label(frame_1, text="David Santiago Macías Maldonado", bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=250, y=10)

# ---------------------------
# Frame 2
# ---------------------------
frame_2 = Frame(ventana_principal, bg="ivory3",width=780, height=240)
frame_2.place(x=10, y=250)

# ---------------------------
# Metodo principal
# ---------------------------
ventana_principal.mainloop()
