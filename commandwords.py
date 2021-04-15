class CommandWords:
    
    def __init__(self):
        pass

    __VALID_COMMANDS = {"go":"<dirección>: ir hacia la dirección", 
    "look":"mirar la habitación",
    "quit":"salir", 
    "help":"<comando> qué comandos usar y cómo", 
    "eat":"<item>: comer item del inventario", 
    "back":"volver a la habitación anterior", 
    "take":"agarrar objeto de la habitación", 
    "drop":"tirar item del inventario sobre la habitación actual", 
    "inventory":"revisar el inventario", 
    "charge":"cargar el arma, si está disponible", 
    "fire":"disparar el arma, si está disponible", 
    "missions":"muestra las misiones disponibles.", 
    "use":"usar item",
    "speak":"<personaje>: hablar con el personaje",
    "give": "<item>: darle item al personaje que se encuentre en la habitación",
    "open": "<item>: abrir item, solo si es de tipo 'Cofre'"
    }

    def isCommand(self, aString):
        return aString in self.__VALID_COMMANDS
    def get_commands(self):
        commands = ''
        for command in self.__VALID_COMMANDS.keys() :
            commands += command + " "
        return commands
    def get_command_help(self, comando):
        if comando in self.__VALID_COMMANDS.keys():
            print (comando, ' : ', self.__VALID_COMMANDS[comando])
        else:
            print('Ese comando no existe.')