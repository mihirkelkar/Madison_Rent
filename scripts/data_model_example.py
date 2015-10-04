"""
Here we have used a publicly available dataset for house prices in boston to 
display how regression works with scikit learn. I will modify this example to work for Madison later on. 
"""
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold

import numpy as np

def read_csv():
  with open('../data/house_rent.csv', 'r') as infile:
    data = infile.readlines()[1:]
  final_data = list()
  price_list = list()
  for ii in data:
    temp_data = ii.split(",")
    price_list.append(float(temp_data[0]))
    final_data.append(map(float, temp_data[1:]))
  return np.array(final_data), np.array(price_list)

x, y = read_csv()

#Get the number of rooms in each house. That is the sizth element in each 
#feature vector
x = np.array([np.append(v, [1]) for v in x])
kf = KFold(len(x), n_folds = 20)
lr = LinearRegression(fit_intercept = True)
err = 0

for train, test in kf:
  lr.fit(x[train], y[train])
  #print x[test]
  p = map(lr.predict, x[test])
  e = p - y[test]
  err += np.sum(e * e)
root_mean_sq_10 = np.sqrt(err / len(x))
print('RMSE on 10 fold cv : {}'.format(root_mean_sq_10))
#print lr.predict([3, 1, 43.074761,-89.3837613, 1])
