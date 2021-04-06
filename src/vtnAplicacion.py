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
        self.estaAbierto1=False
        self.estaAbierto2=False
        self.estaVisualizado=False
        self.estaVisualizado2=False
        self.esOpe2=False

        self.abHtml=Archivo()
        self.abHtml.abrirHtmlOperacion()

        self.error=Archivo()
        self.error.abrirHtmlErrores()

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
                          command=self.oprMatriz)
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
                          command=self.oprMatriz20)
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
                          command=self.genReporte)
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
                          command=self.datosEstudiante)
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
    ### Limpiar la Pantalla o Panel pnlPrincipal

    def limpiarPantalla(self,codigo):
        if(codigo==1):
            self.btnOperacion1.destroy()
            self.btnOperacion2.destroy()
            self.btnOperacion3.destroy()
            self.btnOperacion4.destroy()
            self.btnOperacion5.destroy()
            self.btnOperacion6.destroy()
            self.btnOperacion7.destroy()
            self.btnOperacion8.destroy()

            self.dFila.destroy()
            self.hFila.destroy()
            self.dColumna.destroy()
            self.hColumna.destroy()

            self.dFilaH.destroy()
            self.dColumnaH.destroy()
            self.hColumnaEH.destroy()

            self.dFilaV.destroy()
            self.dColumnaV.destroy()
            self.hColumnaEV.destroy()

            self.dFilaR.destroy()
            self.hFilaR.destroy()
            self.dColumnaR.destroy()
            self.hColumnaR.destroy()

            self.dFilaT.destroy()
            self.hFilaT.destroy()
            self.dColumnaT.destroy()
            self.hColumnaT.destroy()

            self.etiBorrar=Label(self.pnlPrincipal)
            self.etiBorrar.config(bg="#21252b",width="775",height="350")
            self.etiBorrar.place(x=25,y=100)

            if(self.estaVisualizado==True):
                self.Mat1.destroy()
                self.estaVisualizado=False

            if(self.estaVisualizado2==True):
                self.Mat2.destroy()
                self.estaVisualizado2=False

            self.estaVisualizado=False
            self.estaVisualizado2=False
            self.estaAbierto1=False

        if(codigo==2):

            self.btnOperacion21.destroy()
            self.btnOperacion22.destroy()
            self.btnOperacion23.destroy()
            self.btnOperacion24.destroy()

            self.etiBorrar=Label(self.pnlPrincipal)
            self.etiBorrar.config(bg="#21252b",width="800",height="350")
            self.etiBorrar.place(x=20,y=85)



            self.estaAbierto2=False


        self.lstMatriz1=ttk.Combobox(self)
        self.lstMatriz2=ttk.Combobox(self)

###     Cargar Archivo   ###

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

###     Visualizar Matriz Archivo   ###

    def visualizarMatriz(self):

        self.estaVisualizado=True

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
            if(self.esOpe2==True):
                self.imgMat1=self.imgMat1.resize((240,240),Image.ANTIALIAS)
            else:
                self.imgMat1=self.imgMat1.resize((350,350),Image.ANTIALIAS)

            self.imgMat1=ImageTk.PhotoImage(self.imgMat1)

            self.Mat1=Label(self.pnlPrincipal,text=nombre,
                            image=self.imgMat1,
                            compound="top")

            self.Mat1.image=self.imgMat1

            if(self.esOpe2==True):
                self.Mat1.place(x=10,y=150)
            else:
                self.Mat1.place(x=25,y=100)



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

    def visualizarMatriz2(self):

        #self.estaVisualizado=True

        opcion=self.opcion

        arch=Archivo()

        if(opcion==1):
            nombre=self.cmbMatriz2.get()

            for i in range(1,self.listaMat2.tamano+1):
                dato=self.listaMat2.getDato(i)
                if(dato.nombre==nombre):
                    break

            arch.graficarProy(dato,0)

            self.imgMat2=Image.open('imagen/'+nombre+'.png')
            self.imgMat2=self.imgMat2.resize((240,240),Image.ANTIALIAS)
            self.imgMat2=ImageTk.PhotoImage(self.imgMat2)

            self.Mat2=Label(self.pnlPrincipal,text=nombre,
                            image=self.imgMat2,
                            compound="top")
            self.Mat2.image=self.imgMat2
            self.Mat2.place(x=260,y=150)
            #elf.imgMat1.place(x=400,y=150)

            #Graficar imagen 2
            """
            self.imgMatR=Image.open('imagen/'+nombre+'.png')
            self.imgMatR=self.imgMat2.resize((225,225),Image.ANTIALIAS)
            self.imgMatR=ImageTk.PhotoImage(self.imgMat2)

            self.Mat2=Label(self.pnlPrincipal,text=nombre,
                            image=self.imgMat2,
                            compound="top")
            self.Mat2.image=self.imgMat2
            self.Mat2.place(x=300,y=125)
            """
