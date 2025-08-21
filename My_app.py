from tkinter import *
from tkinter import messagebox

# Función para crear cada ventana secundaria
def crear_ventana(titulo, ivory4= "ivory4"):
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry("500x600")
    ventana.config(bg=ivory4)


    Label(ventana, text=titulo, bg=ivory4, fg="black", font=("Helvetica", 16)).pack(pady=10)


    # Botón para cerrar la ventana
    Button(ventana, text="Cerrar", command=ventana.destroy, font=("Helvetica", 10), bg="ivory4").pack(pady=5)
# Funciones individuales para cada ventana
def edad(): edad("edad y lugar de nacimiento", "lightblue")
# Función para crear cada ventana secundaria
def crear_ventana(titulo, ivory4= "ivory4"):
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry("500x600")
    ventana.config(bg=ivory4)

    Label(ventana, text=titulo, bg=ivory4, fg="black", font=("Helvetica", 16)).pack(pady=10)

    # Botón para cerrar la ventana
    Button(ventana, text="Cerrar", command=ventana.destroy, font=("Helvetica", 10), bg="ivory4").pack(pady=5)

def datos(): crear_ventana("Datos Méd", "mistyrose")
def familia(): crear_ventana("Familia", "honeydew")
def Colegio(): crear_ventana("Colegio", "lavender")
def mis_amigos(): crear_ventana("Amigos", "lightcyan")
def tiempo_libre(): crear_ventana("Hobbies", "peachpuff")
def Horario_semanal(): crear_ventana("Horario Semanal", "lightgoldenrod")
def Prueba_saber_2026(): crear_ventana("Preparación Saber 2026", "thistle")
def Mi_vida_en_2031(): crear_ventana("Proyecto de Vida 2031", "azure")
def Tema_libre(): crear_ventana("TWD", "white")

# Ventana principal
ventana_principal = Tk()
ventana_principal.title("Mi App Personal - David Santiago Macías")
ventana_principal.geometry("700x400")
ventana_principal.config(bg="lightgray")
ventana_principal.resizable(False, False)

# Título principal
Label(ventana_principal, text="David Santiago Macías Maldonado", bg="pink", fg="black", font=("Helvetica", 20)).pack(pady=10)

# Frame para los botones organizados horizontalmente
frame_botones = Frame(ventana_principal, bg="ivory4")
frame_botones.pack(pady=20)

# Lista de botones con sus funciones
botones = [
    ("Nacimiento", edad),
    ("Médicos", datos),
    ("Familia", familia),
    ("Educación", Colegio),
    ("Amigos", mis_amigos),
    ("Hobbies", tiempo_libre),
    ("Horario", Horario_semanal),
    ("Saber 2026", Prueba_saber_2026),
    ("Vida 2031", Mi_vida_en_2031),
    ("TWD", Tema_libre),
]

# Crear botones en filas horizontales (2 filas de 5 botones)
for i in range(0, len(botones), 5):
    fila = Frame(frame_botones, bg="ivory4")
    fila.pack(pady=5)
    for texto, comando in botones[i:i+5]:
        Button(fila, text=texto, command=comando, font=("Helvetica", 10), width=12, height=2, bg="white").pack(side=LEFT, padx=5)

# Ejecutar la app
ventana_principal.mainloop()

