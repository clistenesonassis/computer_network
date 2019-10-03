from GeraSom import *
import asyncio
import threading
from utils.Receiver import *
from utils.Pacote import *

class Enlace:

    def __init__(self):
        self.camadaFisica = GeraSom()
        self.sem = threading.Semaphore()

    def transmission(self, pacote, flag):
        self.sem.acquire()
        #self.tamDado = pacote.tamanhodados
        try:
            receiver = Receiver(10)
            t = threading.Thread( target = receiver.listening, args = () )
            t.start()
            self.camadaFisica.emitir(pacote, flag)
            t.join()
        finally:
            self.sem.release()

