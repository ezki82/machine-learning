import numpy as np
import matplotlib.pyplot as plt

Fs = 1000 # 1kHz
Ts = 1/Fs # Time sample step
kantoaaltoF = 50

startTime = 0
stopTime = 1

time = np.arange(startTime, stopTime, Ts)
# print(time)

# kantoaalto = cos (2*pi*f*t)
kantoaalto = np.cos(2 * np.pi * kantoaaltoF * time)

data = np.zeros((1000,))
data[0:500] = np.ones((500,))
data[500:1000] = np.ones((500,)) *(-1)
moduloitu = data * kantoaalto
demoduloitu = moduloitu / kantoaalto

plt.figure(1)
plt.subplot(1,3,1)
plt.plot(kantoaalto)
plt.title('Kantoaalto')
plt.subplot(1,3,2)
plt.plot(moduloitu)
plt.title('Moduloitu')
plt.subplot(1,3,3)
plt.plot(demoduloitu)
plt.title('Demoduloitu')
plt.show()