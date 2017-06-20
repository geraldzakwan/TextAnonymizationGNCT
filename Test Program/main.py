import itertools
import ne_chunker
import corpus
import feature

from nltk import pos_tag, word_tokenize
# from nltk.chunk import conlltags2tree, tree2conlltags

from nltk import tree2conlltags
from nltk.chunk import ChunkParserI
from sklearn.linear_model import Perceptron
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline

# The path to the used corpus, here I used large dataset corpus named Groningen Meaning Bank
corpus_root = 'gmb-2.2.0'
mode = '--core'

def train_perceptron():
    reader = corpus.read_corpus_ner(corpus_root, mode)

    all_classes = ['O', 'B-per', 'I-per', 'B-gpe', 'I-gpe',
                   'B-geo', 'I-geo', 'B-org', 'I-org', 'B-tim', 'I-tim',
                   'B-art', 'I-art', 'B-eve', 'I-eve', 'B-nat', 'I-nat']

    # pa_ner = ne_chunker.NamedEntityChunker.train(itertools.islice(reader, 2000), feature_detector=feature.ner_features,
    #                                                all_classes=all_classes, batch_size=1000, n_iter=5)

    pa_ner = ne_chunker.NamedEntityChunker.load(feature.ner_features)

    text = "Cristiano Ronaldo is a decent footballer both in Real Madrid, Spain and Manchester United, United Kingdom. He is truly a masterpiece."
    print(pa_ner.parse(pos_tag(word_tokenize(text))))

    # accuracy = pa_ner.score(itertools.islice(reader, 1000))
    #
    # print "Accuracy:", accuracy
    # 0.970327096314

train_perceptron()