###     Metodos para los botones del menu  ###
    def oprMatriz(self):
        self.botonOperacion(1)


    def oprMatriz20(self):

        if(self.estaAbierto1==True):
            self.limpiarPantalla(1)

        self.esOpe2=True

        self.listaMat2=Lista()
        self.listaMat2=self.listaMat

        self.lblMatriz2=Label(self.pnlPrincipal,text="Elija una matriz =")
        self.lblMatriz2.config(font=("Verdana",14),
                                bg="#21252b",
                                fg="#787e8c" )
        self.lblMatriz2.place(x=20,y=90)

        self.cmbMatriz2=ttk.Combobox(self.pnlPrincipal)

        for i in range(1,self.listaMat2.tamano+1):
            dato=self.listaMat2.getDato(i)
            values = list(self.cmbMatriz2["values"])
            self.cmbMatriz2["values"] = values + [dato.nombre]
        self.cmbMatriz2.place(x=200,y=90)


        self.btnVisualizar2=Button(self.pnlPrincipal,text="Visualizar Matriz",bg="#2f333d",
                      relief="flat",
                      foreground="#787e8c",
                      activeforeground="#FFFFFF",
                      activebackground="#282c34",
                      overrelief="flat",
                      cursor="hand2",
                      command=self.visualizarMatriz2
                      )
        self.btnVisualizar2.place(x=350,y=90)

        self.botonOperacion2()

