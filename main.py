import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from Option import Option, Call, Put
from BlackScholesPricer import BlackScholesPricer
from MonteCarloPricer import MonteCarloPricer


if __name__ == "__main__":
  
    c = Call(strike=100, maturity=1)
    p = Put(strike=100, maturity=1)
    S_T = np.linspace(50, 150, 100)
    plt.plot(S_T, c.payoff(S_T), label="Call payoff")
    plt.plot(S_T, p.payoff(S_T), label="Put payoff")
    plt.legend()
    pricer = BlackScholesPricer()
    plt.show()
    print("prix du call c", pricer.price(c, spot= 100, rate = 0.05, vol = 0.2))
    print("prix du put p", pricer.price(p, spot= 100, rate = 0.05, vol = 0.2))

    M=MonteCarloPricer()
    print("prix du call par Montecarlo ",M.price(c, spot=100, rate=0.05, vol=0.2) )
    print("prix du put par Montecarlo ",M.price(p, spot=100, rate=0.05, vol=0.2) )
    
