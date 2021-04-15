class Item():
    def __init__(self, name, description , weight):
        self.__name = name
        self.__description = description
        self.__weight = weight
    
    #Todos los atributos a privado y definir variable que devuelve cada valor
    
    def showDescription(self):
        return self.__description
    
    def getName(self):
        return self.__name

    def getWeight(self):
        return self.__weight

    def itemInfo(self):
        return self.__name + ': '+ self.__description
    

class Comestible(Item):

    def __init__(self, name, description , weight, increase, attribute):
        Item.__init__(self, name, description, weight)
        self.__increase = increase
        self.__attribute = attribute
    
    def getIncrease(self):
        return self.__increase


class Usable(Item):

    def __init__(self, name, description , weight, function, room=None):
        Item.__init__(self, name, description, weight)
        self.__function = function
        self.__room = None
    
    def Usable(self):
        return self.__function
    
    def openDoor(self, room):
        room.unlockDoor(room)
    
    def addRoom(self, room):
        self.__room = room
        print('Item cargado en la habitación "%s"' % (self.__room.getDescription()))

    def getRoom(self):
        print('Item disparado! Volviendo a la habitación "%s"' % (self.__room.getDescription()))
        return self.__room
        
class Chest(Item):

    def __init__(self, name, description, weight, items, locked = True):
        Item.__init__(self, name, description, weight)
        self.__locked = bool
        self.__items = items

    def isOpened(self):
        if self.__locked is True:
            return False
        else:
            return True
    def turnLock(self):
        if self.__locked is True:
            self.__locked = False
            print('Cofre abierto')
        else:
            pass
        
    def addItems(self, items):
        for item in items:
            self.__items.append(item)

    def checkBox(self):

        if self.isOpened() is True:
            items_list = []
            for x in self.__items:
                items_list.append(x)
            return items_list
        else:
            print('El cofre se encuentra cerrado e inaccesible, encuentra una llave maestra para abrirlo.')
            
    def openChest(self, item):
        if (item.Usable() == "key"):
            self.turnLock()
            items_list = self.checkBox()
            return items_list
        else:
            print('Este item no es de tipo llave')

    