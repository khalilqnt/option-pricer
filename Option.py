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

