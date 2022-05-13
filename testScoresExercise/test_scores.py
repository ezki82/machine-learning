import math
import numpy as np
from sklearn.linear_model import LinearRegression

def gradient_descent_sklearn(x,y):
    xtemp = x[:,np.newaxis]
    reg = LinearRegression().fit(xtemp,y)
    print("m:", reg.coef_)
    print("b:", reg.intercept_)


def gradient_descent(x, y):
    # print(x)
    # print(y)
    # säädettävät parametrit nollataan aluksi
    m_curr = b_curr = 0.0

    # säädetään parametreja maksimissaan iterations kertaa
    iterations = 1000000

    # hyväksyttävä kustannusfunktion arvo, jolla lopetaan parempien parametrien etsintä
    costApproved = 1e-20

    # n on yhtä kuin arvojen määrä x-akselilla
    n = len(x)

    cost = 0.
    prevCost = 0.
    i = 0
    stayLoop = True

    # learning rate parametri, kannattaa aloittaa tosi pienellä arvolla
    learningRate = 0.0002

    while  stayLoop and i < iterations:
    #for i in range(iterations):
        i += 1 

        # laske outpu- arvo säädettävillä kertoimilla
        y_predicted = m_curr * x + b_curr

        # siirrä edellisen kustannusfunktion arvo muistiin
        prevCost = cost

        # laske kustannusfunktion arvo
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

        # kustannusfunktioiden erotus
        costDiff = prevCost - cost

        # laske kustannusfunktiolla virhe m parametrin suhteen
        md = -(2/n)*sum(x*(y-y_predicted))

        # laske kustannusfunktiolla virhe b parametrin suhteen
        bd = -(2/n)*sum((y-y_predicted))

        # korjaa vähennä säätöparametrista virhe*learningRate
        m_curr = m_curr - learningRate * md
        b_curr = b_curr - learningRate * bd

        if math.isclose(prevCost, cost, rel_tol=costApproved) or i >= iterations - 1:
            print("cost {}, prevCost {}, difference {}".format(cost, prevCost, costDiff))
            stayLoop = False

        if not stayLoop:
            print("m {}, b {}, iteration {}, cost {}, costDiff {}".format(m_curr, b_curr, i, cost, costDiff))
            
        # print("m {}, b {}, iteration {}, cost {}, costDiff {}".format(m_curr, b_curr, i, cost, costDiff))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

dataX = np.genfromtxt('testScoresExercise\\test_scores.csv', delimiter=',', skip_header=1, usecols=(1))
dataY = np.genfromtxt('testScoresExercise\\test_scores.csv', delimiter=',', skip_header=1, usecols=(2))

# gradient_descent(x, y)
gradient_descent(dataX, dataY)
gradient_descent_sklearn(dataX, dataY)