import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from Option import Option, Call, Put

class BlackScholesPricer(): 
    def price(self, option: Option, spot, rate, vol): 
        K,T = option.strike, option.maturity
        d1 = (np.log(spot/K) + (rate + np.square(vol)/2) * T)/(vol * np.sqrt(T))
        d2 = d1 - vol * np.sqrt(T)

        if isinstance(option, Call): 
            return spot * norm.cdf(d1) - K * np.exp(-rate * T) * norm.cdf(d2)
        elif isinstance(option, Put):
            return - spot * norm.cdf(-d1) + K * np.exp(-rate * T) * norm.cdf(-d2) 
        else: 
            raise TypeError("veuillez entrer Put ou Call:  pas une option abstraite")
        
        



