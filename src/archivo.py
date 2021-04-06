import xml.etree.ElementTree as et
from graphviz import Digraph as dg
from matriz import *
from lstCircular import *
import os
import re

class Archivo(object):
    """docstring for archivo."""

    def __init__(self):
        self.nombre=""
        self.listaMatriz=Lista()


    def abrir(self,rutaArchivo):
        os.system("cls")
        try:
            print(rutaArchivo)
            arbol=et.parse(rutaArchivo)
            raiz=arbol.getroot()
            if(raiz.tag=="matrices"):
                for elemento in raiz:
                    print(elemento.tag)
                    matAux=Matriz("A")
                    if(elemento.tag=="matriz"):

                        nsubElement=1
                        for subElemento in elemento:
                            #print(subElemento.tag,nsubElement)
                            if(nsubElement==1 and subElemento.tag=="nombre"):
                                #print(subElemento.tag)
                                #print(subElemento.text)
                                nombre=subElemento.text
                            elif(nsubElement==1 and subElemento.tag!="nombre"):
                                print("Error 101 se esperaba la etiqueta nombre")
                                #print(subElemento.text)
                            else:
                                if(nsubElement==2 and subElemento.tag=="filas"):
                                    #print(subElemento.tag)
                                    #print(subElemento.text)
                                    fila=subElemento.text
                                elif(nsubElement==2 and subElemento.tag!="filas"):
                                    print("Error 102 se esperaba la etiqueta filas")
                                #    print(subElemento.text)
                                else:
                                    if(nsubElement==3 and subElemento.tag=="columnas"):
                                        #print(subElemento.tag)
                                        #print(subElemento.text)
                                        columna=subElemento.text
                                    elif(nsubElement==3 and subElemento.tag!="columnas"):
                                        print("Error 103 se esperaba la etiqueta columna")
                                        #print(subElemento.text)
                                    else:
                                        if(nsubElement==4 and subElemento.tag=="imagen"):
                                            #print(subElemento.tag)
                                            #print(subElemento.text)
                                            imagen=subElemento.text
                                            matAux.matrizAux(nombre,fila,columna,imagen)
                                            self.listaMatriz.agregar(matAux)

                                        elif(nsubElement==4 and subElemento.tag!="imagen"):
                                            print("Error 104 se esperaba la etiqueta imagen")
                                            #print(subElemento.text)
                                        else:
                                            print("Error no se reconoce etiqueta")



                            nsubElement+=1
                    else:
                        print("Error 100 se esperaba la etiqueta matriz")
                        break;
            else:
                print("Error 1 ")

        except FileNotFoundError as e:
            print("El archivo no existe")
        except  Exception as e:
            print("Error en la estrucura del archivo de entrada")


    def graficarProy(self,datoMatriz,op):
            os.system("cls")
            print("graficando....")
            mat=datoMatriz
            nombre=mat.nombre
            imagen=mat.dato
            linea=""
            lin=1
            col=0

            if(op==0):
                matAux=Matriz("Aux")
                for i in range(1,len(imagen)):
                    linea=linea+str(imagen[i])
                    if(imagen[i]=="-"):
                        col+=1
                    if(imagen[i]=="*"):
                        col+=1
                        matAux.agregar(lin,col,"*")
                        print("fila =", lin ,"Columna= ",col)
                    if(imagen[i]=="\n"):
                        col=0
                        lin+=1
                        print(linea)
                        linea=""
            if(op==1):
                nombre=mat.nombre+"G.Horizontal"
                matrizOri=Matriz("Original")
                matOri=matrizOri.llenarMatriz(mat)
                matAux=matrizOri.girarHorizontal(mat,matOri)
            if(op==2):
                nombre=mat.nombre+"G.Vertical"
                matrizOri=Matriz("Original")
                matOri=matrizOri.llenarMatriz(mat)
                matAux=matrizOri.girarVertical(mat,matOri)
            if(op==3):
                nombre=mat.nombre+"Transpuesta"
                matrizOri=Matriz("Original")
                matOri=matrizOri.llenarMatriz(mat)
                matAux=matrizOri.transpuesta(mat,matOri)


            texto=self.tabla(mat,matAux)

            #print(texto)
            s = dg('structs', node_attr={'shape': 'plaintext'})
            s.node('struct1', '''<'''+texto +'''
                    >''')
            s.render("imagen/"+nombre,format="png",view=False)
            #s.view

    def graficarRellenarArea(self,op,datoMatriz,x1,x2,y1,y2):
        os.system("cls")
        print("graficando....")
        mat=datoMatriz
        nombre=mat.nombre
        imagen=mat.dato

        matrizOri=Matriz("Original")

        if(op==0):
            nombre=mat.nombre+"Limpiar"
            matrizOri=Matriz("Original")
            matOri=matrizOri.llenarMatriz(mat)
            matAux=matrizOri.limpiarArea(mat,matOri,x1,x2,y1,y2)

        if(op==1):
            nombre=mat.nombre+"LineaHorizontal"
            matOri=matrizOri.llenarMatriz(mat)
            matAux=matrizOri.llenarLineaHorizontal(mat,matOri,x1,x2,y1)
        if(op==2):
            nombre=mat.nombre+"LineaVertical"
            matOri=matrizOri.llenarMatriz(mat)
            matAux=matrizOri.llenarLineaVertical(mat,matOri,x1,x2,y1)
        if(op==3):
            nombre=mat.nombre+"Rectangulo"
            matOri=matrizOri.llenarMatriz(mat)
            matAux=matrizOri.llenarRectangulo(mat,matOri,x1,x2,y1,y2)

        if(op==4):
            nombre=mat.nombre+"Triangulo"
            matOri=matrizOri.llenarMatriz(mat)
            matAux=matrizOri.llenarTriangulo(mat,matOri,x1,x2,y1,y2)

        texto=self.tabla(mat,matAux)

        #print(texto)
        s = dg('structs', node_attr={'shape': 'plaintext'})
        s.node('struct1', '''<'''+texto +'''
                >''')
        s.render("imagen/"+nombre,format="png",view=False)
        #s.view()
    def graficarOperacion(self,op,datoMatriz1,datoMatriz2):
        os.system("cls")
        print("graficando....")
        mat1=datoMatriz1
        nombre1=mat1.nombre
        imagen1=mat1.dato

        mat2=datoMatriz2
        nombre2=mat2.nombre
        imagen2=mat2.dato

        matrizOri1=Matriz("Original1")
        matrizOri2=Matriz("Original2")

        if(op==1):
            nombre=mat1.nombre+"Union"+mat2.nombre
            matOri1=matrizOri1.llenarMatriz(mat1)
            matOri2=matrizOri2.llenarMatriz(mat2)
            matAux=matrizOri1.unionDeMatrices(mat1,mat2,matOri1,matOri2)
        if(op==2):
            nombre=mat1.nombre+"Interseccion"+mat2.nombre
            matOri1=matrizOri1.llenarMatriz(mat1)
            matOri2=matrizOri2.llenarMatriz(mat2)
            matAux=matrizOri1.interseccionDeMatrices(mat1,mat2,matOri1,matOri2)
        if(op==3):
            nombre=mat1.nombre+"Diferencia"+mat2.nombre
            matOri1=matrizOri1.llenarMatriz(mat1)
            matOri2=matrizOri2.llenarMatriz(mat2)
            matAux=matrizOri1.diferenciaDeMatrices(mat1,mat2,matOri1,matOri2)
        if(op==4):
            nombre=mat1.nombre+"Dif_Simetrica"+mat2.nombre
            matOri1=matrizOri1.llenarMatriz(mat1)
            matOri2=matrizOri2.llenarMatriz(mat2)
            matAux=matrizOri1.difSimetricaDeMatrices(mat1,mat2,matOri1,matOri2)
        texto=self.tabla(mat1,matAux)

        #print(texto)
        s = dg('structs', node_attr={'shape': 'plaintext'})
        s.node('struct1', '''<'''+texto +'''
                >''')
        s.render("imagen/"+nombre,format="png",view=False)


    def tabla(self,dtsMatriz,mAux):

            mat=dtsMatriz
            matAux=mAux

            archivo=open("imagen/tabla.txt","w")
            archivo.write("<table bgcolor=\"#4b5362\" cellspacing=\"0\" >")
            archivo.write("<th>")
            archivo.write("<TD bgcolor=\"red\" width=\"20\" height=\"20\"><font color=\"white\" >"+mat.nombre+"</font></TD>")

            for f in range(1,int(mat.columna)+1):
                archivo.write("<td width=\"20\" height=\"20\">")
                archivo.write(str(f))
                archivo.write("</td>")
                #archivo.write("</th>")
            archivo.write("</th>")
            for f in range(1,int(mat.fila)+1):
                archivo.write("<tr>")
                archivo.write("<td>"+str(f)+"</td>")
                for c in range(1,int(mat.columna)+1):
                    #print(f ," ",c)
                    datoActual=matAux.devolver(int(f),int(c))
                    if(datoActual!=None):
                        #print(datoActual.fila ," " ,datoActual.columna ," ",datoActual.dato)
                    #print(datoActual.fila)
                    #print(datoActual.columna)
                        archivo.write("<td>")

                        if(f==datoActual.fila and c==datoActual.columna and datoActual.dato=="*"):
                            archivo.write("<img src=\"../imagen/ast.png\"></img>")
                            #archivo.write("<font color=\"white\" >*</font>")
                        archivo.write("</td>")
                    else:
                        archivo.write("<td>")
                        #if(f==datoActual.fila and c==datoActual.columna and datoActual.dato=="*"):
                        #    archivo.write("<img src=\"../imagen/ast.png\"></img>")
                            #archivo.write("<font color=\"white\" >*</font>")
                        archivo.write("</td>")

                archivo.write("</tr>")

            archivo.write("</table>")
            archivo.close()
            archivo=open("imagen/tabla.txt","r")
            texto=archivo.read()
            archivo.close()
            return texto
