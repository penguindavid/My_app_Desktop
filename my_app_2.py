from tkinter import *

# Función para crear cada ventana secundaria con texto fijo
def pantalla_nueva(titulo, color_fondo, texto_etiqueta):
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry("500x600")
    ventana.config(bg=color_fondo)

    # Título principal
    Label(ventana, text=titulo, bg=color_fondo, fg="black", font=("Helvetica", 16)).pack(pady=10)

    # Texto fijo que puedes modificar desde el código
    Label(ventana, text=texto_etiqueta, bg=color_fondo, fg="darkblue", font=("Helvetica", 12), wraplength=460, justify=LEFT).pack(pady=20)

    # Botón para cerrar
    Button(ventana, text="Cerrar", command=ventana.destroy, font=("Helvetica", 10), bg=color_fondo).pack(pady=5)

# Funciones individuales con texto personalizado
def edad():
    pantalla_nueva("Edad y Lugar de Nacimiento", "pink",
        "Nací el 24 de marzo de 2010 en San Gil, Santander.")

def datos():
    pantalla_nueva("Datos Médicos", "lightgray",
        "o+,65 kg es mi peso, aunque no estoy del todo segurp, mi estatura es 1.65 y mi eps es la eps familiar.")

def familia():
    pantalla_nueva("Familia", "ligthcian"
        "Mi familia está compuesta por mi mama Claudia milena,mis hermanos mariana,jorge y sergio y mi padrastro sergio. Todos vivimos juntos.")

def Colegio():
    pantalla_nueva("Educación", "honeydew",
        "Estudio en el Colegio SAn Jose de Guanenta. Me gusta mucho la clase de ciencias y tengo buenos amigos en mi curso.")

def mis_amigos():
    pantalla_nueva("Amigos", "lightblue",
        "Mis amigos más cercanos son soreth, manuel y daniel diaz . auque tengo mas amigos.")

def tiempo_libre():
    pantalla_nueva("Hobbies", "lightgreen",
        "En mi tiempo libre me gusta dibujar, programar en Python y ver series de ciencia ficción.")

def Horario_semanal():
    pantalla_nueva("Horario Semanal", "blue",
        "De lunes a viernes estudio en el colegio. Los fines de semana practico programacion, doblo ropa y ayudo en mi casa.")

def Prueba_saber_2026():
    pantalla_nueva("Preparación Saber 2026", "yellow",
        "Estoy preparándome para la prueba Saber 2026 con simulacros, lecturas y clases de refuerzo en matemáticas, ademas de lecturas de los temas .")

def Mi_vida_en_2031():
    pantalla_nueva("Proyecto de Vida 2031", "gray",
        "En el año 2031 me imagino estudiando biologia y trabajndo  en desarrollo de software, ademas de creacion de videojuegos independiente.")

def Tema_libre():
    pantalla_nueva("Tema Libre", "ivory3",
        "Me encanta la serie The Walking Dead. Me gusta analizar los personajes, sus decisiones y cómo sobreviven en un mundo de zombies.")

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
