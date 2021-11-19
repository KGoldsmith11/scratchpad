#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:08:14 2020


@author: kathleengoldsmith
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from scipy import signal

t = np.linspace(0, 1, 2001)

sig_5Hz = np.sin(2*np.pi*5*t)
sig_250Hz = np.sin(2*np.pi*250*t)


# lets combine the signals 
sig_5Hz_250hz = sig_5Hz + sig_250Hz
#plt.plot(sig_5Hz_250hz)
#plt.show()

#### Computing signal mean - demean a periodic signal 
signal_mean = np.mean(sig_5Hz)
print(signal_mean)

#### Computing signal to noise ratio = mean/std
# CV - coefficient of variation is mean/std *100
# What about for non stationary signals? Non perioding?

#### QUANTISATION: 
# Continous signals are converted using an ADC to convert analouge to digital. DAC does the opposite.
# Information management - what information we need to keep and what we cant afford to lose. 
# 
