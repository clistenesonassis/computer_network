#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:38:40 2019

@author: onassis
"""

import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio
from Python.GeraSom import *
from Python.Conversor import *
from Python.Receiver import *
from Python.aloha import *


##  INPUT  ##
text_input = "a"
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
som = GeraSom()
print("Entrada: ", output)
print("Saida: ", som.emitir(output))
print("Saida em texto: ", converter.bin_to_str( output ))
print("Entrada em texto: ", text_input)
##  GERA SOM  ##
