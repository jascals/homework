# coding=utf-8
import csv

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Perceptron, SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier

input_df = pd.read_csv("train.csv", header=0)
submit_df = pd.read_csv("test.csv", header=0)

# load data
df = pd.concat([input_df, submit_df])
df = df.reset_index()
df = df.drop('index', axis=1)
df = df.reindex_axis(input_df.columns, axis=1)

# missing data
df = df.drop('Cabin', axis=1)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode())

# feature engineer
df['Sex'] = pd.factorize(df['Sex'])[0]
df = df.drop('Name', axis=1)
df = df.drop('Ticket', axis=1)
df['Embarked'] = pd.factorize(df['Embarked'])[0]
df['Family_size'] = df['SibSp'] + df['Parch']
df = df.drop(['PassengerId', 'SibSp', 'Parch'], axis=1)

# train
known_survived = df[df['Survived'].notnull()].values
unknown_survived = df[df['Survived'].isnull()].values
Y = known_survived[:, 0]
X = known_survived[:, 1:]

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X, Y)
logreg_pred = logreg.predict(unknown_survived[:, 1:]).astype(int)
acc_log = round(logreg.score(X, Y) * 100, 2)

# Support Vector Machines
svc = SVC()
svc.fit(X, Y)
svc_pred = svc.predict(unknown_survived[:, 1:]).astype(int)
acc_svc = round(svc.score(X, Y) * 100, 2)

#  k-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)
knn_pred = knn.predict(unknown_survived[:, 1:]).astype(int)
acc_knn = round(knn.score(X, Y) * 100, 2)

# Gaussian Naive Bayes
gaussian = GaussianNB()
gaussian.fit(X, Y)
gaussian_pred = gaussian.predict(unknown_survived[:, 1:]).astype(int)
acc_gaussian = round(gaussian.score(X, Y) * 100, 2)

# Perceptron
perceptron = Perceptron()
perceptron.fit(X, Y)
perceptron_pred = perceptron.predict(unknown_survived[:, 1:]).astype(int)
acc_perceptron = round(perceptron.score(X, Y) * 100, 2)

# Linear SVC
linear_svc = LinearSVC()
linear_svc.fit(X, Y)
linear_svc_pred = linear_svc.predict(unknown_survived[:, 1:]).astype(int)
acc_linear_svc = round(linear_svc.score(X, Y) * 100, 2)

# Stochastic Gradient Descent
sgd = SGDClassifier()
sgd.fit(X, Y)
sgd_pred = sgd.predict(unknown_survived[:, 1:]).astype(int)
acc_sgd = round(sgd.score(X, Y) * 100, 2)

# Decision Tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X, Y)
decision_tree_pred = decision_tree.predict(unknown_survived[:, 1:]).astype(int)
acc_decision_tree = round(decision_tree.score(X, Y) * 100, 2)

# Random Forest
random_forest = RandomForestClassifier(n_estimators=1000)
random_forest.fit(X, Y)
random_forest_pred = random_forest.predict(unknown_survived[:, 1:]).astype(int)
acc_random_forest = round(random_forest.score(X, Y) * 100, 2)

# cor
models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression',
              'Random Forest', 'Naive Bayes', 'Perceptron',
              'Stochastic Gradient Decent', 'Linear SVC',
              'Decision Tree'],
    'Score': [acc_svc, acc_knn, acc_log,
              acc_random_forest, acc_gaussian, acc_perceptron,
              acc_sgd, acc_linear_svc, acc_decision_tree]})
models.sort_values(by='Score', ascending=False)
print(models)

# save data
ids = submit_df['PassengerId']
with open('submission.csv','w') as out:
    write = csv.writer(out)
    write.writerow(['PassengerId', 'Survived'])
    write.writerows(zip(ids, random_forest_pred))
