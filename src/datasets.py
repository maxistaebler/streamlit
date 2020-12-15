from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

iris.to_csv('../input/iris.csv')