

class ListaCabecera:
    def __init__(self):
        self.inicio=None

    def crearCabecera(self,nuevaCabecera):

        if(self.inicio==None):
            # si aun no existe cabecera fila creamos una
            # nueva cabecera
            self.inicio=nuevaCabecera
        elif nuevaCabecera.codigo<self.inicio.codigo:
            #agregamos la nueva cabecera como inicio
            #de la lista
            nuevaCabecera.cbrSiguiente=self.inicio
            self.inicio.cbrAnterior=nuevaCabecera
            self.inicio=nuevaCabecera
        else:

            actual=self.inicio
            #ordenamos la cabecera de forma ascendente
            while actual.cbrSiguiente!=None:
                if(nuevaCabecera.codigo>actual.cbrSiguiente.codigo):
                    nuevaCabecera.cbrSiguiente=actual.cbrSiguiente
                    actual.cbrSiguiente.cbrAnterior=nuevaCabecera
                    nuevaCabecera.cbrAnterior=actual
                    actual.cbrSiguiente=nuevaCabecera
                    break
                actual=actual.cbrSiguiente
            if(actual.cbrSiguiente==None):
                actual.cbrSiguiente=nuevaCabecera
                nuevaCabecera.cbrAnterior=actual


    def devolverCabecera(self,codigo):
        actual=self.inicio
        #recorremos la lista para encontrar
        #la cabecera
        while actual!=None:
            if(actual.codigo==codigo):
                return actual
            actual=actual.cbrSiguiente
        actual=None
        return actual


    def devolverCabecera(self,codigo):
        actual=self.inicio
        #recorremos la lista para encontrar
        #la cabecera
        while actual!=None:
            if(actual.codigo==codigo):
                return actual
                
            actual=actual.cbrSiguiente

        return None

class NodoCabecera:
    #Este nodo nos ayudara a llevar el control
    # de nuestra lista de cabecera.
    #parametro codigo es para identificar el
    #numero de columna o numero de fila de la cabecera.
    #y los apuntadores anterior y siguiente por ser
    # una lista doblemente enlazada

    def __init__(self,codigo):
        self.codigo=codigo
        self.cbrAnterior=None
        self.cbrSiguiente=None
        self.nodoDato=None
