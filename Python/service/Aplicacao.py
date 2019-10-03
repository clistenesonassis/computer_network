import math
from pyaudio import PyAudio
from utils import Conversor
from Enlace import *
import threading
from Rede import *

##  INPUT  ##
text_input = "a" ## 01100001
text_input2 = "b" ## 01100010

##  ENLACE  ##
rede = Rede()

## CHAMADA DA RED ##

def Sending(destino, dado):
    rede.send(destino, dado)

print("****Transmition Starting! ****")
t1 = threading.Thread( target = Sending, args = ("01", text_input,) )
t2 = threading.Thread( target = Sending, args = ("02", text_input2,) )
t1.start()
t2.start()