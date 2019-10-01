"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import numpy as np
import threading
import time

class Receiver:

    def __init__(self):
        self.CHUNK = 5000
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 10
        self.mensagem = ''

        # use a Blackman window
        self.window = np.blackman( self.CHUNK )

        # Criando instância do pyaudio
        self.p = pyaudio.PyAudio()

        # Criando Fluxo de midia
        self.stream = self.p.open(format = self.FORMAT,
                            channels = self.CHANNELS,
                            rate = self.RATE,
                            input = True,
                            frames_per_buffer = self.CHUNK,
                            )

        # Array para armazenar audio
        self.frames = []

        t = threading.Thread( target = self.listening )
        t.start()

    def listening(self):
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read( self.CHUNK )
            self.frames.append(data)

            # write data out to the audio stream
            #self.stream.write(data)

            # unpack the data and times by the hamming window
            indata = np.array(wave.struct.unpack("%dh"%(len(data)/2),\
                                                data))

            # Take the fft and square each value
            fftData=abs(np.fft.rfft(indata))**2

            # find the maximum
            which = fftData[1:].argmax() + 1

            # use quadratic interpolation around the max
            if which != len(fftData)-1:
                y0,y1,y2 = np.log(fftData[which-1:which+2:])
                x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
                # find the frequency and output it
                thefreq = ( which + x1 ) * self.RATE / self.CHUNK
                

                if( thefreq > 2000 and thefreq < 3500 ):
                    self.mensagem += '0'
                    print ( "The freq is %f Hz." % (thefreq) )
                elif( thefreq > 8000 and thefreq < 12000 ):
                    self.mensagem += '1'
                    print ( "The freq is %f Hz." % (thefreq) )
            else:
                thefreq = which * self.RATE / self.CHUNK
                

                if( thefreq > 2000 and thefreq < 3500 ):
                    self.mensagem += '0'
                    print ( "The freq is %f Hz." % (thefreq) )
                elif( thefreq > 8000 and thefreq < 12000 ):
                    self.mensagem += '1'
                    print ( "The freq is %f Hz." % (thefreq) )
                    
        print(" * done recording * ")
        print(self.mensagem)

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()