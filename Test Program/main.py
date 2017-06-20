import sys
import perceptron

if __name__ == "__main__":
    classifier = perceptron.train_perceptron(int(sys.argv[1]))
    perceptron.save_perceptron(classifier, sys.argv[1] + '_train_data')
    result = perceptron.classify(classifier, 'default')
