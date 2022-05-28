import tkinter
from tkinter import *

def main():
#Se crea ventana
   ventana = tkinter.Tk()
   ventana.title("Monkey")
   ventana.geometry("800x600")
   ventana.config(bg="white")
   ventana.resizable(False, False) #No se puede hacer grande ni pequeño

# Se crea Canva
   my_canvas = Canvas(ventana, width=800, height=600)
   my_canvas.pack(fill="both", expand=True)


   CampoJugador = PhotoImage(file="Principal.png")
   my_canvas.create_image(0, 0, image=CampoJugador , anchor="nw")

   def salonFama():

      # Canva Registro
      canvaJuego = tkinter.Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg="lightYellow")
      canvaJuego.place(x=0, y=0)

 #Después de 5 segundos se abre el registro del jugador
   ventana.after(5000,salonFama)

   # Loop de la ventana para que se repinte
   ventana.mainloop()

#Se llama el main para que se pueda ejecutar
main()