import math
import time
from pyaudio import PyAudio
import simpleaudio as sa
from utils.Conversor import *

class GeraSom(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GeraSom, cls).__new__(cls, *args, **kwargs)
            return cls._instance
        return -1

    def __init__(self):
        self.wave_obj_1 = sa.WaveObject.from_wave_file("assets/bit1.wav") # Frequência: 10000hz (apróx.)
        self.wave_obj_0 = sa.WaveObject.from_wave_file("assets/bit0.wav") # Frequência: 2690hz (apróx.)
        self.converter = Conversor()

    def emitir(self, pacote, flag):
        
        if not(flag):
            dado = self.converter.str_to_bin( pacote.dados )
            dado = dado.split()
            
            for byte in dado:
                for bit in byte:
                    if bit == '0':
                        play_obj = self.wave_obj_0.play()
                        play_obj.wait_done()
                        time.sleep(1)
                    elif bit == '1':
                        play_obj = self.wave_obj_1.play()
                        play_obj.wait_done()
                        time.sleep(1)
        ##else:
            ##pasagem convertendo origem, destino e dado em binário