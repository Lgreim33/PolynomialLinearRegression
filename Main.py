from regression import LineaerRegression
import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# get dataset
path = kagglehub.dataset_download("abhishek14398/salary-dataset-simple-linear-regression")

regressor = LineaerRegression()

polynomial = regressor.poly_coefficients
polynomial.reverse()

data = pd.read_csv(path + "\\" +  os.listdir(path)[0] )
print(data)
x_values = np.linspace(0,40,regressor.order+1)
# show data
plt.plot(data["YearsExperience"],data["Salary"], marker='o' , linestyle=' ')
# show our line of best fit pre fit
plt.plot(x_values,polynomial)

plt.plot(1.2,regressor.forward(1.2),marker='o' , linestyle=' ')
plt.show()