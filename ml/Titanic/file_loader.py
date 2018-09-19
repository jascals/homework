import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter


def __main__():
    loadData()


def loadData():
    dt_train = pd.read_csv('Titanic/train.csv')

    dt_train_p = dt_train.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    labels = dt_train_p.groupby(['Survived'])
    dataSet = dt_train_p.drop(['PassengerId', 'Survived'], axis=1)

    return labels, dataSet

    # PG_Survival_Rate = (Pclass_Gender_grouped.sum() / Pclass_Gender_grouped.count())['Survived']
    #
    # x = np.array([1, 2, 3])
    # width = 0.3
    # plt.bar(x - width, PG_Survival_Rate.female, width, color='r')
    # plt.bar(x, PG_Survival_Rate.male, width, color='b')
    # plt.title('Survival Rate by Gender and Pclass')
    # plt.xlabel('Pclass')
    # plt.ylabel('Survival Rate')
    # plt.xticks([1, 2, 3])
    # plt.yticks(np.arange(0.0, 1.1, 0.1))
    # plt.grid(True, linestyle='-', color='0.7')
    # plt.legend(['Female', 'Male'])
    # plt.show()
