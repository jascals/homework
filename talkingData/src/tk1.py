# coding=utf-8
import tflearn
from tflearn.data_utils import load_csv

train_data, labels= load_csv('train_sample.csv', target_column=-1,
                      columns_to_ignore=[1,6,7],has_header=True,
                      categorical_labels=True,n_classes=2)

test_data =

# Build neural network
net = tflearn.input_data(shape=[None, 4])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(train_data, labels, n_epoch=10, batch_size=16, show_metric=True)

