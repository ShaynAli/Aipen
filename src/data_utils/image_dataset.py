

import pandas as pd

def imageData():
    # print('Mean temp: ' + str(meanTemp))
    df3 = pd.read_csv("../../data/fashion-mnist_test.csv")
    df4 = pd.read_csv("../../data/fashion-mnist_train.csv")
    print("----------Fashion-mnist Test----------")
    print(df3)
    print("----------FSHION-MNIST Train----------")
    print(df4)


def main():
    imageData()


if __name__ == '__main__':
    main()