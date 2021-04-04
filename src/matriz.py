from cabecera import *
from nodo import *

class Matriz:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cabFila=ListaCabecera()
        self.cabColumna=ListaCabecera()
        self.dato=None
        self.tamano=0


    def agregar(self,nfila,ncolumna,dato):
        self.tamano+=1
        #crear un nuevo nodo donde se guardara el Dato
        nuevoDato=Nodo(nfila,ncolumna,dato)
        #Asignar la cabecera de la fila en la que
        #guardarermos el nodo
        nodoFila=self.cabFila.devolverCabecera(nfila)
        if(nodoFila==None):
            #crear cabecerar
            nodoFila=NodoCabecera(nfila)
            nodoFila.nodoDato=nuevoDato
            self.cabFila.crearCabecera(nodoFila)
        else:
            #print(nuevoDato.columna)
            if nuevoDato.columna<nodoFila.nodoDato.columna:
                nuevoDato.derecha=nodoFila.nodoDato
                nodoFila.nodoDato.izquierda=nuevoDato
                nodoFila.nodoDato=nuevoDato
            else:
                actual=nodoFila.nodoDato
                #recorremos hacia la derecha por las columnas
                #y actualizamos la posicion de los datos

                while actual.derecha!=None:
                    if nuevoDato.columna<actual.derecha.columna:
                        nuevoDato.derecha=actual.derecha
                        actual.derecha.izquierda=nuevoDato
                        nuevoDato.izquierda=actual
                        actual.derecha=nuevoDato

                        break
                    actual=actual.derecha

                if actual.derecha==None:
                    actual.derecha=nuevoDato
                    nuevoDato.izquierda=actual

        #Asignar la cabecera de la Columna en la que
        #guardarermos el nodo
        nodoColumna=self.cabColumna.devolverCabecera(ncolumna)

        if(nodoColumna==None):
            #crear cabecerar
            nodoColumna=NodoCabecera(ncolumna)
            nodoColumna.nodoDato=nuevoDato
            self.cabColumna.crearCabecera(nodoColumna)
        else:
            #nodoColumna=self.cabColumna.devolverCabecera(ncolumna)
            if nuevoDato.fila<nodoColumna.nodoDato.fila:
                nuevoDato.abajo=nodoColumna.nodoDato
                nodoColumna.nodoDato.arriba=nuevoDato
                nodoColumna.nodoDato=nuevoDato
            else:
                actual=nodoColumna.nodoDato
                #recorremos hacia abajo por las filas
                #y actualizamos la posicion de los datos
                while actual.abajo!=None:
                    if nuevoDato.fila<actual.abajo.fila:
                        nuevoDato.abajo=actual.abajo
                        actual.abajo.arriba=nuevoDato
                        nuevoDato.arriba=actual
                        actual.abajo=nuevoDato
                        break
                    actual=actual.abajo
                if actual.abajo==None:
                    actual.abajo=nuevoDato
                    nuevoDato.arriba=actual

    def modificar(self,nfila,ncolumna,dato):
        modiDato=Nodo(nfila,ncolumna,dato)
        nFila=self.cabFila.inicio
        actual=nFila.nodoDato
        while actual!=None:
            #print("Fila = ",actual.fila,"Columna = ",actual.columna)
            if(nfila==actual.fila and ncolumna==actual.columna):
                #print("existe")
                #print(actual.dato)
                actual.dato=dato
                modiDato.izquierda=actual
                #print("Se modifico")
                #print(actual.dato)
                break
            actual=actual.derecha
        nColumna=self.cabColumna.inicio
        actual=nColumna.nodoDato
        while actual!=None:
            #print("Fila = ",actual.fila,"Columna = ",actual.columna)
            if(nfila==actual.fila and ncolumna==actual.columna):
                #print("existe")
                #print(actual.dato)
                actual.dato=dato
                modiDato.arriba=actual
                #print("Se modifico")
                #print(actual.dato)
                break
            actual=actual.abajo

    def eliminar(self,nfila,ncolumna):

        nFila=self.cabFila.inicio
        actual=nFila.nodoDato
        while actual!=None:
            #print("Fila = ",actual.fila,"Columna = ",actual.columna)
            if(nfila==actual.fila and ncolumna==actual.columna):
                #print("existe")
                #print(actual.dato)
                actual.derecha.izquierda=actual.izquierda
                actual.izquierda.derecha=actual.derecha

                #print("Se modifico")
                #print(actual.dato)
                break
            actual=actual.derecha
        nColumna=self.cabColumna.inicio
        actual=nColumna.nodoDato
        while actual!=None:
            #print("Fila = ",actual.fila,"Columna = ",actual.columna)
            if(nfila==actual.fila and ncolumna==actual.columna):
                #print("existe")
                #print(actual.dato)
                actual.abajo.arriba=actual.arriba
                actual.arriba.abajo=actual.abajo
                #print("Se modifico")
                #print(actual.dato)
                break
            actual=actual.abajo




    def desplegar1(self):
        #self.cabFila.devolver(nfila)
        print("Por Filas",self.tamano)

        for i in range(1,self.tamano):
            nFila=self.cabFila.devolverCabecera(i)
            if(nFila!=None):

                actual=nFila.nodoDato

            while actual!=None:
                print("Fila = ",actual.fila,"Columna = ",actual.columna,"[ ",actual.dato,"]" )
                actual=actual.derecha



    def desplegar2(self):
        #self.cabFila.devolver(nfila)
        print("Por Filas" )
        print(self.tamano)

        for i in range(1,self.tamano):
            nFila=self.cabFila.devolverCabecera(i)
            print(i, " ",nFila)
            if(nFila!=None):

                actual=nFila.nodoDato
                while actual!=None:
                    print("Fila = ",actual.fila,"Columna = ",actual.columna,"[ ",actual.dato,"]" )
                    actual=actual.derecha



    def desplegar(self,fila):

        valor=self.cabFila.devolver(fila)

        return valor.nodoDato

    def devolver(self,nfila,ncolumna):
        nFila=self.cabFila.devolverCabecera(nfila)
        #nodoFila=self.cabFila.devolverCabecera(nfila)
        if(nFila!=None):

            actual=nFila.nodoDato
            while actual!=None:

                if(nfila==actual.fila and ncolumna==actual.columna):
                    #print("existe")
                    #print(actual.dato)
                    return actual
                    break
                    #print("Se modifico")
                    #print(actual.dato)

                actual=actual.derecha
        return None

        if(actual==None):
            return None
            print("el dato no existe")


    def matrizAux(self,nombre,fila,columna,dato):
        self.nombre=nombre
        self.fila=fila
        self.columna=columna
        self.dato=dato;
