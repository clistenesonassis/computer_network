from Rede import *
from Pacote import *

class Transporte:

    def __init__(self, name, destino, dado, tipoDado):
        self.name = name
        self.destino = destino
        self.dado = dado
        self.tipoDado = tipoDado
        self.UDP = "Protocolo UDP"
        self.TCP = "Protocolo TCP"

        ##  ENLACE  ##
        self.rede = Rede()
        self.pacote = Pacote(name, destino, dado)

        self.defineProtocol()
        self.send()

    def defineProtocol(self):
        if( self.tipoDado == "chat"):
            self.pacote.setProtocol(self.TCP)

    def send(self):            
        self.rede.send(self.name, self.destino, self.dado)