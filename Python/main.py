#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:38:40 2019

@author: onassis
"""

import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 8000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
FREQUENCY = 1000.63 #Hz, waves per second, 261.63=C4-note.
LENGTH = 0.200 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

for x in range(NUMBEROFFRAMES):
   WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))    

#fill remainder of frameset with silence
for x in range(RESTFRAMES): 
    WAVEDATA += chr(128)

p = PyAudio()
stream = p.open(
    format=p.get_format_from_width(1),
    channels=1,
    rate=BITRATE,
    output=True,
    )

for x in range(5):
    stream.write(WAVEDATA)
    

stream.stop_stream()
stream.close()
p.terminate()