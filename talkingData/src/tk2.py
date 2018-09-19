# coding=utf-8
import pandas as pd

COLUMNS = ['click_id', 'ip', 'app', 'device', 'os', 'channel', 'click_time', 'attributed_time', 'is_attributed']

train_data = pd.read_csv('train_sample.csv',names=COLUMNS, skipinitialspace=True)
test_data = pd.read_csv('test_sample.csv',names=COLUMNS, skipinitialspace=True)

id_list = test_data['click_id']

train_data = train_data.drop('ip', axis=1)
train_data = train_data.drop('click_time', axis=1)
train_data = train_data.drop('attributed_time', axis=1)

test_data = test_data.drop('click_id', axis=1)
test_data = test_data.drop('ip', axis=1)
test_data = test_data.drop('click_time', axis=1)



