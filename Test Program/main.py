import sys
import perceptron

if __name__ == "__main__":
    if(sys.argv[1] == 'naive_bayes'):
        if(sys.argv[2] == 'load'):
            classifier = perceptron.load(sys.argv[3])
        else:
            classifier = perceptron.train_naive_bayes(int(sys.argv[2]))
            # perceptron.save_perceptron(classifier, 'NB_' + sys.argv[2] + '_train_data_' + str(perceptron.calculate_accuracy(classifier, 1000)) + '_accuracy')
        result = perceptron.classify(classifier, 'default')
        print(result)
        # acc = perceptron.calculate_accuracy(classifier, 1000)
        # print(acc)
    elif(sys.argv[1] == 'perceptron'):
        if(sys.argv[2] == 'load'):
            classifier = perceptron.load(sys.argv[3])
        else:
            classifier = perceptron.train_perceptron(int(sys.argv[2]))
            # perceptron.save_perceptron(classifier, 'P_' + sys.argv[2] + '_train_data_' + str(perceptron.calculate_accuracy(classifier, 1000)) + '_accuracy')
        result = perceptron.classify(classifier, 'default')
        print(result)
        # acc = perceptron.calculate_accuracy(classifier, 1000)
        # print(acc)
