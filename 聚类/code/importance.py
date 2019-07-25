import pandas as pd
import numpy as np
# names = ['NUM','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','CLASS']
# names = ['NUM', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'CLASS']
data = pd.read_csv(r'data_using_method_in_paper/outputVtVsVts4_detail.csv', encoding='gbk')
X = data.iloc[:,1:51]  #independent columns
y = data.iloc[:,51]    #target column i.e price range
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(50).plot(kind='barh')
plt.show()