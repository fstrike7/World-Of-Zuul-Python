class Mission():
    def __init__(self, name, description, max_movements, type, objective):
        self.__name = name
        self.__description = description
        self.__type = type # Definimos un tipo de misión, por el momento solo usamos "checkpoint" que sería de llegar a cierta habitación en x cantidad de pasos.
        self.__max_movements = max_movements
        self.__objective = objective
    
    def showDescription(self):
        print(self.__name, ' : ', self.__description)

    def getName(self):
        return self.__name
    
    def getMaxMovements(self):
        return self.__max_movements
    
    def getObjective(self):
        return self.__objective
        
    def checkMission(self, player, movements=None, currentroom=None, item=None):
        if self.__type == 'checkpoint' :
            if movements < self.getMaxMovements() or currentroom.getDescription() == self.getObjective() :
                if currentroom.getDescription() == self.getObjective() : # Si el nombre de la sala coincide con dormitorio...
                    player.delMission(self)
                    print('Has alcanzado el objetivo! Bien hecho.') # Y avisa que se cumplió el objetivo.
                else:
                    print('Has realizado %d pasos!' % movements)
                    print('Te quedan %d pasos para llegar al dormitorio!' % (self.getMaxMovements()-movements))
            else:
                print('No cumpliste con tu objetivo, has fallado.')

