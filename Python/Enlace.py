from Gerasom import *
import asyncio

class Enlace:

    def __init__(self, msg, origem, destino ):
        self.dados = msg
        self.destino = destino
        self.origem = origem
        s = thread.allocate_lock()

    def transmission(self):
        self.camadaFisica = GeraSom()
        lock = asyncio.Lock()
        lock.acquire()
        try:
            self.camadaFisica.emitir(output)
        finally:
            lock.release()

