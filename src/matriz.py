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

####   metodos para Operacion con una Matriz1   ###
    def llenarMatriz(self,datoMatriz):

        mat=datoMatriz
        nombre=mat.nombre
        imagen=mat.dato
        linea=""
        lin=1
        col=0

        matAux=Matriz("Aux")

        for i in range(1,len(imagen)):
            linea=linea+str(imagen[i])
            if(imagen[i]=="-"):
                col+=1
            if(imagen[i]=="*"):
                col+=1
                matAux.agregar(lin,col,"*")
                #print("fila =", lin ,"Columna= ",col)
            if(imagen[i]=="\n"):
                col=0
                lin+=1
                #print(linea)
                linea=""

        return matAux
    def contar(self,datoMatriz):



        imagen=datoMatriz
        linea=""
        lin=1
        col=0
        vacio=0
        lleno=0

        matAux=Matriz("Aux")

        for i in range(1,len(imagen)):
            linea=linea+str(imagen[i])
            if(imagen[i]=="-"):
                vacio+=1

                col+=1
            if(imagen[i]=="*"):
                lleno+=1
                col+=1
                matAux.agregar(lin,col,"*")
                #print("fila =", lin ,"Columna= ",col)
            if(imagen[i]=="\n"):
                col=0
                lin+=1
                #print(linea)
                linea=""

        return lleno,vacio

    def girarHorizontal(self,dtsMatriz,matOrginal):
        mat=dtsMatriz
        matOri=matOrginal
        matTemp=Matriz("Aux")
        contFil=1
        for f in range(int(mat.fila),0,-1):
            for c in range(1,int(mat.columna)+1):
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual!=None):
                    matTemp.agregar(contFil,int(c),"*")
            contFil+=1
        return matTemp

    def girarVertical(self,dtsMatriz,matOrginal):
        mat=dtsMatriz
        matOri=matOrginal
        matTemp=Matriz("Aux")
        contFil=1
        for f in range(int(mat.fila),0,-1):
            for c in range(int(mat.columna),0,-1):
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual!=None):
                    matTemp.agregar(int(f),contFil,"*")
                contFil+=1
            contFil=1
        return matTemp

    def transpuesta(self,dtsMatriz,matOrginal):
        mat=dtsMatriz
        matOri=matOrginal
        matTemp=Matriz("Aux")

        for f in range(int(mat.fila),0,-1):
            for c in range(int(mat.columna),0,-1):
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual!=None):
                    matTemp.agregar(int(c),int(f),"*")


        return matTemp

    def limpiarArea(self,dtsMatriz,matOriginal,x1,x2,y1,y2):
        mat=dtsMatriz
        matOri=matOriginal

        matTempo=Matriz("matTemp")

        for f in range(int(x1),int(x2)+1):
            for c in range(int(y1),int(y2)+1):
                datoActual=matOri.devolver(int(f),int(c))
                if datoActual!=None:
                    matTempo.agregar(int(datoActual.fila),int(datoActual.columna),"*")

        matAux=Matriz("matAux")
        for f in range(1,int(mat.fila)+1):
            for c in range(1,int(mat.columna)+1):
                datoActual1=matOri.devolver(int(f),int(c))
                datoActual2=matTempo.devolver(int(f),int(c))
                if(datoActual1==None and datoActual2!=None):
                    matAux.agregar(int(f),int(c),"*")
                if(datoActual1!=None and datoActual2==None):
                    matAux.agregar(int(f),int(c),"*")
                if(datoActual1!=None and datoActual2!=None):
                    matAux.agregar(int(f),int(c),"-")




        return matAux

    def llenarLineaHorizontal(self,dtsMatriz,matOriginal,fila,columna,nElementos):
        mat=dtsMatriz
        matOri=matOriginal
        matTemp=matOri

        for f in range(int(fila),int(fila)+1):
            for c in range(int(columna),int(columna)+int(nElementos)):
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual==None):
                    matTemp.agregar(int(f),int(c),"*")
        return matTemp

    def llenarLineaVertical(self,dtsMatriz,matOriginal,fila,columna,nElementos):
        mat=dtsMatriz
        matOri=matOriginal
        matTemp=matOri
        for f in range(int(fila),int(fila)+int(nElementos)):

            for c in range(int(columna),int(columna)+1):
                #print(f," ",c)
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual==None):
                    matTemp.agregar(int(f),int(c),"*")
                    datoActual2=matTemp.devolver(int(f),int(c))
        return matTemp
    def llenarRectangulo(self,dtsMatriz,matOriginal,fila,hFila,columna,hColumna):
        mat=dtsMatriz
        matOri=matOriginal
        matTemp=matOri
        for f in range(int(fila),int(hFila)+1):

            for c in range(int(columna),int(hColumna)+1):
                print(f," ",c)
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual==None):
                    matTemp.agregar(int(f),int(c),"*")
                    datoActual2=matTemp.devolver(int(f),int(c))
        return matTemp
    def llenarTriangulo(self,dtsMatriz,matOriginal,fila,hFila,columna,hColumna):
        mat=dtsMatriz
        matOri=matOriginal
        matTemp=matOri
        n=1
        for f in range(int(fila),int(hFila)+1):
            for c in range(int(columna),int(columna)+n):
                #print(f," ",c)
                datoActual=matOri.devolver(int(f),int(c))
                if(datoActual==None):
                    matTemp.agregar(int(f),int(c),"*")
            n+=1

        return matTemp

