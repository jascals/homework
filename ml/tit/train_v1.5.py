# coding=utf-8
# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

# load data
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = pd.concat([train_df, test_df])

# data info
train_df.head()
train_df.tail()
train_df.info()
train_df.describe()
train_df.describe(include=['O'])

# 离散数据
pclass_cor = \
    train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
sex_cor = \
    train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
sibsp_cor = \
    train_df[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False)
parch_cor = \
    train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)

# 连续数据
# grid = sns.FacetGrid(train_df, col='Survived')
# grid.map(plt.hist, 'Age', bins=20)
# grid.savefig('out.png')

# Numerical，Ordinal 特征和Survived的相关性
# grid = sns.FacetGrid(train_df, col='Survived', row='Pclass', size=2.2, aspect=1.6)
# grid.map(plt.hist, 'Age', alpha=.5, bins=20)
# grid.add_legend();
# grid.savefig('out1.png')

# 所有离散型特征和Survived的相关性
# grid = sns.FacetGrid(train_df, row='Embarked', size=2.2, aspect=1.6)
# grid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex', palette='deep')
# grid.add_legend()
# grid.savefig('out2.png')

# 离散型特征，连续型特征和Survived的相关性
# grid = sns.FacetGrid(train_df, row='Embarked', col='Survived', size=2.2, aspect=1.6)
# grid.map(sns.barplot, 'Sex', 'Fare', alpha=.5, ci=None)
# grid.add_legend()
# grid.savefig('out3.png')

# 删除冗余数据
combine = combine.drop(['Ticket', 'Cabin'], axis=1)
combine = combine.drop(['Name'])
combine['Family_size'] = combine['SibSp'] + combine['Parch']

combine['isAlone'] = combine
