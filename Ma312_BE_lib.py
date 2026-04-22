# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:58:52 2024

@author: floal
"""

import sounddevice as sd 
import time 
from scipy.io import wavfile
import numpy as np
from matplotlib.pyplot import *
from numpy.fft import fft
import math
import soundfile as sf
from scipy import signal

#%%

#fonction pour décaler une note 
def jouer_note_decale(data, fe, freq_note):
    fft_data = np.fft.rfft(data) # on calcule la FFT
    freqs = np.fft.rfftfreq(len(data), d=1./fe) #on trouve la fréquence associée
    
    note_freq = freq_note #on décale la FFT 
    shift_amount = note_freq / fe  # on le normalise
    
    fft_decale = np.roll(fft_data, int(len(fft_data) * shift_amount))
    
    signal_reconstruit = np.fft.irfft(fft_decale) # puis on le reconstitue le signal avec la transformée de Fourier inverse
    
    signal_reconstruit /= np.max(np.abs(signal_reconstruit))  # on le normalise 
    
    sd.play(signal_reconstruit, fe) #puis on le joue
    sd.wait() 
    
#%%

def delay (signal , sampling_rate , delay_time = 0.5, feedback = 0.5, mix =0.5) :
    """
    Applique un effet de délai sur le signal .
    : param signal : Le signal audio d ' entrée
    : param sampling_rate : Le taux d'échantillonnage(Hz)
    : param delay_time : Temps de retard en secondes
    : param feedback : Rétroaction(feedback)
    : param mix : Mixage du signal traité ( entre 0 et 1)
    : return : Signal avec l ' effet de délai appliqué
    """
    dtype = str(signal.dtype) 
    delay_samples = int(delay_time * sampling_rate)
    output = np.zeros (len(signal) + delay_samples , dtype=np.float64)
    
    for i in range(len(signal)) :
        output [i] += signal [i]
        if i >= delay_samples:
            output[i] += feedback * output[i - delay_samples]
    # Mixage
    output = (1 - mix) * signal + mix * output [:len(signal)]
    return output.astype(dtype)

#%%

def plot_spectre(signal, samplerate, titre):
    # Calculer la FFT
    freqs = np.fft.rfftfreq(len(signal), d=1/samplerate)
    spectre = np.abs(np.fft.rfft(signal))

    # Tracer le spectre
    figure(figsize=(10, 5))
    plot(freqs, spectre)
    title(title)
    xlabel('Fréquence (Hz)')
    ylabel('Amplitude') 
    grid()
    show()
    
 #%%   convolution en zero-padding
 
def conv_fft(signal,impulse_response) :
    """
    Code utilisant la FFT pour calculer la convolution .
    : param signal : Signal audio d ' entrée ( array NumPy )
    : param impulse_ response : Réponse impulsionnelle(array NumPy)
    : return : Signal audio convolé
    """
    dtype=str ( signal.dtype )
    # Calculer la longueur de la convolution ( signal + IR - 1)
    N = len(signal) + len(impulse_response) - 1
    # Calculer la FFT du signal et de la réponse impulsionnelle avec un zéro-padding
    X = np.fft.rfft(signal , n=N)
    H = np.fft.rfft(impulse_response, n=N)
    # Convolution dans le domaine fréquentiel (multiplication point par point )
    Y = X * H
    # Appliquer la FFT inverse pour revenir au domaine temporel
    y = np.fft.irfft(Y)
    return y [ : len(signal) ].astype(dtype)
 
    
# 2 réponses impultionnelles pour tester    
def impulse_response_echo(delay, gain=0.5):
    """Réponse impulsionnelle d'écho."""
    ir = np.zeros(delay + 1, dtype=np.float32)  # Utiliser float32 pour économiser de la mémoire
    ir[0] = 1  # Amplitude originale
    ir[delay] = gain  # Écho
    return ir

def impulse_response_reverb(length=4410, decay=0.5):
    """Réponse impulsionnelle de réverbération."""
    ir = np.zeros(length, dtype=np.float32)
    ir[0] = 1
    for n in range(1, length):
        ir[n] = decay ** n #décroissance pour faire une reverb
    return ir