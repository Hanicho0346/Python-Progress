import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# iris=load_iris()
# data=pd.DataFrame(data=iris.data, columns=iris.feature_names)
# data['target']=iris.target
# data['target_names']=data['target'].map(lambda x: iris.target_names[x])
# data.to_csv('iris.csv', index=False)
# print(f"head :\n{data.head()}")
# print(f"describe :\n{data.describe()}")
# print(f"info :\n{data.info()}")
# print(f"columns :\n{data.columns}")
# print(f"dtypes :\n{data.dtypes}")
# print(f"isnull sum :\n{data.isnull().sum()}")

sns.set(style="whitegrid")
data=pd.read_csv('iris.csv')
data.hist(figsize=(10, 6), bins=20)
plt.suptitle('Histograms of Iris Dataset Features', fontsize=16)
plt.show()
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='target_names', data=data)
plt.title('Sepal Length vs Sepal Width')
plt.show()
sns.pairplot(data, hue='target_names')
plt.suptitle('Pair Plot of Iris Dataset Features', y=1.02)
plt.show()