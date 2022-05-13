import numpy as np
import matplotlib.pyplot as plt

class signalAnalyser:
    def __init__(self,Fs,t):
        print('Constructor of signalAnalyser')
        self.Fs = Fs
        self.Ts = 1/Fs
        self.t = t
        self.xakseli = np.arange(0,t,self.Ts)       # Mitä tässä tapahtuu?
        self.pituus = int(self.xakseli.size)        # Mitä tässä tapahtuu?
        self.yakseli = np.zeros((1,self.pituus))    # Mitä tässä tapahtuu?
        

    def create(self,f):
        pii = np.pi
        t = self.xakseli
        self.yakseli = np.cos( 2 * pii * f * t)     # Mitä tässä tapahtuu?


    def plot(self,start,stop):
        plt.figure(1)
        plt.plot(self.xakseli[start:stop],self.yakseli[start:stop],'-*')
        plt.show()   

if __name__ == '__main__':
    obj = signalAnalyser(100,2)  # luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
    obj.create(2)                # käytetään objektin create funktiota, missä f = 2 Hz
    obj.plot(0,50)               # käytetään objektin plot funktiota, plotataan väli 0 - 50 näytettä.

