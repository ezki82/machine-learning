'''
Tehtävät:
1. Lue kuva4.csv tiedosto pandas kirjaston avulla ja muuta se numpy arrayksi esimerkin mukaisesti

2. Selvitä, minkä kokoinen kuva on ja muokkaa siitä 28x28 pikselin kokoinen kuva, jonka tulostat
   matplotlib kirjaston plt.imshow -komennolla.

3. Selvitä internetistä, kuinka sigmoid funktio voidaan toteuttaa pythonilla ja numpyllä. Tee siitä 
   aliohjelma ja testaa sen toiminta syöttämällä aliohjelmaan sisälle numpy array, jossa 100 kpl
   arvoja -20 ja +20 väliltä. Käytä np.linspace -funktiota tuon datan tekemiseen. Ja lopuksi tulosta
   kuva plt.plot(x,y) -komennolla, missä x = tekemäsi input data ja y = sigmoid funktiosi output.

4. Selvitä (anna opettajan kertoa), miten 784,30,10 -kokoisen neuroverkon output lasketaan. Toteuta tuo laskenta
   numpyn matmul -komentoa ja tekemääsi sigmoid funktiota hyödyntäen. Saat opetetun neuroverkon parametrit w1,w2
   b1, b2 luettua vastaavista csv tiedostoista. Ja lopuksi tulosta neuroverkon kuvasta 4 laskema tulos.

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

# max pooling testi
import skimage.measure

# def sigmoid(xMat):                           # tähän voit toteuttaa sigmoid funktiosi.
#    return [1/(1+np.exp(-x)) for x in xMat]

def sigmoid(x):                           # tähän voit toteuttaa sigmoid funktiosi.
   return 1/(1+np.exp(-x))

# sigmoid testi
# sigmoidTestX = np.linspace(-20, 20, 100)
# sigmoidTestY = sigmoid(sigmoidTestX)
# plt.plot(sigmoidTestX, sigmoidTestY)
# plt.show()

df = pd.read_csv('kt7\\kuva4.csv',header=None)  # näin saadaan luettua kaikki rivit
a0 = df.to_numpy()  
print("a0 shape:")                       # activation a0 tätä voidaan käyttää neuroverkon inputtina
print(a0.shape)
kuva = df.to_numpy().reshape(28,28)        # Ja tätä voit sitten muokata kuvan tulostamiseksi
plt.imshow(kuva)
plt.show()

maxPooledImage = skimage.measure.block_reduce(kuva, (4,4), np.max)
plt.imshow(maxPooledImage)
plt.show()

df = pd.read_csv('kt7\\w1.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w1 = df.to_numpy().reshape(30,784)              # w1 = 30x784 matriisi
print("w1 shape:")                       # activation a0 tätä voidaan käyttää neuroverkon inputtina
print(w1.shape)

df = pd.read_csv('kt7\\w2.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w2 = df.to_numpy().reshape(10,30)               # w2 = 10*30 matriisi
print("w2 shape:")                       # activation a0 tätä voidaan käyttää neuroverkon inputtina
print(w2.shape)

df = pd.read_csv('kt7\\b1.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b1 = df.to_numpy().reshape(30,1)                # b1 = 30 kpl
print("b1 shape:")                       # activation a0 tätä voidaan käyttää neuroverkon inputtina
print(b1.shape)

df = pd.read_csv('kt7\\b2.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b2 = df.to_numpy().reshape(10,1)                # b2 = 10 kpl
print("b2 shape:")                       # activation a0 tätä voidaan käyttää neuroverkon inputtina
print(b2.shape)

a1temp = np.matmul(w1, a0) + b1
print("a1 shape:")
print(a1temp.shape)
print("a1 printed:")
a1 = sigmoid(a1temp)
print(a1)

a2temp = np.matmul(w2, a1) + b2
print("a2temp shape:")
print(a2temp.shape)
print("a2 printed:")
a2 = sigmoid(a2temp)
plt.stem(a2)
plt.show()
print(a2)
