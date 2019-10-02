from Gerasom import *

class Enlace:

    def __init__(self, msg, origem, destino ):
        self.dados = msg
        self.destino = destino
        self.origem = origem
        s = thread.allocate_lock()

    def transmission(self):
        self.camadaFisica = GeraSom()
        self.colisao
