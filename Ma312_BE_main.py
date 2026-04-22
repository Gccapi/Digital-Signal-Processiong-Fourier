# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:34:38 2024

@author: floal
"""

from scipy import signal
from numpy.fft import fft
from scipy.io import wavfile
from matplotlib.pyplot import *

import numpy as np
import sounddevice as sd 
import soundfile as sf

import os 

import Ma312_BE_lib as lib #on importe le document lib où est la fonction de décalage

"""
Exemple importation de fichier .wav
"""
# On construit le chemin vers le fichier "drum.wav" dans le fichier "Data" que l'on veut ouvrir
file_path = os.path.join('Data', 'drum.wav')

# Lecture du fichier audio et récupère la fréquence d'échantillonnage (fe) et des données audio
fe, data = wavfile.read(file_path)

# On joue l'audio récupéré grace aux données audio et la fréquence d'échantillonnage (data) et (fe)
sd.play(data, fe)  


"""
Exemple de prise de son en direct avec le micro de l'ordinateur
"""
fe = 44000 # on définit de la fréquence d'échantillonnage à 44 000 Hz
duree = 5  # et la durée de l'enregistrement à 5 secondes
monenregistrement = sd.rec(int(duree*fe), samplerate=fe, channels=2)  # Enregistrement d'un son pendant la durée spécifiée
sd.wait()  # Attend la fin de l'enregistrement
sd.play(monenregistrement, fe)  # on lit de l'enregistrement à la fréquence d'échantillonnage définie plus haut


"""
Test d'un signal avec addition de plusieurs fréquences
"""
amplitude = 2 # ≈ volume du son.
freq1 = 523   # Fréquence de la première sinusoïde (523 Hz = DO5)
freq2 = 659   # Fréquence de la deuxième sinusoïde (659 Hz = MI5)
freq3 = 392   # Fréquence de la troisième sinusoïde (392 Hz = SOL4)
duree = 2     # Durée du signal généré toujours en secondes
fe = 44100

t = np.linspace(0, duree, fe*duree)  # Génération d'une grille de temps.
signal = (amplitude * np.sin(2 * np.pi * t * freq1)  
          + amplitude * np.sin(2 * np.pi * t * freq2)  
          + amplitude * np.sin(2 * np.pi * t * freq3))  # on génère un signal en additionnant les trois sinusoïdes de fréquences différentes 
sd.play(signal)         # et on le joue

te = 1.0 / fe          # Calcul de la période d'échantillonnage
n = signal.size        # Réécupère la taille du signal
t2 = np.arange(n) * te # Génération des points temporels
figure()               # on crée une nouvelle figure pour dessiner un graphique 
plot(t2, signal)       # tracé du signal dans le domaine temporel
xlabel("t(s)")         # donne un nom à l'axe des abscisses (temps en seconde)
ylabel("amplitude")    # et à l'axe des ordonnées (amplitude du signal)
axis([0, 0.05, signal.min()-2, signal.max()+2])  # on définie les limites des axes
grid()                 # ajoute une grille en fond du graphique
print(signal.max())    # affiche dans la console la valeur de l'amplitude maximale du signal

#%%
amplitude = 2  
duree = 2  
fe = 44100  
t = np.linspace(0, duree, fe*duree)  
triangle = signal.sawtooth(2*np.pi*100*t, 0.5)  # on génère un signal triangulaire (=sawtooth)
sd.play(triangle)
te = 1.0 / fe  
n = triangle.size  
t2 = np.arange(n) * te  
figure()  
plot(t2, triangle)  
xlabel("t(s)")  
ylabel("amplitude")  
axis([0, 0.1, triangle.min()-2, triangle.max()+2])  
grid()  #de même, on génère un graphique pour tracer dans le domaine temporel le spectre du signal

#%%
amplitude = 2  
duree = 2  
fe = 44100  
t = np.linspace(0, duree, fe*duree)  
square = signal.square(2*np.pi*300*t, 0.5)  # génération d'un signal carré 
sd.play(square)  
te = 1.0 / fe  
n = square.size  
t2 = np.arange(n) * te  
figure()  
plot(t2, square)  
xlabel("t(s)")  
ylabel("amplitude")  
axis([0, 0.1, square.min()-2, square.max()+2])  
grid()  

"""
"A vous dirais-je maman" généré avec différentes notes jouées une par 
une avec un certain tempo imposé et des pauses pour former un rythme.
"""
tempo=1/2
amplitude=1
echantillonage=44100
temps=tempo/4
pause=np.linspace(0,temps,int(echantillonage*temps))

freq=262 # do
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ([ note , pause , note ])
sd.play(signal)

freq=392 # sol
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ([ signal , pause , note , pause , note ] )
sd.play(signal)

freq=440 # la
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note , pause , note ] )
sd.play(signal)

freq=392 # sol
temps=tempo
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note ] )
sd.play(signal)

freq=349 # fa
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , 1.5*pause , note , pause , note ] )
sd.play(signal)

freq=330 # mi
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note , pause , note ] )
sd.play(signal)

freq=294 # re
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note , pause , note ] )
sd.play(signal)

freq=262 # do
temps=tempo
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note ] )
sd.play(signal)

freq=392 # sol
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , 1.5*pause , note , pause , note ] )
sd.play(signal)

freq=349 # fa
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note , pause , note ] )
sd.play(signal)

freq=330 # mi
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note , pause , note , pause , note ] )
sd.play(signal)

freq=294 # re
temps=tempo/2
t=np.linspace(0,temps,int(echantillonage*temps))
note=amplitude* np.sin(2* np.pi *t* freq )
signal=np.block ( [ signal , pause , note ] )
sd.play(signal)


"""
Même musique mais jouée à l'aide d'une boucle, 2 listes 
et génère les notes par une fonction et pas une par une
"""    
#définition de chaque fréquence pour toutes les notes d'une gamme de do
do  = 261.63
re  = 293.66
mi  = 329.63
fa  = 349.23
sol = 392
la  = 440
si  = 493.78

# Paramètres de la mélodie
tempo = 1/2
amplitude = 1
echantillonage = 44100
pause_duree = tempo / 4  # Durée d'une pause entre les notes
pause = np.zeros(int(echantillonage * pause_duree))  # Signal de silence (pour les pauses)

# Fonction pour générer une note
def generer_note(freq, duree, echantillonage):
    t = np.linspace(0, duree, int(echantillonage * duree), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

# Séquence des notes et leurs durées (en unités de tempo défini plus haut)
partition = [do, do, sol, sol, la, la, sol, fa, fa, mi, mi, re, re, do]
durees = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Création du signal complet
signal_complet = np.array([])

#boucle qui se répète autant de fois qu'il y a de valeur dans la liste "partition"
for i in range(len(partition)):
    duree_note = tempo / durees[i]
    note = generer_note(partition[i], duree_note, echantillonage)
    signal_complet = np.concatenate((signal_complet, note, pause))

# Lecture de la mélodie
sd.play(signal_complet, echantillonage)
sd.wait()

"""
Importation d'un fichier et tracé en fréquenciel
"""
file_path = os.path.join('Data', 'guitare1.wav') # Comme sur le premier exemple, récupère le chemin du fichier "guitare1.wav" et on l'importe
fe, data = wavfile.read(file_path) 

# On extrait le nom du fichier sans l'extension pour l'ajouter automatiquement dans le titre du graphe plus tard 
nom_fichier = os.path.splitext(os.path.basename(file_path))[0]
print(f"Taille de l'array de {nom_fichier} :", data.shape) #affiche dans la console (nombre d'échantillons, nombre de canaux) on a ici 383407 échantillons pour 2 canaux (=stéréo)



# On vérifie que le fichier est stéréo
if len(data.shape) > 1:
    print("Le fichier est stréreo")
    canal_gauche = data[:, 0]  # Premier canal (gauche)
    canal_droit = data[:, 1]    # Deuxième canal (droit)

    # on applique la FFT
    fft_gauche = np.fft.rfft(canal_gauche)
    fft_droit = np.fft.rfft(canal_droit)


    freqs = np.fft.rfftfreq(len(canal_gauche), d=1./fe) # puis on calcule les fréquences correspondantes

    figure(figsize=(12, 6)) # Tracer les spectres de fréquence

    # Spectre de fréquence pour le canal gauche
    subplot(2, 1, 1)
    plot(freqs, np.abs(fft_gauche), color='blue')
    title(f'Spectre de Fréquence - {nom_fichier} Canal Gauche')
    xlabel('Fréquence (Hz)')
    ylabel('Amplitude')
    tight_layout()  # Ajuste les graphes pour ne pas se chevaucher
    grid()

    # Spectre de fréquence pour le canal droit
    subplot(2, 1, 2)
    plot(freqs, np.abs(fft_droit), color='orange')
    title(f'Spectre de Fréquence - {nom_fichier} Canal Droit')
    xlabel('Fréquence (Hz)')
    ylabel('Amplitude')
    grid()
    tight_layout()
    show()
else:
    print("Le fichier audio est mono")
    # on applique donc la FFT au seul canal
    fft_mono = np.fft.rfft(data)

    freqs = np.fft.rfftfreq(len(data), d=1./fe) # Calcul des fréquences

    # Tracer le spectre de fréquence
    figure(figsize=(12, 6))
    plot(freqs, np.abs(fft_mono), color='green')
    title(f'Spectre de Fréquence - {nom_fichier}')
    xlabel('Fréquence (Hz)')
    ylabel('Amplitude')
    grid()
    tight_layout()
    show()

"""
On peut utiliser le même code mais en appliquant la transformée de fourier rapide 
sur un échantillon qui est la plus grande contenue dans la taille de notre array 
"""
file_path = os.path.join('Data', 'guitare1.wav')
fe, data = wavfile.read(file_path)

nom_fichier = os.path.splitext(os.path.basename(file_path))[0]
print(f"Taille de l'array de {nom_fichier} :", data.shape)


canal_gauche = data[:, 0]
canal_droit = data[:, 1]


# on veut trouver la plus grande puissance de 2 dans la taille de notre array
n = len(canal_gauche)
puissance_de_2 = 1 << (n - 1).bit_length()


if puissance_de_2 > n: #on vérifie que la puissance de dépasse pas la taille de l'array sinon on prend celle d'avant
   puissance_de_2 //= 2
   
   print("La plus grande puissance de 2 est : ", puissance_de_2)

    # Extraire les données de chaque canal jusqu'à la valeur de la plus grande puissance de 2 trouvée
   canal_gauche_2 = canal_gauche[:puissance_de_2]
   canal_droit_2 = canal_droit[:puissance_de_2]

    # On applique la RFFT
   fft_gauche = np.fft.rfft(canal_gauche_2)
   fft_droit = np.fft.rfft(canal_droit_2)

   freqs = np.fft.rfftfreq(len(canal_gauche_2), d=1./fe)

   figure(figsize=(12, 6))

    # Tracé pour spectre de fréquence pour le canal gauche
   subplot(2, 1, 1)
   plot(freqs, np.abs(fft_gauche), color='blue')
   title(f'Spectre de Fréquence - {nom_fichier} Canal Gauche (plus grande puissance de 2)')
   xlabel('Fréquence (Hz)')   
   ylabel('Amplitude')
   grid()

    # Tracé pour spectre de fréquence pour le canal droit
   subplot(2, 1, 2)
   plot(freqs, np.abs(fft_droit), color='orange')
   title(f'Spectre de Fréquence - {nom_fichier} Canal Droit (plus grande puissance de 2)')
   xlabel('Fréquence (Hz)')
   ylabel('Amplitude')
   grid()
    
   tight_layout()
    
   show()

#%% On peut aussi retrouver la note jouée par auto-corrélation 

# Fonction pour charger les notes MIDI et leurs noms depuis le txt qui les liste
def charger_notes(fichier):
    notes = {}
    # On ouvre le fichier spécifié en mode lecture seule
    with open(fichier, 'r') as file:
        # Puis on parcourt chaque ligne du fichier
        for line in file:
            index, name = line.split(": ")  # On sépare la ligne entre note MIDI et note en francais 
            # Convertit l'index en entier et ajoute l'entrée au dictionnaire
            notes[int(index)] = name.strip().strip('"')
    return notes

file_path = os.path.join('Data', 'guitare1.wav')
fe, data = wavfile.read(file_path)

nom_fichier = os.path.splitext(os.path.basename(file_path))[0]

# Vérification du format de l'audio
if len(data.shape) == 1:  # Mono
    canal_gauche = data
else:  # Stéréo
    canal_gauche = data[:, 0]  # On utilise le canal gauche ici

# Normalisation
canal_gauche = canal_gauche / np.max(np.abs(canal_gauche))

# On calcule l'auto-corrélation
auto_corr = np.correlate(canal_gauche, canal_gauche, mode='full')

# On la dérive
derivative = np.diff(auto_corr)

# Trouver les pics dans la dérivée
peaks = np.where((derivative[:-1] > 0) & (derivative[1:] <= 0))[0] + 1  

# Calculer les intervalles entre les grands pics
threshold = np.max(auto_corr) * 0.5  # Seuil pour considérer un pic "grand"
grand_pics = peaks[auto_corr[peaks] > threshold]


# On récupère toutes les notes MIDI et le nom en francais qui leur correspond
chemin_MIDI = os.path.join('Data', 'notes_MIDI.txt')
notes_midi = charger_notes(chemin_MIDI)


if len(grand_pics) >= 2:
    interval = grand_pics[1] - grand_pics[0]
    frequency = fe / interval  # Fréquence de la note
    note_nombre = 69 + 12 * np.log2(fe / 440.0)  # Note MIDI
    note_nom = int(round(note_nombre))  # Arrondi pour avoir la note MIDI la plus proche
    
    # Puis on retrouve le nom de la note en français grâce au fichier qui les combine toutes
    if note_nom in notes_midi:
        print(f"La note est donc : {notes_midi[note_nom]}")
    else:
        print("Note non reconnue, il faut vous accorder.")
else:
    print("On ne peut pas déterminer la note, pas assez de pics détectés.")


#on peut aussi tracer graphiquement l'auto-corrélation et lire nous même en vérifiant la fréquence
 
"""
Reconstruire un son après avoir enlevé certaines fréquences
"""
file = os.path.join('Data', 'guitare1.wav')
fe, data = wavfile.read(file)

# On utilise toujours le canal de gauche ici
canal_gauche = data[:, 0]

# on recalcule la FFT et les fréquences 
fft_gauche = np.fft.rfft(canal_gauche)
freqs = np.fft.rfftfreq(len(canal_gauche), d=1./fe)

# On ajoute une copie pour appliquer le filtre sans modifier l'original
fft_filtrée = np.copy(fft_gauche)

# on supprime certaines fréquences ici de 0 à 500
frequences_a_supprimer = (freqs >= 0) & (freqs <= 500)
fft_filtrée[frequences_a_supprimer] = 0

# on reconsturit le signal avec la transformée de Fourier inverse
canal_reconstruit = np.fft.irfft(fft_filtrée)

canal_reconstruit /= np.max(np.abs(canal_reconstruit))  # Normaliser entre -1 et 1

sd.play(canal_reconstruit, fe)
sd.wait()  

#puis on trace le spectre d'origine et le spectre filtré pour les comparer
figure(figsize=(12, 6))

# Spectre original
subplot(2, 1, 1)
plot(freqs, np.abs(fft_gauche), color='blue')
title('Spectre de Fréquence Original')
xlabel('Fréquence (Hz)')
ylabel('Amplitude')
grid()

# Spectre filtré
subplot(2, 1, 2)
plot(freqs, np.abs(fft_filtrée), color='orange')
title('Spectre de Fréquence Filtrée')
xlabel('Fréquence (Hz)')
ylabel('Amplitude')
grid()

tight_layout()
show()

"""
Exemple d'utilisation décalage de note
"""
file_path = os.path.join('Data', 'guitare1.wav')
fe, data = wavfile.read(file_path)

# Supposons que l'on utilise le canal gauche
canal_gauche = data[:, 0]
    
lib.jouer_note_decale(canal_gauche, fe, 523) #on utilise la fonction de décalage pour jouer avec le son de guitare un DO (523 Hz)

#%%

file_path = os.path.join('Data', 'piano.wav')
fe, data = wavfile.read(file_path)

signal_effet = lib.delay(fe, data) 

sd.play(signal_effet, data)
sd.wait()

#%% Modification d'un son avec un delay
file_path = os.path.join('Data', 'piano.wav')
fe, data = sf.read(file_path)

# on applique l'effet de délai sur chaque coté du stéréo, 

#ATTENTION AUX OREILLES MODIFICATEURS A FOND A DROITE

delayed_signal_l = lib.delay(fe[:, 0], data,0.5,1,1)
delayed_signal_r = lib.delay(fe[:, 1], data,0.5,5,5)
delayed_signal = np.column_stack((delayed_signal_l, delayed_signal_r))

# puis on calcule les spectres
freqs = np.fft.rfftfreq(len(fe), d=1/data)
fft_original_l = np.abs(np.fft.rfft(fe[:, 0]))
fft_original_r = np.abs(np.fft.rfft(fe[:, 1]))
fft_delayed_l = np.abs(np.fft.rfft(delayed_signal[:, 0]))
fft_delayed_r = np.abs(np.fft.rfft(delayed_signal[:, 1]))

# pour jouer le fichier audio avec effet de délai
sd.play(delayed_signal, data)
sd.wait()

figure(figsize=(10, 8))

# Spectre original
subplot(2, 1, 1)
plot(freqs, fft_original_l, color='blue', label='Gauche')
plot(freqs, fft_original_r, color='orange', label='Droite')
title('Spectre de Fréquence Original')
xlabel('Fréquence (Hz)')
ylabel('Amplitude')
xlim(0, data/14)
grid()
legend()

# Spectre avec délai
subplot(2, 1, 2)
plot(freqs, fft_delayed_l, color='blue', label='Gauche')
plot(freqs, fft_delayed_r, color='orange', label='Droite')
title('Spectre de Fréquence avec Délai')
xlabel('Fréquence (Hz)')
ylabel('Amplitude')
xlim(0, data/14)
grid()
legend()
tight_layout()
show()

#%% 

file_path = os.path.join('Data', 'piano.wav')
fe, data = wavfile.read(file_path)

fe = np.ravel(fe)  # Aplatir le signal pour gagner en mémoire (le son ne voulait pas être joué autrement)

# Appliquer les réponses impulsionnelles
echo_ir = lib.impulse_response_echo(delay=22050)  # Écho de 0.5 seconde
reverb_ir = lib.impulse_response_reverb(length=44100, decay=0.9)  # Réverbération de 0.1 seconde

# Convoler le signal avec l'écho et la réverbération
signal_echo = lib.conv_fft(fe, echo_ir)
signal_reverb = lib.conv_fft(fe, reverb_ir)

signal_echo /= np.max(np.abs(signal_echo))  # Normalisation de l'écho
signal_reverb /= np.max(np.abs(signal_reverb))  # Normalisation de la réverbération

# ON joue les résultats en ajoutant un facteur, les modifications ayant fait ralentir le tout, même l'original ? vient de la convolution ?
factor = 2.0 
print("Jouer le signal d'origine...")
sd.play(fe, data*factor)
sd.wait()

print("Jouer le signal avec écho...")
sd.play(signal_echo, data*factor)
sd.wait()

print("Jouer le signal avec réverbération...")
sd.play(signal_reverb, data*factor)
sd.wait()

# puis on trace les signaux
figure(figsize=(10, 6))

# Signal original
subplot(3, 1, 1)
plot(fe)
title('Signal Original')
xlabel('Échantillons')
ylabel('Amplitude')
xlim(604600, 604810)
grid()

# Signal avec écho
subplot(3, 1, 2)
plot(signal_echo)
title('Signal avec Écho')
xlabel('Échantillons')
ylabel('Amplitude')
xlim(604600, 604810)
grid()

# Signal avec réverbération
subplot(3, 1, 3)
plot(signal_reverb)
title('Signal avec Réverbération')
xlabel('Échantillons')
ylabel('Amplitude')
xlim(604600, 604810)
grid()

tight_layout()
show()
