class Room:
    def __init__(self, description):
        self.__description = description
        self.__exits = {}
        self.__items = {} #Diccionario
        self.__npc = {}

    def setExits(self, north, east, south, west, up, down):
        if(north != None):
            self.__exits['north'] = north
        if(east != None):
            self.__exits['east'] = east
        if(south != None):
            self.__exits['south'] = south
        if(west != None):
            self.__exits['west'] = west
        if (up != None):
            self.__exits['up'] = up
        if (down != None):
            self.__exits['down'] = down
    
    def setExit(self, direction, room):
        self.__exits[direction] = room

    
    def getDescription(self):
        return self.__description

    def getExit(self, direction):
        if(direction in self.__exits):
            return self.__exits[direction]
        else:
            return None

    def getExits(self):
        return self.__exits

    def getLocationInfo(self):
        print("Estas en " + self.getDescription())
        print("Salidas: " + self.getExitStrings())
        print ("Items : " + self.getItems())
        print()
        if not self.getNPCs():
            pass
        else:
            print("Personajes en la sala: ")
            for x in self.getNPCs():
                print(x, ' ')

    def getExitStrings(self):
        exits = ' // '
        exits = exits.join(self.__exits.keys())
        return exits

    def addItem(self, item):
        self.__items[item.getName()] = item # Utiliza el nombre del item como clave, y el objeto (item) como valor.
    
    def getItems(self):
        resultado = ' , '
        resultado = resultado.join(self.__items.keys()) # Va recorriendo cada valor de la lista, la convierte en string y los separa con una coma.
        return resultado

    def delItems(self, item_name):
        item = {}
        if(item_name in self.__items):
            item = self.__items[item_name] #Parecido a addItem, almacena en la variable item el valor "item" (el cual es un objeto) de la clave "item_name" (el cual es una string)
            del self.__items[item_name]
            return item # Devuelve el objeto
        else:
            return None

    def addNPC(self, npc):
        self.__npc[npc.getName()] = npc # Agregar el nombre como clave y el objeto NPC como valor

    def delNPC(self, npc_name):
        if (npc_name in self.__npc):
            del self.__npc[npc_name] # Elimina el NPC del diccionario
        else:
            return None

    def getNPCs(self):
        list_npc = []
        for x in self.__npc:
            list_npc.append(x)
        return list_npc
    def getInfoNPC(self, npc):
        if(npc in self.__npc):
            return self.__npc[npc]
        else:
            return None

        
class lockedRoom(Room):
    def __init__(self, description):
        Room.__init__(self, description)
        self.__exits = {}
        self.__items = {}
        self.__locked = True
    
    def checkDoor(self):
        return self.__locked
    
    def unlockDoor(self, room):
        self.__locked = False
    
    
        



