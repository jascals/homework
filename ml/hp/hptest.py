import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import skew
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

all_df = pd.concat((train_df.loc[:, 'MSSubClass':'SaleCondition'], test_df.loc[:, 'MSSubClass':'SaleCondition']),
                   axis=0, ignore_index=True)
all_df['MSSubClass'] = all_df['MSSubClass'].astype(str)

quantitative = [f for f in all_df.columns if all_df.dtypes[f] != 'object']
qualitative = [f for f in all_df.columns if all_df.dtypes[f] == 'object']
print("quantitative: {}, qualitative: {}".format(len(quantitative), len(qualitative)))

missing = all_df.isnull().sum()
missing.sort_values(inplace=True, ascending=False)
missing = missing[missing > 0]
types = all_df[missing.index].dtypes
percent = (all_df[missing.index].isnull().sum() / all_df[missing.index].isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([missing, percent, types], axis=1, keys=['Total', 'Percent', 'Types'])
missing_data.sort_values('Total', ascending=False, inplace=True)

print(train_df.describe()['SalePrice'])

corrmat = train_df.corr()
k = 10
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(train_df[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values,
                 xticklabels=cols.values)
plt.show()


#dealing with missing data
all_df = all_df.drop((missing_data[missing_data['Total'] > 1]).index,1)
# df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)
all_df.isnull().sum().max() #just checking that there's no missing data missing...
# 对于missing 1 的我们到时候已平均数填充

#histogram and normal probability plot
sns.distplot(train_df['SalePrice'], fit=norm);
fig = plt.figure()
res = stats.probplot(train_df['SalePrice'], plot=plt)

