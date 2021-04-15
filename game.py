# Importamos las distintas clases
from room import Room, lockedRoom
from parser_commands import Parser
from commandwords import CommandWords
from item import Item, Comestible, Usable, Chest
from stack import Stack
from player import Player
from mission import *
from NPC import NPC

# Definimos la función principal del juego, que contiene los distintos metodos y atributos para armar el juego.
class Game():
    def __init__(self):
        self.createRooms()
        self.parser = Parser()
        self.previousRoom = Stack()
        #self.item = Item()

    def createRooms(self):

        #Salas

        sala = Room("sala")
        comedor = Room("comedor")
        cocina = Room("cocina")
        lavadero = Room("lavadero")
        jardin = Room("jardin")
        pasillo = Room("pasillo")
        dormitorio = Room("dormitorio")
        baño = Room("baño")
        balcon = Room("balcon")

        #Definimos las salas cerradas
        garaje = lockedRoom("garaje")

        #Definimos salidas

        garaje.setExit('east', sala)
        sala.setExit('north', comedor)
        sala.setExit('east', pasillo)
        sala.setExit('west', garaje)
        comedor.setExit('north', lavadero)
        comedor.setExit('east', cocina)
        comedor.setExit('south', sala)
        cocina.setExit('north', jardin)
        cocina.setExit('west', comedor)
        lavadero.setExit('south', comedor)
        jardin.setExit('south', cocina)
        pasillo.setExit('up', dormitorio)
        pasillo.setExit('west', sala)
        dormitorio.setExit('north', baño)
        dormitorio.setExit('east', balcon)
        dormitorio.setExit('down', pasillo)
        baño.setExit('south', dormitorio)
        balcon.setExit('west', dormitorio)

        #Definimos items

        lampara = Item('lampara', 'Una lámpara rota', 2)
        botella = Item('botella', 'Una botella vacía', 3)
        zapato = Item('zapato', 'Un zapato', 1.5)
        heladera = Item('heladera', 'Una heladera', 8)
        lavarropas = Item('lavarropas', 'Lavarropas', 10)
        tender = Item('tender', 'Un tender con ropa', 6)
        muñeco = Item('muñeco', 'Un muñeco de trapo', 3)
        cuadro = Item('cuadro', 'Un cuadro', 2)
        banco = Item('banco', 'Un banco', 4)
        mesa = Item('mesa', 'Una mesa de madera', 6)
        espejo = Item('espejo', 'Un espejo', 3)
        computadora = Item('computadora', 'Una computadora de escritorio', 6)
        cama = Item('cama', 'Una cama', 7)
        linterna = Item('linterna', 'Una linterna', 1)
        
        #Definimos items comestibles con sus respectivas propiedades.
        
        manzana = Comestible('manzana', 'Una manzana ordinaria', 1, 0, None)
        galleta = Comestible('galleta', 'Una galleta mágica', 2, 2, 'weight')

        #Definimos items utilizables, con su respectiva función.
        key = Usable('llave', 'Llave maestra', 1, 'key')
        beamer = Usable('portalgun', 'Arma de portales', 3, 'teleport')

        #Definimos cofres

        magic_box = Chest('Cofre', 'Magico cofre con muchos tesoros dentro', 1000, [manzana, galleta, espejo])

        #Añadiendo items a las distintas salas.
        comedor.addItem(zapato)
        sala.addItem(linterna) 
        sala.addItem(lampara)
        cocina.addItem(botella) 
        cocina.addItem(heladera)
        lavadero.addItem(lavarropas)
        jardin.addItem(tender)
        jardin.addItem(muñeco)
        pasillo.addItem(cuadro)
        balcon.addItem(banco)
        balcon.addItem(mesa)
        baño.addItem(espejo)
        dormitorio.addItem(cama)
        dormitorio.addItem(galleta)
        dormitorio.addItem(computadora)
        sala.addItem(manzana)
        sala.addItem(beamer)
        sala.addItem(key)
        sala.addItem(magic_box)

        #Definimos misiones
        mision1 = Mission('1ra mision', 'Llegar al dormitorio en menos de 10 movimientos', 10, 'checkpoint', 'dormitorio')

        #Definiendo NPC
        mago = NPC('Mago', sala, 'Traeme un arma de portales y te devolveré una galleta', beamer, galleta)
        aprendiz = NPC('Aprendiz', cocina, 'Bienvenido a Zuul, revisa toda la casa para encontrar objetos importantes')


        #Agregandolo a la sala
        sala.addNPC(mago)
        cocina.addNPC(aprendiz)


        #Definiendo jugador
        self.player = Player('Peter', None, 0)
        self.player.addMission(mision1)

        #Definiendo sala
        self.currentRoom = sala
        self.player.setActualRoom(self.currentRoom)

        
        return

    # Definimos la función "jugar" que se ejecutará hasta dada la orden de finalizarla.
    def play(self):
        self.printWelcome()
        
        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Gracias por jugar, adiós!")

    #Definimos un mensaje de bienvenida.
    def printWelcome(self):
        print()
        print("Bienvenido al mundo de Zuul!")
        print("El mundo de Zuul es un nuevo, increiblemente aburrido juego de aventuras.")
        print("")
        print("Escribe 'help' si necesitas ayuda.")
        print("")
        self.currentRoom.getLocationInfo()
        print("")
        self.missions()

    # Definimos una función que procesa el texto ingresado por el usuario, según su respuesta se ejecuta tal función.
    def processCommand(self,command):
        wantToQuit = False

        if(command.isUnknown()):
            print("No sé a que te refieres...")
            return False
        
        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp(command)
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)
        elif(commandWord == "look"):
            self.look()
        elif(commandWord == 'eat'):
            self.eat(command)
        elif(commandWord == 'back'):
            self.back()
        elif(commandWord == 'take'):
            self.take(command)
        elif(commandWord == 'drop'):
            self.drop(command)
        elif(commandWord == 'inventory'):
            self.inventory()
        elif(commandWord == 'charge'):
            self.charge(command)
        elif(commandWord == 'fire'):
            self.fire(command)
        elif(commandWord == 'missions'):
            self.missions()
        elif(commandWord == 'use'):
            self.use(command)
        elif(commandWord == 'speak'):
            self.speak(command)
        elif(commandWord == 'give'):
            self.give(command)
        elif(commandWord == 'open'):
            self.open(command)
        

        return wantToQuit

    def printHelp(self, command):
        if(not command.hasSecondWord()):
            print("Estás perdido. Estás solo. Deambulando")
            print("alrededor de una casa")
            print()
            print("Tus comandos son:")
            #print("   go quit help")
            print(self.parser.getHelp())
            print("Podes consultar como funciona cada comando ingresando: help <comando>")
            return
        else:
            comando = command.getSecondWord()
            print(self.parser.getCommandHelp(comando))
            print()


    def goRoom(self, command):
        if(not command.hasSecondWord()):
            print("Ir a donde?")
            return
        
        direction = command.getSecondWord()
        nextRoom = self.currentRoom.getExit(direction)
        
        
        if(nextRoom == None):
            print("No hay ninguna puerta!")
        else:
            if isinstance(nextRoom, lockedRoom) and nextRoom.checkDoor() is True:
                print ('La puerta se encuentra cerrada.')
            else:
                self.previousRoom.push(self.currentRoom)
                self.currentRoom = nextRoom
                self.currentRoom.getLocationInfo()
                self.player.setActualRoom(self.currentRoom)

                self.player.addMovement()

                currentmission = self.player.getMission()
                movements = self.player.getMovements()

                for x in currentmission:
                    x.checkMission(self.player, movements, self.currentRoom)
        
    def look(self):
        self.currentRoom.getLocationInfo()

    def back(self):
        if(not self.previousRoom.isEmpty()) :
            print('Volviendo a la última ubicación...')
            self.currentRoom = self.previousRoom.pop()
            self.currentRoom.getLocationInfo()
        else:
            print("No puedes volver")

    def take(self, command):
        if(not command.hasSecondWord()):
            print("Agarrar qué?")
            return

        item_name = command.getSecondWord()
        item = self.currentRoom.delItems(item_name) # Toma el objeto item que retorna room.py
        if(item is not None):
            item = self.player.setItem(item, item_name) # Usa el objeto item y el str item_name, pero retorna item para verificar si excedió el peso máximo
            if(item is None): # Se fija si se excedió el peso máximo, devuelve None si no lo excedió.
                print('Agarraste ', item_name)
            else:
                self.currentRoom.addItem(item) # Devuelve el objeto item a la habitación, no se usa el metodo "delItem" de player.pi porque debería revisar si está el objeto en el inventario.
                print('Devolviste ', item_name)                
        else:
            print('Error 404: ', item_name, 'not found in the current room')
    
    def drop(self, command):
        if(not command.hasSecondWord()):
            print("Dejar qué?")
            return

        item_name = command.getSecondWord()
        item = self.player.delItems(item_name) # player.py retorna item como objeto
        if(item is not None):
            self.currentRoom.addItem(item) # room.py usa el metodo addItem agregando a su diccionario 'item'
            print('Tiraste ', item_name)
        else:
            print('Error 404: ', item_name, 'not found in your inventory') # No encuentra el item en el inventario

    def eat(self, command): # Al igual que take y drop, usa la segunda palabra como comando.
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Usar qué?")
            return

        item_name = command.getSecondWord()
        if(item_name is not None):
            if isinstance(self.player.getItemInfo(item_name), Comestible):
                self.player.eatItem(item_name) # Usa el metodo eatItem de player.pi
            else:
                print("No es comestible.")
        else:
            print('Error 404: ', item_name, 'not found in the inventory') # No encuentra el item en el inventario

    def inventory(self):
        print (self.player.getItems()) # Retorna cada item en forma de lista
        self.player.getWeight() # Retorna el peso actual junto al peso máximo


    def quit(self, command):
        if(command.hasSecondWord()):
            print("Sacar qué?")
            return False
        else:
            return True
    
    def charge(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Cargar qué?")
            return

        item_name = command.getSecondWord()
        room = self.currentRoom
        if(item_name in self.player.getItems()):
            if isinstance(self.player.getItemInfo(item_name), Usable):
                item = self.player.getItemInfo(item_name)
                item.addRoom(room)

            else:
                print("El item %s no es usable" % item_name)
        else:
            print('Error 404: %s not found in the inventory' % item_name)
        
    def fire(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Disparar qué?")
            return

        item_name = command.getSecondWord()
        if(item_name in self.player.getItems()):
            if isinstance(self.player.getItemInfo(item_name), Usable):
                item = self.player.getItemInfo(item_name)
                room = item.getRoom()
                if room is not None:
                    self.currentRoom = room
                    print("")
                    self.currentRoom.getLocationInfo()

            else:
                print("El item %s no es usable" % item_name)
        else:
            print ('Error 404: %s not found in the inventory' % item_name)
    def use(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Usar qué?")
            return

        item_name = command.getSecondWord()
        if(item_name in self.player.getItems()):
            item = self.player.getItemInfo(item_name)
            if isinstance(item, Usable):
                for direction in self.currentRoom.getExits():
                    room = self.currentRoom.getExit(direction)
                    if isinstance(room, lockedRoom):
                        item.openDoor(room)
                        print('Abriste la puerta %s con %s' % (room.getDescription(), item.getName()))
                    else:
                        pass
            else:
                print("El item %s no es usable" % item_name)
        else:
            print('Error 404: %s not found in the inventory' % item_name)
        
    def missions(self):
        print('Misiones pendientes: ')
        for x in self.player.getMission():
            print(x.showDescription())

    def speak(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Hablar con quién?")
            return
            
        npc_name = command.getSecondWord()
        npc_list = self.currentRoom.getNPCs()

        if npc_name in npc_list:
            npc = self.currentRoom.getInfoNPC(npc_name)
            if npc is not None:
                print(npc.getName(), ' dice: \n', npc.getSpeech())
            else:
                print('Ese personaje no se encuentra en la sala')
        else:
            print('No se encuentra ese personaje en la sala')
    def give(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Dar qué?")
            return
        
        item_name = command.getSecondWord()
        if(item_name in self.player.getItems()):
            item = self.player.getItemInfo(item_name)
            for x in self.currentRoom.getNPCs(): # Para cada NPC en la habitación
                npc = self.currentRoom.getInfoNPC(x) # Nos devuelve el objeto NPC
                check = npc.reciveItem(item) # Recibe el item y devuelve True si es el que pedía, devuelve False si no es.
                if check is True:
                    reward = npc.getItem() # Premio
        
                    self.player.delItems(item_name) # Eliminamos el item que damos, pero provisoriamente, ya que si el premio que nos devuelve el NPC no cabe en nuestro inventario, necesitamos regresar éste objeto a nuestro inventario

                    objective = self.player.setItem(reward, reward.getName()) # Agregamos el regalo al inventario

                    if objective is None: # Si todo sale bien
                        self.currentRoom.delNPC(npc.getName()) # Eliminamos al NPC de la habitación
                    else: # Si excedemos el peso máximo con el regalo...
                        objective = self.player.setItem(item, item_name) # Volvemos a agregar el primer item a nuestro inventario
                        print('No tienes espacio en el inventario para juntar éste objeto, devolviendolo..')
                        
                else:
                    return
        else:
            print('Error 404: Item not found in the inventory')
    
    def open(self, command):
        if(not command.hasSecondWord()): # Verifica que haya segunda palabra
            print("Dar qué?")
            return
        
        item_name = command.getSecondWord()
        if(item_name in self.currentRoom.getItems()):
            key = self.player.getItemInfo("llave") # Revisa si el jugador tiene la llave, si 

            chest = self.currentRoom.delItems(item_name)
            
            if not key:
                print('No tienes una llave en el inventario para abrir el cofre.')
                return
            else:
                items = chest.openChest(key) # Retorna una lista con items
                for item in items:
                    self.currentRoom.addItem(item) # Agrega cada item de la lista al cuarto y elimina el cofre del cuarto
                print('El cofre ha dejado nuevos items en el cuarto.') # Retorna un mensaje de aviso, de que un nuevo item se encuentra en el cuarto.




            

g = Game()
g.play() 