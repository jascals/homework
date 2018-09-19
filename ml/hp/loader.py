import pandas as pd
import numpy as np
import csv

# read in the training and testing data into Pandas.DataFrame objects
input_df = pd.read_csv('train.csv', header=0)
submit_df = pd.read_csv('test.csv', header=0)
df = pd.concat([input_df, submit_df])
df = df.reset_index()
df = df.drop('index', axis=1)
df.reindex_axis(input_df.columns, axis=1)
df['Alley'][df['Alley'].isnull()] = 'noAlley'
df['BsmtCond'][df['BsmtCond'].isnull()] = 'noBasement'
df['BsmtExposure'][df['BsmtExposure'].isnull()] = 'noBasement'
df['BsmtFinSF1'][df['BsmtFinSF1'].isnull()] = df['BsmtFinSF1'].mean()
df['BsmtFinSF2'][df['BsmtFinSF2'].isnull()] = df['BsmtFinSF2'].mean()
df['BsmtFinType1'][df['BsmtFinType1'].isnull()] = 'noBasement'
df['BsmtFinType2'][df['BsmtFinType2'].isnull()] = 'noBasement'
df['BsmtFullBath'][df['BsmtFullBath'].isnull()] = df['BsmtFullBath'].mode()
df['BsmtFullBath'][df['BsmtFullBath'].isnull()] = df['BsmtFullBath'].mode()
df['BsmtFullBath'][df['BsmtFullBath'].isnull()] = df['BsmtFullBath'].mean()
df['BsmtHalfBath'][df['BsmtHalfBath'].isnull()] = df['BsmtHalfBath'].mode()
df['BsmtHalfBath'][df['BsmtHalfBath'].isnull()] = df['BsmtHalfBath'].mean()
df['BsmtQual'][df['BsmtQual'].isnull()] = 'NB'
df['BsmtUnfSF'][df['BsmtUnfSF'].isnull()] = df['BsmtUnfSF'].mean()
df['Electrical'][df['Electrical'].isnull()] = df['Electrical'].mode()
df['Electrical'][df['Electrical'].isnull()] = 'SBrkr'
df['Exterior1st'][df['Exterior1st'].isnull()] = 'VinylSd'
df['Exterior2nd'][df['Exterior2nd'].isnull()] = 'VinylSd'
df['Fence'][df['Fence'].isnull()] = 'noFence'
df['FireplaceQu'][df['FireplaceQu'].isnull()] = 'noFQ'
df['Functional'][df['Functional'].isnull()] = 'Typ'
df['GarageArea'][df['GarageArea'].isnull()] = df['GarageArea'].mean()
df['GarageCars'][df['GarageCars'].isnull()] = df['GarageCars'].mean()
df['GarageCond'][df['GarageCond'].isnull()] = 'noG'
df['GarageFinish'][df['GarageFinish'].isnull()] = 'noG'
df['GarageQual'][df['GarageQual'].isnull()] = 'noG'
df['GarageType'][df['GarageType'].isnull()] = 'noG'
df['GarageYrBlt'][df['GarageYrBlt'].isnull()] = df['GarageYrBlt'].mean()
df['KitchenQual'][df['KitchenQual'].isnull()] = 'TA'
df['LotFrontage'][df['LotFrontage'].isnull()] = df['LotFrontage'].mean()
df['MSZoning'][df['MSZoning'].isnull()] = 'RL'
df['MasVnrArea'][df['MasVnrArea'].isnull()] = df['MasVnrArea'].mean()
df['MasVnrType'][df['MasVnrType'].isnull()] = 'None'
df['MiscFeature'][df['MiscFeature'].isnull()] = 'NA'
df['PoolQC'][df['PoolQC'].isnull()] = 'noPool'
df['SaleType'][df['SaleType'].isnull()] = 'WD'
df['TotalBsmtSF'][df['TotalBsmtSF'].isnull()] = df['TotalBsmtSF'].mean()
df['Utilities'][df['Utilities'].isnull()] = 'AllPub'

