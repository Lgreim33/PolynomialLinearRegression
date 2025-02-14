from regression import LineaerRegression
import kagglehub


# get dataset
path = kagglehub.dataset_download("abhishek14398/salary-dataset-simple-linear-regression")

regressor = LineaerRegression(2)

print(regressor.poly)