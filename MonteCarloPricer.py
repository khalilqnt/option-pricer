import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from Option import Option, Call, Put

class MonteCarloPricer(): 

    def __init__(self, N = 100000): 
        self.nsim = N

    def price(self, option: Option, spot, rate, vol): 
        Z= np.random.standard_normal(self.nsim)
        T=option.maturity
        S_T = spot * np.exp((rate - (vol**2)/2)*T + vol * np.sqrt(T) * Z)
        p = option.payoff(S_T)
        return np.mean(p) * np.exp(-rate * T)
    
    
    