df['MSZoning'] = pd.factorize(df['MSZoning'])[0]
df['Street'] = pd.factorize(df['Street'])[0]
df['Alley'] = pd.factorize(df['Alley'])[0]
df['LotShape'] = pd.factorize(df['LotShape'])[0]
df['LandContour'] = pd.factorize(df['LandContour'])[0]
df['Utilities'] = pd.factorize(df['Utilities'])[0]
df['LotConfig'] = pd.factorize(df['LotConfig'])[0]
df['LandSlope'] = pd.factorize(df['LandSlope'])[0]
df['Neighborhood'] = pd.factorize(df['Neighborhood'])[0]
df['Condition1'] = pd.factorize(df['Condition1'])[0]
df['Condition2'] = pd.factorize(df['Condition2'])[0]
df['BldgType'] = pd.factorize(df['BldgType'])[0]
df['HouseStyle'] = pd.factorize(df['HouseStyle'])[0]
df['RoofStyle'] = pd.factorize(df['RoofStyle'])[0]
df['RoofMatl'] = pd.factorize(df['RoofMatl'])[0]
df['Exterior1st'] = pd.factorize(df['Exterior1st'])[0]
df['Exterior2nd'] = pd.factorize(df['Exterior2nd'])[0]
df['MasVnrType'] = pd.factorize(df['MasVnrType'])[0]
df['ExterQual'] = pd.factorize(df['ExterQual'])[0]
df['ExterCond'] = pd.factorize(df['ExterCond'])[0]
df['Foundation'] = pd.factorize(df['Foundation'])[0]
df['BsmtQual'] = pd.factorize(df['BsmtQual'])[0]
df['BsmtCond'] = pd.factorize(df['BsmtCond'])[0]
df['BsmtExposure'] = pd.factorize(df['BsmtExposure'])[0]
df['BsmtFinType1'] = pd.factorize(df['BsmtFinType1'])[0]
df['BsmtFinType2'] = pd.factorize(df['BsmtFinType2'])[0]
df['Heating'] = pd.factorize(df['Heating'])[0]
df['HeatingQC'] = pd.factorize(df['HeatingQC'])[0]
df['CentralAir'] = pd.factorize(df['CentralAir'])[0]
df['Electrical'] = pd.factorize(df['Electrical'])[0]
df['KitchenQual'] = pd.factorize(df['KitchenQual'])[0]
df['Functional'] = pd.factorize(df['Functional'])[0]
df['FireplaceQu'] = pd.factorize(df['FireplaceQu'])[0]
df['GarageType'] = pd.factorize(df['GarageType'])[0]
df['GarageFinish'] = pd.factorize(df['GarageFinish'])[0]
df['GarageQual'] = pd.factorize(df['GarageQual'])[0]
df['GarageCond'] = pd.factorize(df['GarageCond'])[0]
df['PavedDrive'] = pd.factorize(df['PavedDrive'])[0]
df['PoolQC'] = pd.factorize(df['PoolQC'])[0]
df['Fence'] = pd.factorize(df['Fence'])[0]
df['MiscFeature'] = pd.factorize(df['MiscFeature'])[0]
df['SaleType'] = pd.factorize(df['SaleType'])[0]
df['SaleCondition'] = pd.factorize(df['SaleCondition'])[0]

sed = df[df['SalePrice'].notnull()].values
wfs = df[df['SalePrice'].isnull()].values
Y = sed[:, 70]
X = sed[:, 0:70]
X2 = sed[:, 71:80]

X0  = np.hstack((X,X2))

linear_reg = linear_model.LinearRegression()

# tree_reg
from sklearn import tree
tree_reg = tree.DecisionTreeRegressor()

# simple line reg
# from sklearn import linear_model
# linear_reg.fit(X0,Y)

# knn
# from sklearn import neighbors
# knn = neighbors.KNeighborsRegressor()

rf =ensemble.RandomForestRegressor(n_estimators=50)
rf.fit(X0,Y)
rf.predict(XX0)

YY = wfs[:,70]
XX1  =wfs[:,0:70]
XX2  =wfs[:,71:80]
XX0 = np.hstack((XX1,XX2))

r = linear_reg.predict(XX0)

ids = submit_df['Id']

predictions_file = open("hp/myfirstsubmission.csv", "w")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["Id", "SalePrice"])
open_file_object.writerows(zip(ids, r))
predictions_file.close()
