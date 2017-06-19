import os
import sys
import collections

if(len(sys.argv) < 2):
    sys.exit('Please specify whether you want to get the subcategory or not. Either type --all to include subcategory or --core to not include it.')

# Create collections.Counter structure data
# It is basically to count occurence of the words
ner_count = collections.Counter()
postag_count = collections.Counter()
word_count = collections.Counter()

# Debugging
# print(type(ner_tags))

# The path to the used corpus, here I used large dataset corpus named Groningen Meaning Bank
corpus_root = "gmb-2.2.0"

# Debugging
# Simply to count how many files are processed
count_tag_file = 0
# Simply to determine the total file size
sum_file_size = 0
# Exit point
exit = True

#Iterate through all the files
for root, dirs, files in os.walk(corpus_root):
    # if (exit):
    #     break;
    for filename in files:
        # if (exit):
        #     break;
        # Only process tag file
        if filename.endswith("en.tags"):
            count_tag_file = count_tag_file + 1
            sum_file_size = sum_file_size + os.path.getsize(os.path.join(root, filename))

            # Open the full path
            with open(os.path.join(root, filename), 'rb') as file_handle:
                # Decode file content
                file_content = file_handle.read().decode('utf-8').strip()

                # Split sentences, sentences are separated with two newline characters
                annotated_sentences = file_content.split('\n\n')

                # Iterate through sentences
                for annotated_sentence in annotated_sentences:

                    # Split words, words are separated with a newline character
                    annotated_tokens = [seq for seq in annotated_sentence.split('\n') if seq]

                    standard_form_tokens = []

                    for idx, annotated_token in enumerate(annotated_tokens):
                        # Split annotations, annotations are separated with a tab character
                        annotations = annotated_token.split('\t')

                        # The 1st annotation is the word itself, the 2nd is pos_tag, and the 3rd is it's named entity
                        word, pos_tag, ner = annotations[0], annotations[1], annotations[3]

                        if (sys.argv[1] == '--all'):
                            # Get all category including subcategory
                            ner_count[ner] += 1
                        elif (sys.argv[1] == '--core'):
                            # Get only the primary category
                            if ner != 'O':
                                ner = ner.split('-')[0]
                            ner_count[ner] += 1
                        else:
                            sys.exit('Wrong arguments supplied.')

                        postag_count[pos_tag] += 1
                        word_count[word] += 1

        # if (count_tag_file >= 5):
        #     exit = True;
        #     break;

# Debugging
# print()
# print('DELIMITER : WORD : BEGIN')
# print()
# print(word_count)

# print()
# print('DELIMITER : TAG : BEGIN')
# print()
# print(postag_count)

print()
print('DELIMITER : NER : BEGIN')
print()
print(ner_count)

print()
print('DELIMITER : END')
print()

# Debugging
# print(count_tag_file)
# print(sum_file_size)
print "Total words which have named entity : ", sum(ner_tags.values())
# 1354149

"""
For --core
Counter
({
    # Not a named entity (outside)
    u'O': 1146068,

    # Geographical Entity
    u'geo': 58388,

    # Organization
    u'org': 48094,
    u'per': 44254,
    u'tim': 34789,
    u'gpe': 20680,
    u'art': 867,
    u'eve': 709,
    u'nat': 300
})
"""

"""
For --all
Counter
({
        u'O': 1146068,
        u'geo-nam': 58388,
        u'org-nam': 48034,
        u'per-nam': 23790,
        u'gpe-nam': 20680,
        u'tim-dat': 12786,
        u'tim-dow': 11404,
        u'per-tit': 9800,
        u'per-fam': 8152,
        u'tim-yoc': 5290,
        u'tim-moy': 4262,
        u'per-giv': 2413,
        u'tim-clo': 891,
        u'art-nam': 866,
        u'eve-nam': 602,
        u'nat-nam': 300,
        u'tim-nam': 146,
        u'eve-ord': 107,
        u'per-ini': 60,
        u'org-leg': 60,
        u'per-ord': 38,
        u'tim-dom': 10,
        u'per-mid': 1,
        u'art-add': 1
})
"""
