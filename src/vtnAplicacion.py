from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from lstCircular import *
from matriz import *
from archivo import *
from PIL import Image
from PIL import ImageTk




class Principal(ttk.Frame):

    def __init__(self,main_window):
        super().__init__(ventana)

        self.opcion=0

        ventana.title("Matrices")

        pnlMenu=Frame(ventana,height=760,width=225,bg="#282c34")
        pnlMenu.place(x=0,y=0)

        self.lg=Image.open('imagen/logo.png')
        self.lg=ImageTk.PhotoImage(self.lg)

        btnLogo=Button(pnlMenu, image=self.lg,
                          height=40,width=295,
                          compound="left",
                          justify="center",
                          bg="#282c34",
                          relief="flat",
                          borderwidth="2",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2"
                          )
        btnLogo.place(x=-100,y=2)


        self.img=Image.open('imagen/abrir.png')
        #self.img=self.img.resize((55,40),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(self.img)
        #self.img.place(x=5,y=50)


        btnArchivo=Button(pnlMenu, image=self.img,text="Cargar Archivo",
                          height=37,width=295,
                          compound="left",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          borderwidth="2",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.cargarArchivo)
        btnArchivo.place(x=-65,y=50)
        self.img1=Image.open('imagen/mat1.png')
        #self.img=self.img.resize((55,40),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(self.img1)

        btnOperacion=Button(pnlMenu,image=self.img1,text="Operacion con una matriz",
                          height=37,width=255,
                          compound="left",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.cargarArchivo)
        btnOperacion.place(x=-17,y=98)

        self.img2=Image.open('imagen/mat2.png')
        #self.img=self.img.resize((55,40),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(self.img2)

        btnOperacion2=Button(pnlMenu,image=self.img2,text="Operacion con dos matrices",
                          height=37,width=238,
                          compound="left",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.cargarArchivo)
        btnOperacion2.place(x=-5,y=146)
        self.img3=Image.open('imagen/reporte.png')
        #self.img=self.img.resize((55,40),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(self.img3)

        btnReporte=Button(pnlMenu,image=self.img3,text="Reporte",
                          height=37,width=310,
                          compound="left",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.cargarArchivo)
        btnReporte.place(x=-95,y=194)
        self.img4=Image.open('imagen/ayuda.png')
        #self.img=self.img.resize((55,40),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(self.img4)
        btnAyuda=Button(pnlMenu,image=self.img4,text="Ayuda",
                          height=37,width=320,
                          compound="left",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.cargarArchivo)
        btnAyuda.place(x=-103,y=242)



        self.pnlPrincipal=Frame(ventana,height=760,width=1024,bg="#21252b")
        pnlMenu.grid(row=0,column=250)


        self.cmbMatriz1=ttk.Combobox(self.pnlPrincipal)
        self.cmbMatriz2=ttk.Combobox(self.pnlPrincipal)


        self.btnVisualizar=Button(self.pnlPrincipal,text="Visualizar Matriz",bg="#2f333d",
                      relief="flat",
                      foreground="#787e8c",
                      activeforeground="#FFFFFF",
                      activebackground="#282c34",
                      overrelief="flat",
                      cursor="hand2",
                      command=self.visualizarMatriz
                      )



        pnlMenu.pack(side=LEFT)
        self.pnlPrincipal.pack()
        ventana.mainloop()

        #main_window.config(menu=barraMenu)
        #main_window.configure(width=600,height=200)
        #self.place(width=600,height=200)

    def item_seleccionado(self):
        #item=self.combo.get()
        print("Usted eligio ",item)
    def rotarHorizontal(self):
        item=self.lstMatriz1.get()
        messagebox.showinfo(message="hola",title="info")

    def union(self):
        self.limpliarPantalla()
        self.lstMatriz2["values"]=["matriz1","matriz2","matriz3"]
        self.lstMatriz2.place(x=200,y=50)
    def limpliarPantalla(self):
        self.lstMatriz1=ttk.Combobox(self)
        self.lstMatriz2=ttk.Combobox(self)

    def cargarArchivo(self):
        rutaArchivo=filedialog.askopenfilename(initialdir="logica",title="Abrir archivo")
        self.listaMat=Lista()
        self.archivo=Archivo()

        self.archivo.abrir(rutaArchivo)

        self.listaMat=self.archivo.listaMatriz
        self.lblMatriz1=Label(self.pnlPrincipal,text="Elija una matriz =")
        self.lblMatriz1.config(font=("Verdana",14),
                                bg="#21252b",
                                fg="#787e8c" )
        self.lblMatriz1.place(x=20,y=45)

        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            values = list(self.cmbMatriz1["values"])
            self.cmbMatriz1["values"] = values + [dato.nombre]
        self.cmbMatriz1.place(x=200,y=50)
        self.btnVisualizar.place(x=350,y=50)

        self.opcion=1

        messagebox.showinfo(message="Archivo Cargado Exitosamente",title="Informacion")

    def visualizarMatriz(self):
        opcion=self.opcion

        arch=Archivo()

        if(opcion==1):
            nombre=self.cmbMatriz1.get()

            for i in range(1,self.listaMat.tamano+1):
                dato=self.listaMat.getDato(i)
                if(dato.nombre==nombre):
                    break

            arch.graficarProy(dato,0)

            self.imgMat1=Image.open('imagen/'+nombre+'.png')
            self.imgMat1=self.imgMat1.resize((350,350),Image.ANTIALIAS)
            self.imgMat1=ImageTk.PhotoImage(self.imgMat1)

            self.Mat1=Label(self.pnlPrincipal,text=nombre,
                            image=self.imgMat1,
                            compound="top")

            self.Mat1.image=self.imgMat1
            self.Mat1.place(x=225,y=100)
            #elf.imgMat1.place(x=400,y=150)

            #Graficar imagen 2
            """
            self.imgMat2=Image.open('imagen/'+nombre+'.png')
            self.imgMat2=self.imgMat2.resize((225,225),Image.ANTIALIAS)
            self.imgMat2=ImageTk.PhotoImage(self.imgMat2)

            self.Mat2=Label(self.pnlPrincipal,text=nombre,
                            image=self.imgMat2,
                            compound="top")
            self.Mat2.image=self.imgMat2
            self.Mat2.place(x=300,y=125)
            """



ventana=tk.Tk()
app=Principal(ventana)
app.mainloop()