### Botones para la Operacion con una Matriz    ###

    def botonOperacion(self,codigo):
        if(self.estaAbierto2==True):
            self.limpiarPantalla(2)

        self.estaAbierto1=True
        self.esOpe2=False
        self.lstBotones=Lista()

        nombre="Rotar\nHorizontal"
        self.imgGh=Image.open('imagen/gHor.png')
        self.imgGh=ImageTk.PhotoImage(self.imgGh)

        self.btnOperacion1=Button(self.pnlPrincipal,image=self.imgGh,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz1)
        self.btnOperacion1.place(x=30,y=550)
        nombre="Rotar\nVertical"
        self.imgGv=Image.open('imagen/gVer.png')
        self.imgGv=ImageTk.PhotoImage(self.imgGv)

        self.btnOperacion2=Button(self.pnlPrincipal,image=self.imgGv,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz2)
        self.btnOperacion2.place(x=122,y=550)

        nombre="Transpuesta\n "
        self.imgT=Image.open('imagen/matT.png')
        self.imgT=ImageTk.PhotoImage(self.imgT)

        self.btnOperacion3=Button(self.pnlPrincipal,image=self.imgT,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz3)
        self.btnOperacion3.place(x=214,y=550)

        nombre="Limpiar\nZona"
        x1=260
        y1=450
        ancho="5"

        self.etiqueta("Fil",310,475)
        self.dFila=Entry(self.pnlPrincipal,width=ancho)
        self.dFila.insert(0,"Desde")
        self.dFila.place(x=50+x1,y=50+y1)

        self.hFila=Entry(self.pnlPrincipal,width=ancho)
        self.hFila.insert(0,"Hasta")
        self.hFila.place(x=50+x1,y=75+y1)

        self.etiqueta("Col",350,475)
        self.dColumna=Entry(self.pnlPrincipal,width=ancho)
        self.dColumna.insert(0,"Desde")
        self.dColumna.place(x=90+x1,y=50+y1)

        self.hColumna=Entry(self.pnlPrincipal,width=ancho)
        self.hColumna.insert(0,"Hasta")
        self.hColumna.place(x=90+x1,y=75+y1)


        self.imgLim=Image.open('imagen/lMat.png')
        self.imgLim=ImageTk.PhotoImage(self.imgLim)
        self.btnOperacion4=Button(self.pnlPrincipal,image=self.imgLim,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz4)
        self.btnOperacion4.place(x=306,y=550)

        nombre="Agregar\nLinea Horizontal"
        x1=352
        y1=450
        ancho="5"

        self.etiqueta("Fil",402,475)
        self.dFilaH=Entry(self.pnlPrincipal,width=ancho)
        self.dFilaH.place(x=50+x1,y=50+y1)

        self.etiqueta("nEl",402,525)

        self.etiqueta("Col",442,475)
        self.dColumnaH=Entry(self.pnlPrincipal,width=ancho)
        self.dColumnaH.place(x=90+x1,y=50+y1)

        self.hColumnaEH=Entry(self.pnlPrincipal,width=ancho)
        self.hColumnaEH.place(x=90+x1,y=75+y1)

        self.imgLhor=Image.open('imagen/LHor.png')
        self.imgLhor=ImageTk.PhotoImage(self.imgLhor)
        self.btnOperacion5=Button(self.pnlPrincipal,image=self.imgLhor,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz5)
        self.btnOperacion5.place(x=398,y=550)
        nombre="Agregar\nLinea vertical"

        x1=444
        y1=450
        ancho="5"
        self.etiqueta("Fil",494,475)
        self.dFilaV=Entry(self.pnlPrincipal,width=ancho)
        self.dFilaV.place(x=50+x1,y=50+y1)

        self.etiqueta("nEl",494,525)

        self.etiqueta("Col",534,475)
        self.dColumnaV=Entry(self.pnlPrincipal,width=ancho)
        self.dColumnaV.place(x=90+x1,y=50+y1)

        self.hColumnaEV=Entry(self.pnlPrincipal,width=ancho)
        self.hColumnaEV.place(x=90+x1,y=75+y1)


        self.imgLver=Image.open('imagen/LVer.png')
        self.imgLver=ImageTk.PhotoImage(self.imgLver)
        self.btnOperacion6=Button(self.pnlPrincipal,image=self.imgLver,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz6)
        self.btnOperacion6.place(x=490,y=550)

        nombre="Agregar\nRectangulo"

        x1=536
        y1=450
        ancho="5"

        self.etiqueta("Fil",586,475)
        self.dFilaR=Entry(self.pnlPrincipal,width=ancho)
        self.dFilaR.insert(0,"Desde")
        self.dFilaR.place(x=50+x1,y=50+y1)

        self.hFilaR=Entry(self.pnlPrincipal,width=ancho)
        self.hFilaR.insert(0,"Hasta")
        self.hFilaR.place(x=50+x1,y=75+y1)

        self.etiqueta("Col",626,475)
        self.dColumnaR=Entry(self.pnlPrincipal,width=ancho)
        self.dColumnaR.insert(0,"Desde")
        self.dColumnaR.place(x=90+x1,y=50+y1)

        self.hColumnaR=Entry(self.pnlPrincipal,width=ancho)
        self.hColumnaR.insert(0,"Hasta")
        self.hColumnaR.place(x=90+x1,y=75+y1)



        self.imgRec=Image.open('imagen/rect.png')
        self.imgRec=ImageTk.PhotoImage(self.imgRec)
        self.btnOperacion7=Button(self.pnlPrincipal,image=self.imgRec,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz7)
        self.btnOperacion7.place(x=582,y=550)

        nombre="Agregar\nTriangulo"

        x1=628
        y1=450
        ancho="5"

        self.etiqueta("Fil",678,475)
        self.dFilaT=Entry(self.pnlPrincipal,width=ancho)
        self.dFilaT.insert(0,"Desde")
        self.dFilaT.place(x=50+x1,y=50+y1)

        self.hFilaT=Entry(self.pnlPrincipal,width=ancho)
        self.hFilaT.insert(0,"Hasta")
        self.hFilaT.place(x=50+x1,y=75+y1)

        self.etiqueta("Col",718,475)
        self.dColumnaT=Entry(self.pnlPrincipal,width=ancho)
        self.dColumnaT.insert(0,"Desde")
        self.dColumnaT.place(x=90+x1,y=50+y1)

        self.hColumnaT=Entry(self.pnlPrincipal,width=ancho)
        self.hColumnaT.insert(0,"Hasta")
        self.hColumnaT.place(x=90+x1,y=75+y1)



        self.imgTri=Image.open('imagen/tRec.png')
        self.imgTri=ImageTk.PhotoImage(self.imgTri)
        self.btnOperacion8=Button(self.pnlPrincipal,image=self.imgTri,text=nombre,
                          height=100,width=75,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz8)
        self.btnOperacion8.place(x=674,y=550)


