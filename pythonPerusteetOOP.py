
'''
Tämän tiedoston tarkoituksena on perehtyä Pythonin luokkiin ja olioihin sekä perintään.
'''

class baseClass:              # ei tarvita sulkuja, jos ei peritä eikä välitetä parametreja konstruktorille.
    def __init__(self):
        self.nimi = "This is baseClass"

    def printName(self):
        print(self.nimi)



class derivedClass(baseClass):  # perintä 
    def __init__(self):
        self.nimi = "This is derivedClass"
        self.C = aggregate()

class aggregate():
    def __init__(self):
        self.nimi = "This is aggregateClass"

    def aggregatePrint(self):
       print(self.nimi)      


def createBothClasses():
    A = baseClass()
    A.printName()
    B = derivedClass()
    B.printName()
    B.C.aggregatePrint()
    


if __name__ == '__main__':
    createBothClasses()
