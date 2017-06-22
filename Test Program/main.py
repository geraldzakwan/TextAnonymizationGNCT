import sys
import perceptron

if __name__ == "__main__":
    classifier = perceptron.train_naive_bayes(int(sys.argv[1]))
    perceptron.save_perceptron(classifier, sys.argv[1] + '_train_data' + '_NB')
    result = perceptron.classify(classifier, 'default')
    perceptron.calculate_accuracy(classifier, 1000)
