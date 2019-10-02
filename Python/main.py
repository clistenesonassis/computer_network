#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio
from Conversor import *
from Python.Enlace import *
import threading
#from aloha import *


##  INPUT  ##
text_input = "a" ## 01100001

##  ENLACE  ##
enlace = Enlace()

##  CONVERTE CONTEÚDO EM BINÁRIO  ##

converter = Conversor()
output = converter.str_to_bin( text_input )

## CHAMADA DO ENLACE ##


print(" * Starting recording... * ")
print("Entrada em texto: ", output)

