import cv2               # Asenna OpenCV: pip install opencv-python, jos et ole sitä jo tehnyt
                         # Tutustu OpenCV dokumentaatioon:https://docs.opencv.org/4.5.3/
'''
Asenna OpenCV: pip install opencv-python, jos et ole sitä jo tehnyt
Tutustu OpenCV dokumentaatioon:https://docs.opencv.org/4.5.3/
Tutustu annettuu koodiin ja tee seuraavat tehtävät:
1. Ja tee ohjelma, jolla saat luettua kaikki tehtävässä annetut kuvat ja 
   tulostettua ne matplotlib:n plt.imshow() –funktiolla
2. OpenCV esittää kuvan BGR muodossa, kun taas pyplot.imshow() olettaa kuvan olevan RGB muodossa. 
   Muokkaa luettua kuvaa siten, että saat esitettyä kuvat oikean värisinä (vertaa alkuperäisiin väreihin).
3. Käydään yhdessä tunnilla läpi, miten kuvan suodatus toimii (siitä on myös esimerkki koodissa).
4. Suodata annettu kuva 3, jonka olet ensin lukenut harmaasävykuvaksi seuraavilla reunoja tunnistavilla
   suodattimilla (joudut siis tekemään suodattimet = "kernelit")
   
   -1 -1 -1       -1 2 -1      -1 -2 -1
    2  2  2       -1 2 -1       0  0  0
   -1 -1 -1       -1 2 -1       1  2  1


'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kt5\kuva3.png',cv2.IMREAD_COLOR)  # lukee värikuvan tiedostosta.
#img.shape                                      # tällä voi katsoa kuinka paljon pikseleitä
kernel1 = np.ones((5,5),np.float32) / 25        # tehdään suodatin, joka summaa pikselit
                                                # 5x5 pikselin alueelta ja jaetaan tulos 25:llä

kernel2_1 = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
print(kernel2_1)
kernel2_2 = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
print(kernel2_2)
kernel2_3 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
print(kernel2_3)

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # näin voidaan muuttaa värikuva grayscale kuvaksi
#grayscale.shape                                 # ja näin voidaan katsoa sen muoto

varitOikein = np.zeros((img.shape))              # näin voidaan alustaa oikean kokoinen ja muotoinen
                                                 # kuvamatriisi, johon sinun tulee sitten osata
                                                 # laittaa oikean väriset pikselit oikeaan "alimatriisin"

varitOikein[:,:,0] = img[:,:,2]
varitOikein[:,:,1] = img[:,:,1]
varitOikein[:,:,2] = img[:,:,0]

suodatettu1 = cv2.filter2D(grayscale,-1,kernel1) # Tällä komennolla tehdään kuvalle suodatus
suodatettu2_1 = cv2.filter2D(grayscale,-1,kernel2_1)
suodatettu2_2 = cv2.filter2D(suodatettu2_1, -1, kernel2_2)
suodatettu2_3 = cv2.filter2D(suodatettu2_2, -1, kernel2_3)

# Ja tänne sinun pitäisi sitten osata tehdä ne 3 erilaista suodatinta ja 
# tulostaa sitten se neljäs kuva


plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(varitOikein/255,cmap='viridis')
plt.title('Värit Oikein')


plt.subplot(2,2,2)
plt.imshow(grayscale/255,cmap='gray')
plt.title('Harmaasävyt')


plt.subplot(2,2,3)
plt.imshow(suodatettu1/255,cmap='gray')
plt.title('blurrattu')

plt.subplot(2,2,4)
plt.imshow(suodatettu2_3/255,cmap='gray')
plt.title('Derivoitu')

plt.show()