### Botones para la Operacion con una Matriz    ###

    def botonOperacion2(self):



        self.estaAbierto2=True
        separacion=50
        nombre="Union"
        self.imgUn=Image.open('imagen/union.png')
        self.imgUn=ImageTk.PhotoImage(self.imgUn)
        self.btnOperacion21=Button(self.pnlPrincipal,image=self.imgUn,text=nombre,
                          height=100,width=125,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz21)
        self.btnOperacion21.place(x=50+separacion,y=550)
        separacion+=150

        nombre="Interseccion"
        self.imgInt=Image.open('imagen/interseccion.png')
        self.imgInt=ImageTk.PhotoImage(self.imgInt)
        self.btnOperacion22=Button(self.pnlPrincipal,image=self.imgInt,text=nombre,
                          height=100,width=125,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz22)
        self.btnOperacion22.place(x=50+separacion,y=550)
        separacion+=150

        nombre="Diferencia"
        self.imgDi=Image.open('imagen/diferencia.png')
        self.imgDi=ImageTk.PhotoImage(self.imgDi)
        self.btnOperacion23=Button(self.pnlPrincipal,image=self.imgDi,text=nombre,
                          height=100,width=125,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz23)
        self.btnOperacion23.place(x=50+separacion,y=550)
        separacion+=150

        nombre="Diferencia Simetrica"
        self.imgDifSim=Image.open('imagen/difSimetrica.png')
        self.imgDifSim=ImageTk.PhotoImage(self.imgDifSim)
        self.btnOperacion24=Button(self.pnlPrincipal,image=self.imgDifSim,text=nombre,
                          height=100,width=125,
                          compound="top",
                          justify="center",
                          bg="#2f333d",
                          relief="flat",
                          foreground="#787e8c",
                          activeforeground="#FFFFFF",
                          activebackground="#282c34",
                          overrelief="flat",
                          cursor="hand2",
                          command=self.oprMatriz24)
        self.btnOperacion24.place(x=50+separacion,y=550)
        separacion+=150



