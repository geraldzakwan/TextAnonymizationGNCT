import nltk
# from nltk import ne_chunk, pos_tag, word_tokenize
# from nltk.tree import Tree

def get_continuous_chunks(text):
    # This is used to parse betweens sentences
    sentences = nltk.sent_tokenize(text)

    # Debugging
    # print(sentences)

    # This is used to parse between words in each sentence
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    # Debugging
    # print(tokenized_sentences)

    # This is used to do post tagging for each word
    tagged_sentences = [nltk.pos_tag(word) for word in tokenized_sentences]

    # Debugging
    # print(tagged_sentences)

    # This is used to do NER tagging for each word
    # Binary = True means it will only detect whether a word has named entity
    # Binary = False means it will also detect the class of a word which has named entity
    chunked_sentences = [nltk.ne_chunk(word, binary=False) for word in tagged_sentences]

    # Debugging
    # print(chunked_sentences)

    # This will be the output of NER processing
    processed_list = []
    # chunked_sentences is a tree with root node containing sentences
    # So, we should get what's inside the root node
    inside_chunked_sentences = chunked_sentences[0]
    iterator_1 = 0

    while(iterator_1 < len(inside_chunked_sentences)):
        # Debugging
        # print(inside_chunked_sentences[iterator_1])

        # Check if it contains named entity label
        if (type(inside_chunked_sentences[iterator_1]) == nltk.tree.Tree):
            # Later check for case there is 'of' between named entity (between Tree)
            # e.g. United States of America
            while(type(inside_chunked_sentences[iterator_1]) == nltk.tree.Tree):
                # If it is a named entity, add the right label/class to the tuple
                processed_list.append([inside_chunked_sentences[iterator_1][0][0], inside_chunked_sentences[iterator_1].label()])
                iterator_1 = iterator_1 + 1

        # If it is not a named entity, add None label to the tuple
        processed_list.append([inside_chunked_sentences[iterator_1][0], None])

        iterator_1 = iterator_1 + 1

    print(processed_list)

txt = "Barack Obama is a great person in United States of America and Great BritainHe is truly our president."
chunked = get_continuous_chunks(txt)
