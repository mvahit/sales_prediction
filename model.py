
import pickle #python nesnelerini kaydetmek ve cagirmak icin kullanilir.
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv("data/Advertising.csv", index_col = 0)

from sklearn.linear_model import LinearRegression

X = df.drop('sales', axis=1)
y = df[["sales"]]

reg_model = LinearRegression()
reg_model.fit(X, y)
y_pred = reg_model.predict(X)
rmse = np.sqrt(mean_squared_error(y, y_pred))
print("RMSE:",rmse)

pickle.dump(reg_model, open('regression_model.pkl','wb'))

print("Model Kaydedildi")

#model = pickle.load(open('regression_model.pkl','rb'))
#print(model.predict

#paket versionlarini cikarmak heroku icin.
#conda env export > requrements.txt