with open('data.csv.arff') as myfile:
    index = 0
    with open('train.arff', 'w') as train:
        with open('test.arff', 'w') as test:
            for _ in range(42417):
                if _ < 32561:
                    train.write(myfile.readline())
                else:
                    test.write(myfile.readline())
