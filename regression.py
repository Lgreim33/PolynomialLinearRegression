import pandas as pd
import matplotlib as plt
import random

class LineaerRegression:
    
    def __init__(self,order: int):
        self.order = order
        self.poly = self.initializeList(order)

    # creates a list of length n, where n is the order, returns a list of random floats between -1 and 1
    def initializeList(self,order : int):
        return [random.uniform(-1,1) for _ in range(order+1)]
