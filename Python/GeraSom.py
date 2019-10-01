import math
import time
from pyaudio import PyAudio
import simpleaudio as sa

class GeraSom:
    
    def __init__(self, b, nf):
        self.bitrate = b
        self.numFrames = nf
        self.WAVEDATA = '' 
        self.wave_obj_1 = sa.WaveObject.from_wave_file("assets/beep-04.wav")
        self.wave_obj_0 = sa.WaveObject.from_wave_file("assets/beep-02.wav")

        '''
        self.p = PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(1),
            channels = 1,
            rate = self.bitrate,
            output = True,
            )
        '''

    def emitir(self, string):

        ## tamanho do binário
        binario = str(string)
        self.tamanhoArquivo = int( len(binario) )
        msg = ""

        print(binario)

        for b in binario:
            if b == '0':
                msg += "0"
                play_obj = self.wave_obj_0.play()
                play_obj.wait_done()
            elif b == '1':
                msg += "1"
                play_obj = self.wave_obj_1.play()
                play_obj.wait_done()
            elif b == ' ':
                msg += ' '
            
        print(msg)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


    def reproduzir(self, frequency):

        '''
        for x in range(self.numFrames):
            self.WAVEDATA += chr(int(math.sin(x / ((self.bitrate / frequency) / math.pi)) * 127 + 128))

        for x in range(self.tamanhoArquivo):
            self.stream.write(self.WAVEDATA)
            time.sleep(0.2)
            print(x)
            if(x == 3):
                return 0
        
        self.WAVEDATA = ''
        '''

        play_obj = self.wave_obj_1.play()
        play_obj.wait_done()
    