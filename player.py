class Player():
    def __init__(self, name, items, weight):
        self.__name = None
        self.__items = {}
        self.__weight = 0
        self.__max_weight = 5
        self.__actualroom = None
        self.__movements = 0 # Movimientos del jugador.
        self.__currentMission = [] # Lista con misiones pendientes
    
    def setItem(self, item, item_name):
        peso = self.__weight + (item.getWeight()) # item, al ser un objeto Item, permite usar metodos como getWeight, getName, etc.
        if (peso <= (self.__max_weight-self.__weight)): # Si la suma anterior no excede el peso asignado en la variable max_weight...
            self.__items[item_name] = item # Al igual que en room.py, define una clave de tipo string (item_name) y un valor de tipo objeto (item).
            self.__weight = peso # La suma pasa a ser la variable self.__weight
            return None # Retorna None si no excedió el peso máximo
        else:
            print('Excediste el peso máximo, no puedes juntar este item.') # En caso contrario se notifica que se excede el peso máximo permitido
            return item # y retorna el objeto "item"
        #self.__items[item.getName()] = item

    def delItems(self, item_name):
        if(item_name in self.__items): # Se fija si el item se encuentra en el inventario.
            item = self.__items[item_name]
            self.__weight = self.__weight - (self.__items[item_name].getWeight()) # Toma el peso actual del personaje y resta el del objeto por eliminar / tirar.
            del self.__items[item_name]
            return item # Retorna item para que sea usado por room.py
        else:
            return None

    def getItemInfo(self, item_name):
        return self.__items[item_name]


    def getItems(self):
        return self.__items.keys() # Devuelve los elementos del diccionario en forma de lista, para evitar el comentario "dic.keys"

    def getWeight(self):
        print (self.__weight, ' / ', self.__max_weight) # A la izquierda, el peso actual. A la derecha, el peso máximo.


    def eatItem(self, item_name):
        if item_name in self.__items: # El item está en el inventario
                amount = self.__items[item_name].getIncrease() #Toma el valor del atributo increase.
                self.addWeight(amount) # Agrega ese valor al peso máximo actual
                self.delItems(item_name) # Llama a la función delItems.
        else:
            return None

    
    def addWeight(self, add):
        if add>0: # Si el incremento es mayor a 0

            self.__max_weight += add # Peso máximo actual más el valor de incremento.
            print ("Tu peso máximo aumentó a: %s " % self.__max_weight)
        
        else:
            print('No aumentaste tu peso máximo.')

#Habitacion actual
    def setActualRoom(self, room):
        self.__actualroom = room
#Movimientos    
    def getMovements(self):
        return self.__movements
    
    def addMovement(self):
        self.__movements +=1
    
#Misiones
    def addMission(self, mission):
        self.__currentMission.append(mission) # Agrega un objeto "mission" a la lista
    def delMission(self, mission):
        self.__currentMission.remove(mission)
    def getMission(self):
        return self.__currentMission # Retorna la lista con las misiones pendientes