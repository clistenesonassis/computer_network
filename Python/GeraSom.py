import math
import time
from pyaudio import PyAudio
import simpleaudio as sa

class GeraSom(object):

    '''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GeraSom, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    '''

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GeraSom, cls).__new__(cls, *args, **kwargs)
            return cls._instance
        return -1

    def __init__(self):
        self.wave_obj_1 = sa.WaveObject.from_wave_file("assets/bit1.wav") # Frequência: 10000hz (apróx.)
        self.wave_obj_0 = sa.WaveObject.from_wave_file("assets/bit0.wav") # Frequência: 2690hz (apróx.)
        self.numero = 5

    def emitir(self, string):

        ## tamanho do binário
        binario = str(string)
        self.tamanhoArquivo = int( len(binario) )

        for b in binario:
            if b == '0':
                play_obj = self.wave_obj_0.play()
                play_obj.wait_done()
                time.sleep(0.3)
            elif b == '1':
                play_obj = self.wave_obj_1.play()
                play_obj.wait_done()
                time.sleep(0.3)