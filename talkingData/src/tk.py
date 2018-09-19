# coding=utf-8

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

train_data = pd.read_csv('train_sample.csv')
test_data = pd.read_csv('test.csv')

id_list = test_data['click_id']

# v1.0
train_data = train_data.drop('attributed_time', axis=1)
test_data = test_data.drop('click_id', axis=1)
train_data = train_data.drop('ip', axis=1)
test_data = test_data.drop('ip', axis=1)
train_data = train_data.drop('click_time', axis=1)
test_data = test_data.drop('click_time', axis=1)

# train_data['attributed_time'] = train_data['attributed_time'].fillna('0')
# train_data['attributed_time'] = train_data['attributed_time'].apply(lambda x: str(x)[0])

# search for the best parameters of random forest
def parameter_evaluate(data):
    clf_ev = RandomForestClassifier()
    x, y = data.drop(['is_attributed'], axis=1), data['is_attributed']
    parameters = {'n_estimators': [100, 300], 'max_features': [3, 4, 5, 'auto'],
                  'min_samples_leaf': [9, 10, 12], 'random_state': [7]}
    grid_search = GridSearchCV(estimator=clf_ev, param_grid=parameters, cv=10, scoring='accuracy')
    print("parameters:")
    # train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
    grid_search.fit(x, y)
    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    bsp = grid_search.best_estimator_.get_params()  # the dict of parameters with best score
    for param_name in sorted(bsp.keys()):
        print("\t%s: %r" % (param_name, bsp[param_name]))
    return bsp


paras = parameter_evaluate(train_data)
# rf = RandomForestClassifier(n_estimators=100,criterion="gini",min_samples_leaf=9,random_state=17)

rf = RandomForestClassifier(**paras)
rf.fit(train_data.drop(['is_attributed'], axis=1), train_data['is_attributed'])

results = rf.predict(test_data)
output = pd.DataFrame({'click_id': id_list, "is_attributed": results})
output.to_csv('prediction.csv', index=False)