####   Operaciones con una matriz  ####

    def oprMatriz1(self):
        #messagebox.showinfo(message=self.btnOperacion1.cget("text") +" "+ self.cmbMatriz1.get(),title="Informacion")
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        #messagebox.showinfo(message=nombre,title="Informacion")
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        arch.graficarProy(dato,1)



        self.imgMat2=Image.open('imagen/'+nombre+"G.Horizontal"+'.png')
        self.imgMat2=self.imgMat2.resize((350,350),Image.ANTIALIAS)
        self.imgMat2=ImageTk.PhotoImage(self.imgMat2)
        self.Mat2=Label(self.pnlPrincipal,text=nombre+"G.Horizontal",
                        image=self.imgMat2,
                        compound="top")

        self.Mat2.image=self.imgMat2
        self.Mat2.place(x=400,y=100)

        self.abHtml.datosHtmlOperacion(self.btnOperacion1.cget("text"),nombre)
        messagebox.showinfo(message=self.btnOperacion1.cget("text"),title="Informacion")

         #print(self.cmbMatriz1.get())

    def imgOperacion(self,nombre):
        self.estaVisualizado2=True

        self.imgMat2=Image.open('imagen/'+nombre+'.png')
        self.imgMat2=self.imgMat2.resize((350,350),Image.ANTIALIAS)
        self.imgMat2=ImageTk.PhotoImage(self.imgMat2)
        self.Mat2=Label(self.pnlPrincipal,text=nombre,
                        image=self.imgMat2,
                        compound="top")
        self.Mat2.image=self.imgMat2
        self.Mat2.place(x=400,y=100)


    def imgOperacionR(self,nombre):
        self.estaVisualizado2=True

        self.imgMatR=Image.open('imagen/'+nombre+'.png')
        self.imgMatR=self.imgMatR.resize((240,240),Image.ANTIALIAS)
        self.imgMatR=ImageTk.PhotoImage(self.imgMatR)
        self.MatR=Label(self.pnlPrincipal,text=nombre,
                        image=self.imgMatR,
                        compound="top")
        self.MatR.image=self.imgMatR
        self.MatR.place(x=515,y=150)



    def oprMatriz2(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        #messagebox.showinfo(message=nombre,title="Informacion")
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        arch.graficarProy(dato,2)
        nombre=nombre+"G.Vertical"
        self.imgOperacion(nombre)
        self.abHtml.datosHtmlOperacion(self.btnOperacion2.cget("text"),nombre)
        messagebox.showinfo(message=self.btnOperacion2.cget("text"),title="Informacion")

    def oprMatriz3(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        arch.graficarProy(dato,3)
        nombre=nombre+"Transpuesta"
        self.imgOperacion(nombre)
        self.abHtml.datosHtmlOperacion(self.btnOperacion3.cget("text"),nombre)
        messagebox.showinfo(message=self.btnOperacion3.cget("text"),title="Informacion")

    def oprMatriz4(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        dFila=int(self.dFila.get())
        dColumna=int(self.dColumna.get())
        hFila=int(self.hFila.get())
        hColumna=int(self.hColumna.get())

        if(dFila>int(dato.fila)):
            self.error.datosHtmlErrores(self.btnOperacion4.cget("text"),nombre,"Valor incorrecto de Fila Desde \nEs mayor")
            messagebox.showinfo(message="Valor incorrecto de Fila Desde \nEs mayor",title="Informacion")
        else:
            if(dColumna>int(dato.columna)):
                self.error.datosHtmlErrores(self.btnOperacion4.cget("text"),nombre,"Valor incorrecto de Columna Desde \nEs mayor")
                messagebox.showinfo(message="Valor incorrecto de Columna Desde \nEs mayor",title="Informacion")
            else:
                if(hFila>int(dato.fila)):
                    self.error.datosHtmlErrores(self.btnOperacion4.cget("text"),nombre,"Valor incorrectos de Fila Hasta \nEs mayor")
                    messagebox.showinfo(message="Valor incorrectos de Fila Hasta \nEs mayor",title="Informacion")
                else:
                    if(hColumna>int(dato.columna)):
                        self.error.datosHtmlErrores(self.btnOperacion4.cget("text"),nombre,"Valor incorrecto de Columna Hasta \nEs mayor")
                        messagebox.showinfo(message="Valor incorrecto de Columna Hasta \nEs mayor",title="Informacion")
                    else:
                        arch.graficarRellenarArea(0,dato,dFila,hFila,dColumna,hColumna)
                        nombre=nombre+"Limpiar"
                        self.imgOperacion(nombre)
                        self.abHtml.datosHtmlOperacion(self.btnOperacion4.cget("text"),nombre)
                        messagebox.showinfo(message=self.btnOperacion4.cget("text"),title="Informacion")

    def oprMatriz5(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        Fila=int(self.dFilaH.get())
        Columna=int(self.dColumnaH.get())
        nElementos=int(self.hColumnaEH.get())

        if(Fila>int(dato.fila)):
            self.error.datosHtmlErrores(self.btnOperacion5.cget("text"),nombre,"Valor incorrecto de Fila Desde \nEs mayor")
            messagebox.showinfo(message="Valor incorrecto de Fila Desde \nEs mayor",title="Informacion")
        else:
            if(Columna>int(dato.columna)):
                self.error.datosHtmlErrores(self.btnOperacion5.cget("text"),nombre,"Valor incorrecto de Columna Desde \nEs mayor")
                messagebox.showinfo(message="Valor incorrecto de Columna Desde \nEs mayor",title="Informacion")
            else:
                if(nElementos>int(dato.columna)):
                    self.error.datosHtmlErrores(self.btnOperacion5.cget("text"),nombre,"Valor incorrectos de elmentos es mayor ")
                    messagebox.showinfo(message="El numero de elementos \nEs mayor a las columnas",title="Informacion")
                else:
                    arch.graficarRellenarArea(1,dato,Fila,Columna,nElementos,0)
                    nombre=nombre+"LineaHorizontal"
                    self.imgOperacion(nombre)
                    self.abHtml.datosHtmlOperacion(self.btnOperacion5.cget("text"),nombre)
                    messagebox.showinfo(message=self.btnOperacion5.cget("text"),title="Informacion")
    def oprMatriz6(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        Fila=int(self.dFilaV.get())
        Columna=int(self.dColumnaV.get())
        nElementos=int(self.hColumnaEV.get())

        if(Fila>int(dato.fila)):
            self.error.datosHtmlErrores(self.btnOperacion6.cget("text"),nombre,"Valor incorrecto de Fila Desde \nEs mayor")
            messagebox.showinfo(message="Valor incorrecto de Fila Desde \nEs mayor",title="Informacion")
        else:
            if(Columna>int(dato.columna)):
                self.error.datosHtmlErrores(self.btnOperacion6.cget("text"),nombre,"Valor incorrecto de Columna Desde \nEs mayor")
                messagebox.showinfo(message="Valor incorrecto de Columna Desde \nEs mayor",title="Informacion")
            else:
                if(nElementos>int(dato.fila)):
                    self.error.datosHtmlErrores(self.btnOperacion6.cget("text"),nombre,"Valor incorrectos de Fila Hasta \nEs mayor")
                    messagebox.showinfo(message="El numero de elementos \nEs mayor a las filas",title="Informacion")
                else:
                    arch.graficarRellenarArea(2,dato,Fila,Columna,nElementos,0)
                    nombre=nombre+"LineaVertical"
                    self.imgOperacion(nombre)
                    self.abHtml.datosHtmlOperacion(self.btnOperacion6.cget("text"),nombre)
                    messagebox.showinfo(message=self.btnOperacion6.cget("text"),title="Informacion")

    def oprMatriz7(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break

        dFila=int(self.dFilaR.get())
        dColumna=int(self.dColumnaR.get())
        hFila=int(self.hFilaR.get())
        hColumna=int(self.hColumnaR.get())

        if(dFila>int(dato.fila)):
            self.error.datosHtmlErrores(self.btnOperacion7.cget("text"),nombre,"Valor incorrecto de Fila Desde \nEs mayor")
            messagebox.showinfo(message="Valor incorrecto de Fila Desde \nEs mayor",title="Informacion")
        else:
            if(dColumna>int(dato.columna)):
                self.error.datosHtmlErrores(self.btnOperacion7.cget("text"),nombre,"Valor incorrecto de Columna Desde \nEs mayor")
                messagebox.showinfo(message="Valor incorrecto de Columna Desde \nEs mayor",title="Informacion")
            else:
                if(hFila>int(dato.fila)):
                    self.error.datosHtmlErrores(self.btnOperacion7.cget("text"),nombre,"Valor incorrectos de Fila Hasta \nEs mayor")
                    messagebox.showinfo(message="Valor incorrectos de Fila Hasta \nEs mayor",title="Informacion")
                else:
                    if(hColumna>int(dato.columna)):
                        self.error.datosHtmlErrores(self.btnOperacion7.cget("text"),nombre,"Valor incorrecto de Columna Hasta \nEs mayor")
                        messagebox.showinfo(message="Valor incorrecto de Columna Hasta \nEs mayor",title="Informacion")
                    else:
                        arch.graficarRellenarArea(3,dato,dFila,hFila,dColumna,hColumna)
                        nombre=nombre+"Rectangulo"
                        self.imgOperacion(nombre)
                        self.abHtml.datosHtmlOperacion(self.btnOperacion7.cget("text"),nombre)
                        messagebox.showinfo(message=self.btnOperacion7.cget("text"),title="Informacion")

    def oprMatriz8(self):
        arch=Archivo()
        nombre=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato=self.listaMat.getDato(i)
            if(dato.nombre==nombre):
                break
        dFila=int(self.dFilaT.get())
        dColumna=int(self.dColumnaT.get())
        hFila=int(self.hFilaT.get())
        hColumna=int(self.hColumnaT.get())

        if(dFila>int(dato.fila)):
            self.error.datosHtmlErrores(self.btnOperacion8.cget("text"),nombre,"Valor incorrecto de Fila Desde \nEs mayor")
            messagebox.showinfo(message="Valor incorrecto de Fila Desde \nEs mayor",title="Informacion")
        else:
            if(dColumna>int(dato.columna)):
                self.error.datosHtmlErrores(self.btnOperacion8.cget("text"),nombre,"Valor incorrecto de Columna Desde \nEs mayor")
                messagebox.showinfo(message="Valor incorrecto de Columna Desde \nEs mayor",title="Informacion")
            else:
                if(hFila>int(dato.fila)):
                    self.error.datosHtmlErrores(self.btnOperacion8.cget("text"),nombre,"Valor incorrectos de Fila Hasta \nEs mayor")
                    messagebox.showinfo(message="Valor incorrectos de Fila Hasta \nEs mayor",title="Informacion")
                else:
                    if(hColumna>int(dato.columna)):
                        self.error.datosHtmlErrores(self.btnOperacion8.cget("text"),nombre,"Valor incorrecto de Columna Hasta \nEs mayor")
                        messagebox.showinfo(message="Valor incorrecto de Columna Hasta \nEs mayor",title="Informacion")
                    else:
                        arch.graficarRellenarArea(4,dato,dFila,hFila,dColumna,hColumna)
                        nombre=nombre+"Triangulo"
                        self.imgOperacion(nombre)
                        self.abHtml.datosHtmlOperacion(self.btnOperacion8.cget("text"),nombre)
                        messagebox.showinfo(message=self.btnOperacion8.cget("text"),title="Informacion")


###    Operaciones con dos matrices   ###

    def oprMatriz21(self):
        arch=Archivo()
        nombre1=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato1=self.listaMat.getDato(i)
            if(dato1.nombre==nombre1):
                break
        nombre2=self.cmbMatriz2.get()
        for j in range(1,self.listaMat.tamano+1):
            dato2=self.listaMat.getDato(j)
            if(dato2.nombre==nombre2):
                break

        if(dato1.fila>dato2.fila or dato2.fila>dato1.fila):
            self.error.datosHtmlErrores(self.btnOperacion21.cget("text"),nombre1+","+nombre2,"Las matrices no tienen las mismas dimensiones")
            messagebox.showinfo(message="Las matrices no tienen las mismas dimensiones",title="Informacion")
        else:
            arch.graficarOperacion(1,dato1,dato2)
            nombre=nombre1+"Union"+nombre2
            self.imgOperacionR(nombre)
            messagebox.showinfo(message=self.btnOperacion21.cget("text"),title="Informacion")
            self.abHtml.datosHtmlOperacion(self.btnOperacion21.cget("text"),nombre)


    def oprMatriz22(self):
        arch=Archivo()
        nombre1=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato1=self.listaMat.getDato(i)
            if(dato1.nombre==nombre1):
                break
        nombre2=self.cmbMatriz2.get()
        for j in range(1,self.listaMat.tamano+1):
            dato2=self.listaMat.getDato(j)
            if(dato2.nombre==nombre2):
                break

        if(dato1.fila>dato2.fila or dato2.fila>dato1.fila):
            self.error.datosHtmlErrores(self.btnOperacion22.cget("text"),nombre1+","+nombre2,"Las matrices no tienen las mismas dimensiones")
            messagebox.showinfo(message="Las matrices no tienen las mismas dimensiones",title="Informacion")
        else:

            arch.graficarOperacion(2,dato1,dato2)
            nombre=nombre1+"Interseccion"+nombre2
            self.imgOperacionR(nombre)
            messagebox.showinfo(message=self.btnOperacion22.cget("text"),title="Informacion")
            self.abHtml.datosHtmlOperacion(self.btnOperacion22.cget("text"),nombre)


    def oprMatriz23(self):
        arch=Archivo()
        nombre1=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato1=self.listaMat.getDato(i)
            if(dato1.nombre==nombre1):
                break
        nombre2=self.cmbMatriz2.get()
        for j in range(1,self.listaMat.tamano+1):
            dato2=self.listaMat.getDato(j)
            if(dato2.nombre==nombre2):
                break

        if(dato1.fila>dato2.fila or dato2.fila>dato1.fila):
            self.error.datosHtmlErrores(self.btnOperacion23.cget("text"),nombre1+","+nombre2,"Las matrices no tienen las mismas dimensiones")
            messagebox.showinfo(message="Las matrices no tienen las mismas dimensiones",title="Informacion")
        else:

            arch.graficarOperacion(3,dato1,dato2)
            nombre=nombre1+"Diferencia"+nombre2
            self.imgOperacionR(nombre)
            messagebox.showinfo(message=self.btnOperacion23.cget("text"),title="Informacion")
            self.abHtml.datosHtmlOperacion(self.btnOperacion23.cget("text"),nombre)

    def oprMatriz24(self):
        arch=Archivo()
        nombre1=self.cmbMatriz1.get()
        for i in range(1,self.listaMat.tamano+1):
            dato1=self.listaMat.getDato(i)
            if(dato1.nombre==nombre1):
                break
        nombre2=self.cmbMatriz2.get()
        for j in range(1,self.listaMat.tamano+1):
            dato2=self.listaMat.getDato(j)
            if(dato2.nombre==nombre2):
                break

        if(dato1.fila>dato2.fila or dato2.fila>dato1.fila):
            self.error.datosHtmlErrores(self.btnOperacion24.cget("text"),nombre1+","+nombre2,"Las matrices no tienen las mismas dimensiones")
            messagebox.showinfo(message="Las matrices no tienen las mismas dimensiones",title="Informacion")
        else:
            arch.graficarOperacion(4,dato1,dato2)
            nombre=nombre1+"Dif_Simetrica"+nombre2
            self.imgOperacionR(nombre)
            messagebox.showinfo(message=self.btnOperacion24.cget("text"),title="Informacion")
            self.abHtml.datosHtmlOperacion(self.btnOperacion24.cget("text"),nombre)

### Reporte ###
    def genReporte(self):
        self.abHtml.cerrarHtmlOperacion()
        self.error.cerrarHtmlErrores()

        messagebox.showinfo(message="Reportes generados en la carpeta Html",title="Informacion")
### Datos de Estudiante  ###
    def datosEstudiante(self):

        self.imgEst=Image.open('imagen/datosPersonales.png')
        self.imgEst=self.imgEst.resize((625,250),Image.ANTIALIAS)
        self.imgEst=ImageTk.PhotoImage(self.imgEst)
        self.est=Label(self.pnlPrincipal,text="Datos Estudiante",
                        image=self.imgEst,
                        compound="top")
        self.est.image=self.imgEst
        self.est.place(x=50,y=150)


####  Etiqueta para Operaciones  ####

    def etiqueta(self,texto,x1,y1):
        self.lblOpe=Label(self.pnlPrincipal,text=texto)
        self.lblOpe.config(font=("Verdana",12),
                                bg="#21252b",
                                fg="#787e8c" )
        self.lblOpe.place(x=x1,y=y1)

ventana=tk.Tk()
app=Principal(ventana)
app.mainloop()
