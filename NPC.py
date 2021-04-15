class NPC():
    def __init__(self, name, room,  speach, item=None,  reward = None):
        self.__name = name
        self.__room = room
        self.__dialogue = speach
        self.__reward = reward
        self.__objective = item


    def getName(self):
        return self.__name
    def getRoom(self):
        return self.__room
    def getItem(self):
        return self.__objective
    def getSpeech(self):
        return self.__dialogue
    def getReward(self):
        return self.__reward
    
    def reciveItem(self, item): # Recibe el item
        if item == self.getItem(): # Si es el mismo que se pedía
            print(self.getName(), ' dice:')
            print('Has cumplido con tu misión')
            return True # Retorna True
        else:
            print(self.getName(), ' dice: ')
            print('Este no es el item que te pedí')
            return False # Sino retorna False

    