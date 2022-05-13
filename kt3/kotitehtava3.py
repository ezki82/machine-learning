import numpy as np
import matplotlib.pyplot as plt

""" Tehdään ensin numpyllä kaksi sinimuotoista signaalia
    kerrotaan ne keskenään ja piirretään matplotlibin avulla
    nuo kaksi signaalia yhteen kuvaan ja tulos toiseen kuvaan"""

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)   # start = 0, stop = 1sekuntti ja steppi = Ts
N = t.size
#print(t), # jos haluat katsoa millainen 1000 näytteen mittainen "vektori" syntyi

f1 = 10
f2 = 15
sig1 = np.sin(2*np.pi*f1*t)
sig2 = np.sin(2*np.pi*f2*t)
tulo = sig1*sig2

# 25 Hz suodatetaan pois
suodatin = np.ones((40,)) # Eli tehdään pystyvektori, jossa 40 kpl ykkösiä
suodatettu = np.convolve(tulo,suodatin,mode='same')
plt.figure(4)
plt.plot(t, suodatettu)

plt.figure(1)
plt.plot(t,sig1)
plt.plot(t,sig2)

plt.figure(2)
plt.plot(t,tulo)
plt.title('Tuloksena pitäisi olla 5 Hz ja 25 Hz signaalit')
plt.show()

""" Sinun tehtävänä on todistaa, että tuloksena on todella 5 Hz ja 25 Hz signaalit. 
    Sen voi tehdä joko siten, että suodattaa 25 Hz taajuisen signaalin täysin pois
    suodattimella joka summaa 40 peräkkäistä näytettä (1000&25 = 40 eli yhdestä 25 Hz 
    signaalin jaksosta ehditään ottaa 40 näytettä. Koska puolet noista näytteistä on 
    positiivisia ja puolet negatiivisia, niin jos suodatus tulos on aina summa 40
    perättäisen näytteen yli, niin 25 Hz signaali poistuu täysin ja jäljelle jää
    5 Hz signaali (1000/5 = 200, joten tämä signaali vain vahvistuu suodattimen läpi
    mennessään, mutta taajuus pysyy samana. 
    
    Toinen tapa todistaa, että tulossa on nuo kaksi komponenttia on laskea tulo signaalista
    sen taajuus sisältö fourier muunnoksella. Sekin löytyy NumPystä.
    
    Molemmista tavoista on tässä alla nyt vähän esimerkkiä, teidän tulee vain kokeilla
    ja soveltaa

    suodatin = np.ones((40,)) # Eli tehdään pystyvektori, jossa 40 kpl ykkösiä
    suodatettu = np.convolve(tulo,suodatin,mode='same')
    
"""

taajuussisalto = np.fft.fft(tulo)  #tuloksena on kompleksinen signaali, missä
                                   # reaali osa kertoo kuinka paljon eri taajuuksilla oli
                                   # cos signaalin vaiheessa olevaa komponenttia
                                   # ja imaginääri osa kertoo kuinka paljon eri taajuuksilla
                                   # oli sini signaalin vaiheessa olevaa komponenttia
                                   # FFT:n tuloksena on yhtä monta taajuuspistettä, kuin
                                   # näytteitä oli inputtina annetussa signaalissa.
                                   # Jos näytteitä on N kpl ja näytetaajuus on Fs, niin
                                   # ensimmäinen FFT tulos taajuussisalto[0] = 0 Hz
                                   # seuraavat tulokset ovat taajuussisalto[1] = Fs/N = 1000/1000 = 1Hz
                                   # taajuussisalto[499] = 
xakseli = Fs/N*np.arange(0,Fs/2,Fs/N) 
taajuuteenAsti = 500 
plt.figure(3)
plt.semilogy(xakseli[0:taajuuteenAsti],np.abs(taajuussisalto[0:taajuuteenAsti]))
plt.show()
plt.close()

print(taajuussisalto[499:501])
