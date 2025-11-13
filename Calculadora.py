import tkinter as tk
from tkinter import font


class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x600")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#1e1e2e")

        self.expresion = ""
        self.texto_entrada = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame para la pantalla
        frame_pantalla = tk.Frame(self.ventana, bg="#1e1e2e", height=150)
        frame_pantalla.pack(fill=tk.BOTH, padx=20, pady=20)

        # Pantalla de resultados
        fuente_pantalla = font.Font(family="Arial", size=32, weight="bold")
        pantalla = tk.Entry(
            frame_pantalla,
            textvariable=self.texto_entrada,
            font=fuente_pantalla,
            justify="right",
            bd=0,
            bg="#2d2d44",
            fg="white",
            insertbackground="white"
        )
        pantalla.pack(fill=tk.BOTH, expand=True, ipady=20, padx=10, pady=10)

        # Frame para los botones
        frame_botones = tk.Frame(self.ventana, bg="#1e1e2e")
        frame_botones.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Configuración de botones
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]

        # Colores de botones
        color_numero = "#3d3d5c"
        color_operador = "#5e5ce6"
        color_especial = "#ff6b6b"
        color_igual = "#4ecca3"

        fuente_boton = font.Font(family="Arial", size=18, weight="bold")

        for i, fila in enumerate(botones):
            frame_botones.grid_rowconfigure(i, weight=1)
            for j, boton in enumerate(fila):
                frame_botones.grid_columnconfigure(j, weight=1)

                # Determinar color del botón
                if boton == 'C':
                    color = color_especial
                elif boton == '=':
                    color = color_igual
                elif boton in ['/', '*', '-', '+', '%', '⌫', '±']:
                    color = color_operador
                else:
                    color = color_numero

                btn = tk.Button(
                    frame_botones,
                    text=boton,
                    font=fuente_boton,
                    bg=color,
                    fg="white",
                    activebackground=color,
                    activeforeground="white",
                    bd=0,
                    command=lambda x=boton: self.click_boton(x)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)

                # Efecto hover
                btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=self.ajustar_color(c)))
                btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

    def ajustar_color(self, color):
        # Hacer el color un poco más claro para el efecto hover
        return color.replace("3d", "4d").replace("5e", "6e").replace("ff", "ff").replace("4e", "5e")

    def click_boton(self, valor):
        if valor == 'C':
            self.expresion = ""
            self.texto_entrada.set("")

        elif valor == '⌫':
            self.expresion = self.expresion[:-1]
            self.texto_entrada.set(self.expresion)

        elif valor == '=':
            try:
                resultado = str(eval(self.expresion))
                self.texto_entrada.set(resultado)
                self.expresion = resultado
            except ZeroDivisionError:
                self.texto_entrada.set("Error: División por 0")
                self.expresion = ""
            except:
                self.texto_entrada.set("Error")
                self.expresion = ""

        elif valor == '±':
            if self.expresion:
                try:
                    if self.expresion[0] == '-':
                        self.expresion = self.expresion[1:]
                    else:
                        self.expresion = '-' + self.expresion
                    self.texto_entrada.set(self.expresion)
                except:
                    pass

        else:
            self.expresion += str(valor)
            self.texto_entrada.set(self.expresion)


def main():
    ventana = tk.Tk()
    calculadora = Calculadora(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()

