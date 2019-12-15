"""Digit recognition algorithm using a state vector machine and the MNIST dataset"""
import gzip
import pickle
import time

from sklearn import svm


def load_data():
    """Loads MNIST dataset from local file"""
    mnist = gzip.open("Digit-Recognition/mnist.pkl.gz", "rb")
    training_data, validation_data, test_data = pickle.load(mnist, encoding="latin1")
    mnist.close()
    return (training_data, test_data)


def classify():
    """Uses a state vector machine to classify the digits in the MNIST dataset"""
    training_data, test_data = load_data()
    # train the model
    print("Training the model...")
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    # test the model
    correct = 0
    for i, prediction in enumerate(clf.predict(test_data[0])):
        answer = test_data[1][i]
        print(f"Prediction: {prediction}, Answer: {answer}")
        if int(prediction) == int(answer):
            correct += 1

    percentage = round(int(correct) / len(test_data[1]) * 100, 2)
    print(
        f"\n{str(correct)} of {str(len(test_data[1]))} values correct ({percentage}% accuracy)"
    )


classify()
