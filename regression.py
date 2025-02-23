import matplotlib.pyplot as plt
import random

class LineaerRegression:
    
    def __init__(self,order = 1,min = -100000, max = 100000):
        self.order = order
        self.poly_coefficients = self.initializeList(order,min,max)

    # creates a list of length n, where n is the order, returns a list of random floats between -1 and 1
    def initializeList(self,order : int,min: int,max: int):
        return [random.uniform(min,max) for _ in range(order+1)]

    def forward(self,x):
        
        # stochastic gradient descent
        if type(x) != list():
            y_pred = 0.0
            for i in range(self.order):
                y_pred += self.poly_coefficients[i]*(x**i)

            return y_pred
            

            
        
    # One round of gradient decent 
    def backProp(self,learning_rate,loss):
        updated_weights = self.poly_coefficients

        # Very simple implementation, we are going to apply the power rule to each element in the array, the order of polynomial increasing from right to left
        # The index should correlate to the exact power we would expect for a  
        for i in range(self.order):
            updated_weights[i] += learning_rate * loss 


    
        


