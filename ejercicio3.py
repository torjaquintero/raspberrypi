# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.3
# programa en python con tkinter con una ventana que monitorea un semaforo conectado al puerto gpio de una raspberry pi 4.
# La ventana debe tener un semaforo que cambia de color segun se activen las salidas del puerto. 
# La ventana permitira establecer modo automatico o manual.
# La secuencia del modo automatico debe ser primero el rojo 3 segundos, luego verde 4 segundos y por ultimo ambar 1 segundo.
# En el modo manual debe permitir ponerlo intermitente en rojo o intermitente en amarillo.
# ==============================================================================================

import tkinter as tk
import RPi.GPIO as GPIO
import time
from threading import Thread

class SemaforoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semaforo Control")
        self.root.geometry("300x400")

        self.estado = "Automatico"
        self.create_widgets()
        self.setup_gpio()
        self.update_semaphor()

    def create_widgets(self):
        self.label_estado = tk.Label(self.root, text="Modo: Automatico")
        self.label_estado.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=100, height=250, bg="white")
        self.canvas.pack()

        self.btn_cambiar_modo = tk.Button(self.root, text="Cambiar Modo", command=self.cambiar_modo)
        self.btn_cambiar_modo.pack(pady=10)

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        self.rojo_pin = 17  # Puedes cambiar el número del pin según tu conexión
        self.amarillo_pin = 18
        self.verde_pin = 27
        GPIO.setup(self.rojo_pin, GPIO.OUT)
        GPIO.setup(self.amarillo_pin, GPIO.OUT)
        GPIO.setup(self.verde_pin, GPIO.OUT)

    def cambiar_modo(self):
        if self.estado == "Automatico":
            self.estado = "Manual"
            self.label_estado.config(text="Modo: Manual")
        else:
            self.estado = "Automatico"
            self.label_estado.config(text="Modo: Automatico")
            self.update_semaphor()

    def update_semaphor(self):
        if self.estado == "Automatico":
            self.auto_thread = Thread(target=self.secuencia_automatica)
            self.auto_thread.start()
        elif self.estado == "Manual":
            self.encender_rojo()

    def secuencia_automatica(self):
        while self.estado == "Automatico":
            self.encender_rojo()
            time.sleep(3)
            self.apagar_todos()
            time.sleep(1)
            self.encender_verde()
            time.sleep(4)
            self.apagar_todos()
            time.sleep(1)
            self.encender_amarillo()
            time.sleep(1)
            self.apagar_todos()

    def encender_rojo(self):
        self.apagar_todos()
        GPIO.output(self.rojo_pin, GPIO.HIGH)
        self.canvas.create_oval(40, 40, 160, 160, fill="red")

    def encender_amarillo(self):
        self.apagar_todos()
        GPIO.output(self.amarillo_pin, GPIO.HIGH)
        self.canvas.create_oval(40, 40, 160, 160, fill="yellow")

    def encender_verde(self):
        self.apagar_todos()
        GPIO.output(self.verde_pin, GPIO.HIGH)
        self.canvas.create_oval(40, 40, 160, 160, fill="green")

    def apagar_todos(self):
        GPIO.output(self.rojo_pin, GPIO.LOW)
        GPIO.output(self.amarillo_pin, GPIO.LOW)
        GPIO.output(self.verde_pin, GPIO.LOW)
        self.canvas.create_oval(40, 40, 160, 160, fill="white")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SemaforoApp(tk.Tk())
    app.run()
