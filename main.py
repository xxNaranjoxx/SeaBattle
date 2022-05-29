import tkinter
from tkinter import *
from tkinter import messagebox

bubbleGum = "#FFBED2"
lightBlue = "#98D3E3"

def main():
#Se crea ventana
   ventana = tkinter.Tk()
   ventana.title("Monkey")
   ventana.geometry("800x600")
   ventana.config(bg="white")
   ventana.resizable(False, False) #Tamaño

   # Se crea Canva
   splashCanva = Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=lightBlue)
   splashCanva.place(x=0, y=0)

   fondoRegistro = PhotoImage(file="Computador.png")
   splashCanva.create_image(0, 0, image=fondoRegistro, anchor="nw")
print("Hola")




   def registro():
      my_canvas = Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=lightBlue)
      my_canvas.place(x=0, y=0)

      fondoRegistro = PhotoImage(file="Registro.png")
      my_canvas.create_image(0, 0, image=fondoRegistro, anchor="nw")

      nombres = Entry(my_canvas,width=50,borderwidth=3)
      nombres.place(x=195,y=290)
      #Juego


      def registroJug():
         if nombres.get() == "":
            messagebox.showwarning("Nombre", "Error en el nombre")
         else:
            messagebox.showinfo("Nombre", "Registrado")
            archivo = open("Jugadores1.txt", "a")
            archivo.write(nombres.get() + "-")
            archivo.close()
            salonFama()


      imprimirJugador = Button(my_canvas, text="Registrar y Jugar", command=registroJug) # Regsitrar y Jugar
      imprimirJugador.place(x=195, y=335)





   def salonFama():

      # Canva Registro
      canvaJuego = tkinter.Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=bubbleGum)
      canvaJuego.place(x=0, y=0)

      regresoB = Button(canvaJuego, text="Regresar al registro", command=registro)  # Salon de la fama
      regresoB.place(x=5, y=5)


   def ayuda():
      canvaAyuda = tkinter.Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg="lightYellow")
      canvaAyuda.place(x=0, y=0)


   salonFamaB = Button(my_canvas, text="Salon de la fama", command=salonFama)  # Salon de la fama
   salonFamaB.place(x=5, y=5)
   ayudaB = Button(my_canvas, text="Ayuda", command=ayuda)  # Ayuda
   ayudaB.place(x=110, y=5)

   ventana.after(5000,registro)

   ventana.mainloop() # loop para main



main()# Llamado de main