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

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 8000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
FREQUENCY = 1000.63 #Hz, waves per second, 261.63=C4-note.
LENGTH = 1 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

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
print(output)
##  CONVERTE CONTEÚDO EM BINÁRIO  ##

##  GERA SOM  ##
som = GeraSom(BITRATE, NUMBEROFFRAMES)
som.emitir(output)
##  GERA SOM  ##