import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Option(): 
    def __init__(self, strike, maturity): 
        self.strike = strike 
        self.maturity = maturity

    def payoff(self, S_T): 
        #raise NotImplementedError("methode pas encore implémentée")
        pass

class Call(Option):
    def __init__(self, strike, maturity): 
        super().__init__(strike, maturity)
    def payoff(self, S_T):
        return np.maximum(S_T - self.strike, 0)

class Put(Option):
    def __init__(self, strike, maturity): 
        super().__init__(strike, maturity)
    def payoff(self, S_T):
        return np.maximum(self.strike - S_T, 0)

if __name__ == "__main__":
    c = Call(strike=100, maturity=1)
    p = Put(strike=100, maturity=1)
    S_T = np.linspace(50, 150, 100)
    plt.plot(S_T, c.payoff(S_T), label="Call payoff")
    plt.plot(S_T, p.payoff(S_T), label="Put payoff")
    plt.legend()
    plt.show()
