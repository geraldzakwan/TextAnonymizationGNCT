import main_ner_2
import nltk_ner_trainer
import access_corpus

# The path to the used corpus, here I used large dataset corpus named Groningen Meaning Bank
corpus_root = 'gmb-2.2.0'
mode = '--core'

reader = access_corpus.read_corpus(corpus_root, mode)
data = list(reader)

training_samples = data[:int(len(data) * 0.9)]
test_samples = data[int(len(data) * 0.9):]

print "#training samples = %s" % len(training_samples)    # training samples = 55809
print "#test samples = %s" % len(test_samples)                # test samples = 6201
