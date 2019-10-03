from asyncio import selector_events
from Enlace import *
import threading as thr
from Pacote import *
from Conversor import *

class Rede:

    def __init__(self, mask='255.0'):
        self.enlace = Enlace() # Camada Enlace
        self.rota = { "lu":0.11, "jo":0.101, "ca":1.010 }

    def send(self, address, destino, dados):
        pacote = Pacote(address, self.rota[destino], dados)

        ## Mudando forma de envio do pacote.
        flag = False
        self.enlace.transmission(pacote, flag)
    
    def listening(self):
        msg = ''
        conversor = Conversor()
        while(True):
            receiver = Receiver(1)
            byteRecebido = receiver.listening
            receiver = Receiver(0.5)
            confirmByte = receiver.listening
            
            if( int(confirmByte) ):
                msg += conversor.bin_to_str(byteRecebido)
                print("LISTENING: ", msg)

'''     def receiveAndPrint(self):
    pacoteRecebido = 
    if pacoteRecebido is None:
    self.listening = False
    break
    if pacoteRecebido.destino == self.address:
    print("Sucesso!") '''

'''def start(self):
escritor = thr.Thread(target = self.send)
escritor.start() '''