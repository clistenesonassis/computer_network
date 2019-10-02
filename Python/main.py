#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:38:40 2019

@author: onassis
"""

import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio
from GeraSom import *
from Conversor import *
from Receiver import *
import threading
#from aloha import *


##  INPUT  ##
text_input = "oi, Guido!"
## 01100001

##  INPUT  ##

##  Listening  ##
listening = Receiver()
##  Listening  ##

##  CONVERTE CONTEÚDO EM BINÁRIO  ##

converter = Conversor()
output = converter.str_to_bin( text_input )
##  CONVERTE CONTEÚDO EM BINÁRIO  ##

##  GERA SOM  ##


'''def test1():
    som = GeraSom()
    print("test1: ", som)

def test2():
    som2 = GeraSom()
    print("test2: ", som2)

t1 = threading.Thread( target = test1, args =() )
t2 = threading.Thread( target = test2, args = () )
t1.start()
t2.start()'''

som = GeraSom()
som.emitir(output)
#print(" * Starting recording... * ")
print("Entrada em texto: ", output)
##  GERA SOM  ##