### Metodos para Operacion con dos Matrices ###
    def unionDeMatrices(self,dtsMatriz1,dtsMatriz2,matOriginal1,matOriginal2):
        mat1=dtsMatriz1
        mat2=dtsMatriz2
        matOri1=matOriginal1
        matOri2=matOriginal2
        matTemp=Matriz("matTemporal")
        for f in range(1,int(mat1.fila)+1):
            for c in range(1,int(mat1.columna)+1):
                datoActual1=matOri1.devolver(int(f),int(c))
                datoActual2=matOri2.devolver(int(f),int(c))

                if(datoActual1==None and datoActual2!=None):
                    matTemp.agregar(int(f),int(c),"*")
                if(datoActual1!=None and datoActual2==None):
                    matTemp.agregar(int(f),int(c),"*")
                if(datoActual1!=None and datoActual2!=None):
                    matTemp.agregar(int(f),int(c),"*")
        return matTemp

    def interseccionDeMatrices(self,dtsMatriz1,dtsMatriz2,matOriginal1,matOriginal2):
        mat1=dtsMatriz1
        mat2=dtsMatriz2
        matOri1=matOriginal1
        matOri2=matOriginal2
        matTemp=Matriz("matTemporal")
        for f in range(1,int(mat1.fila)+1):
            for c in range(1,int(mat1.columna)+1):
                datoActual1=matOri1.devolver(int(f),int(c))
                datoActual2=matOri2.devolver(int(f),int(c))
                if(datoActual1!=None and datoActual2!=None):
                    matTemp.agregar(int(f),int(c),"*")
        return matTemp

    def diferenciaDeMatrices(self,dtsMatriz1,dtsMatriz2,matOriginal1,matOriginal2):
        mat1=dtsMatriz1
        mat2=dtsMatriz2
        matOri1=matOriginal1
        matOri2=matOriginal2
        matTemp=Matriz("matTemporal")

        for f in range(1,int(mat1.fila)+1):
            for c in range(1,int(mat1.columna)+1):
                datoActual1=matOri1.devolver(int(f),int(c))
                datoActual2=matOri2.devolver(int(f),int(c))
                if(datoActual1!=None and datoActual2==None):
                    matTemp.agregar(int(f),int(c),"*")

        return matTemp

    def difSimetricaDeMatrices(self,dtsMatriz1,dtsMatriz2,matOriginal1,matOriginal2):
        mat1=dtsMatriz1
        mat2=dtsMatriz2
        matOri1=matOriginal1
        matOri2=matOriginal2
        matTemp=Matriz("matTemporal")
        for f in range(1,int(mat1.fila)+1):
            for c in range(1,int(mat1.columna)+1):
                datoActual1=matOri1.devolver(int(f),int(c))
                datoActual2=matOri2.devolver(int(f),int(c))

                if(datoActual1==None and datoActual2!=None):
                    matTemp.agregar(int(f),int(c),"*")
                if(datoActual1!=None and datoActual2==None):
                    matTemp.agregar(int(f),int(c),"*")

        return matTemp
