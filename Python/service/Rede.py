from asyncio import selector_events
from Enlace import *
import threading as thr
from utils.Pacote import *

class Rede:

    def __init__(self, address='0.0', mask='255.0'):
        self.enlace = Enlace() # Camada Enlace
        self.address = address # endereço a ser atribuido como próprio
        self.rota = {"1":"Sachine Tendulkar", "2":"Dravid", "3":"Sehwag", "4":"Laxman","5":"Kohli"}

    def send(self, destino, dados):
        pacote = Pacote(self.address, destino, dados)
        self.rota = destino

        ## Mudando forma de envio do pacote.
        flag = False
        self.enlace.transmission(pacote, flag)

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