from GeraSom import *
import asyncio
import threading
from multiprocessing.pool import ThreadPool
from Receiver import *
from Pacote import *
from Conversor import *

class Enlace:

    def __init__(self):
        self.camadaFisica = GeraSom()
        self.sem = threading.Semaphore()
        self.conversor = Conversor()
        self.correctByte = False

    def transmission(self, pacote, flag):
        self.sem.acquire()
        dadoRecebido = ''
        try:
            for palavra in pacote.quantDados:
                for letra in palavra:
                    while not( self.correctByte ):
                        receiver = Receiver(1)
                        pool = ThreadPool(processes=1)
                        async_call = pool.apply_async(receiver.listening)
                        self.camadaFisica.emitir(letra, flag)
                        arquivoRecebido = async_call.get()
                        arquivoRecebido = self.conversor.bin_to_str( arquivoRecebido )

                        if( arquivoRecebido == letra ):
                            self.correctByte = True
                            print("arquivo Recebido: ", arquivoRecebido)
                            dadoRecebido += arquivoRecebido
                            self.camadaFisica.correct( self.correctByte )
                        else:
                            self.camadaFisica.correct( self.correctByte )
                    self.correctByte = False
                            
            print("MENSAGEM FINAL RECEBIDA:", dadoRecebido)

        finally:
            self.sem.release()

