import numpy as np

def gradient_descent(x, y):
    # säädettävät parametrit nollataan aluksi
    m_curr = b_curr = 0.0

    # säädetään parametreja maksimissaan iterations kertaa
    iterations = 100000

    # hyväksyttävä kustannusfunktion arvo
    costApproved = 0.00001

    # n on yhtä kuin arvojen määrä x-akselilla
    n = len(x)

    cost = 1
    i = 0

    # learning rate parametri, kannattaa aloittaa tosi pienellä arvolla
    learningRate = 0.01

    while cost > costApproved and i < iterations:
    #for i in range(iterations):
        i += 1 
        # laske outpu- arvo säädettävillä kertoimilla
        y_predicted = m_curr * x + b_curr

        # laske kustannusfunktion arvo
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

        # laske kustannusfunktiolla virhe m parametrin suhteen
        md = -(2/n)*sum(x*(y-y_predicted))

        # laske kustannusfunktiolla virhe b parametrin suhteen
        bd = -(2/n)*sum((y-y_predicted))

        # korjaa vähennä säätöparametrista virhe*learningRate
        m_curr = m_curr - learningRate * md
        b_curr = b_curr - learningRate * bd
        print("m {}, b {}, iteration {}, cost {}".format(m_curr, b_curr, i, cost))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)