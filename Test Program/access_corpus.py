import os
import collections

ner_tags = collections.Counter()

corpus_root = "gmb-2.2.0"   # Make sure you set the proper path to the unzipped corpus
count_tag_file = 0
sum_file_size = 0

for root, dirs, files in os.walk(corpus_root):
    for filename in files:
        if filename.endswith("en.tags"):
            count_tag_file = count_tag_file + 1
            sum_file_size = sum_file_size + os.path.getsize(os.path.join(root, filename))
            # with open(os.path.join(root, filename), 'rb') as file_handle:
            #     file_content = file_handle.read().decode('utf-8').strip()
            #     annotated_sentences = file_content.split('\n\n')   # Split sentences
            #     for annotated_sentence in annotated_sentences:
            #         annotated_tokens = [seq for seq in annotated_sentence.split('\n') if seq]  # Split words
            #
            #         standard_form_tokens = []
            #
            #         for idx, annotated_token in enumerate(annotated_tokens):
            #             annotations = annotated_token.split('\t')   # Split annotations
            #             word, tag, ner = annotations[0], annotations[1], annotations[3]
            #
            #             ner_tags[ner] += 1

# print ner_tags

print(count_tag_file)
print(sum_file_size)
"""
Counter({u'O': 1146068, u'geo-nam': 58388, u'org-nam': 48034, u'per-nam': 23790, u'gpe-nam': 20680, u'tim-dat': 12786, u'tim-dow': 11404, u'per-tit': 9800, u'per-fam': 8152, u'tim-yoc': 5290, u'tim-moy': 4262, u'per-giv': 2413, u'tim-clo': 891, u'art-nam': 866, u'eve-nam': 602, u'nat-nam': 300, u'tim-nam': 146, u'eve-ord': 107, u'per-ini': 60, u'org-leg': 60, u'per-ord': 38, u'tim-dom': 10, u'per-mid': 1, u'art-add': 1})
"""
