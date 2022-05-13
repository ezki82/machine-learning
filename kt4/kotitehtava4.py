import cv2               # Asenna OpenCV: pip install opencv-python
import numpy as np
from matplotlib import pyplot as plt

koe1 = np.arange(27,dtype=np.float64)  # tehdään array = 0.0, 1.0, 2.0,..., 26.0
koe2 = np.arange(27,dtype=np.float64)  # tehdään array = 0.0, 1.0, 2.0,..., 26.0
koe3 = np.arange(27,dtype=np.float64)  # tehdään array = 0.0, 1.0, 2.0,..., 26.0
koe4 = np.arange(27,dtype=np.float64)  # tehdään array = 0.0, 1.0, 2.0,..., 26.0
koe5 = np.arange((6*6*3),dtype=np.float64)  # tehdään array = 0.0, 1.0, 2.0,..., 26.0
kuva_red = np.reshape(koe1,(3,3,3))        # muokataan se kolmeksi 3x3 "pikselin" matriisiksi
kuva_green = np.reshape(koe2,(3,3,3))        # muokataan se kolmeksi 3x3 "pikselin" matriisiksi
kuva_blue = np.reshape(koe3,(3,3,3))        # muokataan se kolmeksi 3x3 "pikselin" matriisiksi
kuva_gray = np.reshape(koe4,(3,3,3))        # muokataan se kolmeksi 3x3 "pikselin" matriisiksi
kuva_comb = np.zeros((6,6,3))        # muokataan se kolmeksi 3x3 "pikselin" matriisiksi
ykkoset = np.ones((3,3))        
nollat = np.zeros((3,3))

kuva_red[:,:,0]=ykkoset
kuva_red[:,:,1]=nollat
kuva_red[:,:,2]=nollat

kuva_green[:,:,0]=nollat
kuva_green[:,:,1]=ykkoset
kuva_green[:,:,2]=nollat

kuva_blue[:,:,0]=nollat
kuva_blue[:,:,1]=nollat
kuva_blue[:,:,2]=ykkoset

kuva_gray[:,:,0]=ykkoset * 0.5
kuva_gray[:,:,1]=ykkoset * 0.5
kuva_gray[:,:,2]=ykkoset * 0.5

kuva_comb[0:3,0:3,0:3] = kuva_red
kuva_comb[0:3,3:6,0:3] = kuva_green
kuva_comb[3:6,0:3,0:3] = kuva_blue
kuva_comb[3:6,3:6,0:3] = kuva_gray

# print(kuva_red)
# print(ykkoset)
print(kuva_comb)
# plt.subplot(1,5,1)
# plt.imshow(kuva_red)
# plt.subplot(1,5,2)
# plt.imshow(kuva_green)
# plt.subplot(1,5,3)
# plt.imshow(kuva_blue)
# plt.subplot(1,5,4)
# plt.imshow(kuva_gray)
# plt.subplot(1,5,5)
# plt.show()
plt.imshow(kuva_comb)
plt.show()

'''
 Tehtävät:
 1. Muokkaa annettua koodia siten, että saat piirrettyä punaisen 3*3 pikselin kokoisen kuvan
    lisäksi myös vihreän, sinisen ja harmaan 3*3 pikselin kokoisen kuvan.

 2. Tee annetun koodin opetusten perusteella 6x6 pikselin kokoinen kuva, jossa on 3*3 pikselin
    kokoiset alueet punaisella, sinisellä, vihreällä ja harmaalla värillä.
'''

