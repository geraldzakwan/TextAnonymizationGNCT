import perceptron

if __name__ == "__main__":
    classifier = perceptron.train_perceptron(10000)
    perceptron.save_perceptron(classifier, '10000_train_data')
    result = perceptron.classify(classifier, 'default')
