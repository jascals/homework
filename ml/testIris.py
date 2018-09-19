from numpy import hstack, vstack, array, median, nan, log1p
from numpy.random import choice
from sklearn.datasets import load_iris
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import MinMaxScaler
from FeatureUnionExt import FeatureUnionExt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# 特征矩阵加工
# 使用vstack增加一行含缺失值的样本(nan, nan, nan, nan)
# 使用hstack增加一列表示花的颜色（0-白、1-黄、2-红），花的颜色是随机的，意味着颜色并不影响花的分类
iris = load_iris()
iris.data = hstack((choice([0, 1, 2], size=iris.data.shape[0] + 1).reshape(-1, 1),
                    vstack((iris.data, array([nan, nan, nan, nan]).reshape(1, -1)))))
# 目标值向量加工
# 增加一个目标值，对应含缺失值的样本，值为众数
iris.target = hstack((iris.target, array([median(iris.target)])))

# 新建计算缺失值的对象
step1 = ('Imputer', Imputer())
# 新建将部分特征矩阵进行定性特征编码的对象
step2_1 = ('OneHotEncoder', OneHotEncoder(sparse=False))
# 新建将部分特征矩阵进行对数函数转换的对象
step2_2 = ('ToLog', FunctionTransformer(log1p))
# 新建将部分特征矩阵进行二值化类的对象
step2_3 = ('ToBinary', Binarizer())
# 新建部分并行处理对象，返回值为每个并行工作的输出的合并
step2 = ('FeatureUnionExt',
         FeatureUnionExt(transformer_list=[step2_1, step2_2, step2_3], idx_list=[[0], [1, 2, 3], [4]]))
# 新建无量纲化对象
step3 = ('MinMaxScaler', MinMaxScaler())
# 新建卡方校验选择特征的对象
step4 = ('SelectKBest', SelectKBest(chi2, k=3))
# 新建PCA降维的对象
step5 = ('PCA', PCA(n_components=2))
# 新建逻辑回归的对象，其为待训练的模型作为流水线的最后一步
step6 = ('LogisticRegression', LogisticRegression(penalty='l2'))
# 新建流水线处理对象
# 参数steps为需要流水线处理的对象列表，该列表为二元组列表，第一元为对象的名称，第二元为对象
pipeline = Pipeline(steps=[step1, step2, step3, step4, step5, step6])

# 新建网格搜索对象
# 第一参数为待训练的模型
# param_grid为待调参数组成的网格，字典格式，键为参数名称（格式“对象名称__子对象名称__参数名称”），值为可取的参数值列表
grid_search = GridSearchCV(pipeline, param_grid={'FeatureUnionExt__ToBinary__threshold': [1.0, 2.0, 3.0, 4.0],
                                                 'LogisticRegression__C': [0.1, 0.2, 0.4, 0.8]})  # 训练以及调参
grid_search.fit(iris.data, iris.target)

#持久化数据
#第一个参数为内存中的对象
#第二个参数为保存在文件系统中的名称
#第三个参数为压缩级别，0为不压缩，3为合适的压缩级别
dump(grid_search, 'grid_search.dmp', compress=3)
#从文件系统中加载数据到内存中
grid_search = load('grid_search.dmp')
