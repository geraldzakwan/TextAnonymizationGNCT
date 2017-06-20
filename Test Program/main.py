import perceptron

if __name__ == "__main__":
    classifier = perceptron.train_perceptron()
    result = perceptron.classify(classifier, 'default')
