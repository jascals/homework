# coding:utf-8
# auther:cherie

import numpy
import scipy
import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn.svm import SVC

print('author : cherie')
print('numpy.version = '+numpy.__version__)
print('scipy.version = '+scipy.__version__)
print('sklearn.version = '+sklearn.__version__)
print('-----------')

digits = datasets.load_digits()
print(digits)
clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])
SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.001, kernel='rbf', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False)