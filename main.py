import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

bubbleGum = "#FFBED2"
lightBlue = "#98D3E3"



class balas():
   def __init__(self):
      posX = self.posX
      posY = self.posY

class barco():
   def __init__(self,tamano,posx, posy):
      self.tamano = tamano
      self.posx = posx
      self.posy = posy

   def  get_tamano(self):
      return self.tamano

   def  get_posx(self):
      return self.posx

   def  get_posy(self):
      return self.posy

   def  set_posy(self):
      return self.posy

   def  set_posy(self):
      return self.posy

   def  set_posy(self, x):
      self.posy = x



class Juego():
   def __init__(self, l_cuadrado):
      self.l_cuadrado = l_cuadrado

      self.ventana = tkinter.Tk()
      self.ventana.title("Juego")
      self.ventana.wm_geometry(f"{str(l_cuadrado * 10)}x{str(l_cuadrado * 10)}")
      self.ventana.resizable(0,0)

      self.ventana1 = tkinter.Tk()
      self.ventana1.title("Juego")
      self.ventana1.wm_geometry(f"{str(l_cuadrado * 10)}x{str(l_cuadrado * 10)}")
      self.ventana1.resizable(0, 0)

      self.interfaz1 = tkinter.Canvas(self.ventana1)
      self.interfaz1.pack(fill="both", expand=True)

      self.interfaz = tkinter.Canvas(self.ventana)
      self.interfaz.pack(fill="both", expand=True)

   def __call__(self):
      self.ventana.mainloop()

   def dibujoTableroJ(self):
      #self.interfaz.create_rectangle(x0,y0,x1,y1,fill=null)
      for i in range(10):
         for j in range(10):
            self.interfaz.create_rectangle(i * self.l_cuadrado,j * self.l_cuadrado,(i + 1) * self.l_cuadrado,(j + 1) * self.l_cuadrado,fill="white")

   def dibujoTableroC(self):
      #self.interfaz.create_rectangle(x0,y0,x1,y1,fill=null)
      for i in range(10):
         for j in range(10):
            self.interfaz1.create_rectangle(i * self.l_cuadrado,j * self.l_cuadrado,(i + 1) * self.l_cuadrado,(j + 1) * self.l_cuadrado,fill="red")




def main():
#Se crea ventana
   ventana = tkinter.Tk()
   ventana.title("SeaBattle")
   ventana.geometry("800x600")
   ventana.config(bg="white")
   ventana.resizable(False, False) #Tamaño

   def paso():
      while barraProgreso["value"] != 100:
         for x in range(5):
            barraProgreso["value"] += 20
            splashCanva.update_idletasks()
            time.sleep(1)
      registro()


   # Se crea Canva
   splashCanva = Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=lightBlue)
   splashCanva.place(x=0, y=0)

   fondoSplash = PhotoImage(file="Splash.png")
   splashCanva.create_image(0, 0, image=fondoSplash, anchor="nw")


   barraProgreso = ttk.Progressbar(splashCanva, orient=HORIZONTAL, length = 780, mode = "determinate")
   barraProgreso.place(x=10, y=575)

   botonBarra = Button(splashCanva, text="Entrar al Juego",font=("Cooper black", 15), command=paso)  # Salon de la fama
   botonBarra.place(x=320 , y=299)



   def registro():
      my_canvas = Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=lightBlue)
      my_canvas.place(x=0, y=0)

      pideNombre = tkinter.Label(my_canvas, text="Registro ", font=("Cooper black", 40),bg=lightBlue, fg="black")
      pideNombre.place(x=250, y=60)

      pideNombre = tkinter.Label(my_canvas, text="Nombre del jugador: ", font=("Cooper black", 20), bg=lightBlue,fg="black")
      pideNombre.place(x=195, y=240)

      nombres = Entry(my_canvas, width=50, borderwidth=3)
      nombres.place(x=195, y=290)

      salonFamaB = Button(my_canvas, text="Salon de la fama", command=salonFama)  # Salon de la fama
      salonFamaB.place(x=5, y=5)

      ayudaB = Button(my_canvas, text="Ayuda", command=ayuda)  # Ayuda
      ayudaB.place(x=110, y=5)


      def registroJug():

         if nombres.get() == "":
            messagebox.showwarning("Nombre", "Error en el nombre")
         else:
            messagebox.showinfo("Nombre", "Registrado")
            archivo = open("Jugadores1.txt", "a")
            archivo.write(nombres.get() + "-")
            archivo.close()
            Leerjuego()

      imprimirJugador = Button(my_canvas, text="Registrar y Jugar", command=registroJug) # Regsitrar y Jugar
      imprimirJugador.place(x=195, y=335)



   def salonFama():

      # Canva Registro
      canvaSF = tkinter.Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg=bubbleGum)
      canvaSF.place(x=0, y=0)

      pideNombre = tkinter.Label(canvaSF, text="Salon de la fama ", font=("Cooper black", 40), bg=lightBlue, fg="black")
      pideNombre.place(x=250, y=60)

      salonFamaSFB = Button(canvaSF, text="Salon de la fama", command=salonFama)  # Salon de la fama
      salonFamaSFB.place(x=5, y=5)

      ayudaSFB = Button(canvaSF, text="Ayuda", command=ayuda)  # Ayuda
      ayudaSFB.place(x=110, y=5)

      registroSFB = Button(canvaSF, text="Registro", command=registro)  # Ayuda
      registroSFB.place(x=160, y=5)


   def ayuda():
      canvaAyuda = tkinter.Canvas(ventana, width=800, height=600, borderwidth=0, highlightthickness=0, bg="lightYellow")
      canvaAyuda.place(x=0, y=0)

      pideNombre = tkinter.Label(canvaAyuda, text="Ayuda ", font=("Cooper black", 40), bg=lightBlue, fg="black")
      pideNombre.place(x=250, y=60)

      salonFamaAB = Button(canvaAyuda, text="Salon de la fama", command=salonFama)  # Salon de la fama
      salonFamaAB.place(x=5, y=5)

      ayudaAB = Button(canvaAyuda, text="Ayuda", command=ayuda)  # Ayuda
      ayudaAB.place(x=110, y=5)

      registroAB = Button(canvaAyuda, text="Registro", command=registro)  # Ayuda
      registroAB.place(x=160, y=5)

   def Leerjuego():
      personaJuego = Juego(40)
      personaJuego.dibujoTableroJ()
      personaJuego.dibujoTableroC()
      personaJuego()





   ventana.mainloop() # loop para main

main()# Llamado de main