import math
from pyaudio import PyAudio
from Conversor import *
from Enlace import *
import threading
from Rede import *
from Receiver import *
from Conversor import *

##  INPUT  ##
text_input = input("Insira uma mensagem: ") ## 01100001
text_input2 = "ta" ## 01100010
text_input3 = "bom" ## 01100110 

##  ENLACE  ##
rede = Rede()
## CHAMADA DA RED ##

def Sending(destino, dado):
    rede.send(t1.name, destino, dado)

def listening(self):
    msg = ''
    conversor = Conversor()
    while(True):
        receiver = Receiver(1)
        byteRecebido = receiver.listening
        receiver = Receiver(0.5)
        confirmByte = receiver.listening
        
        if(confirmByte):
            msg += conversor.bin_to_str(byteRecebido)
            print("LISTENING: ", msg)

print("****Transmition Starting! ****")

t1 = threading.Thread( name = "lu", target = Sending, args = ("jo", text_input,) )
#t2 = threading.Thread( name = "jo", target = listening, args = () )
#t3 = threading.Thread( name = "ca", target = Sending, args = ("03", text_input3,) )

t1.start()
#t2.start()
#t3.start()

print("### ### ID DA THREAD: ", t1.ident)
#print("### ### ID DA THREAD: ", t2.ident)
#print("### ### ID DA THREAD: ", t3.ident)