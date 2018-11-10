
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd


class TfCalculator:

    def __init__(self):
        pass

    def cal_tf_values(self, text_list):
        filtered_text = [self._pre_handle_text(text) for text in text_list]
        # filtered_text = text_list
        vectorizer = CountVectorizer(decode_error='ignore', ngram_range=(2, 3))
        cvec_counts = vectorizer.fit_transform(filtered_text)

        # print 'sparse matrix shape:', cvec_counts.shape
        # print 'nonzero count:', cvec_counts.nnz
        # print 'sparsity: %.2f%%' % (100.0 * cvec_counts.nnz / (cvec_counts.shape[0] * cvec_counts.shape[1]))

        # occ = np.asarray(cvec_counts.sum(axis=0)).ravel().tolist()
        # counts_df = pd.DataFrame({'term': vectorizer.get_feature_names(), 'occurrences': occ})
        # print counts_df.sort_values(by='occurrences', ascending=False).head(20)
        # word = vectorizer.get_feature_names()

        transformer = TfidfTransformer()
        transformed_weights = transformer.fit_transform(cvec_counts)
        weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
        weights_df = pd.DataFrame({'term': vectorizer.get_feature_names(), 'weight': weights})
        sort_df = weights_df.sort_values(by='weight', ascending=False).head(10)
        # print sort_df
        return sort_df['term']

    def _pre_handle_text(self, text):
        # lower_text = text.lower()
        # no_punctuation = text.translate(None, string.punctuation)
        # stemmer = SnowballStemmer("english")
        # stem_text = [stemmer.stem(wd) for wd in text.split(' ')]

        ru_stop = set(stopwords.words('id'))
        no_stopwords = [wd for wd in text.split(' ') if wd not in ru_stop]

        en_stop = set(stopwords.words('english'))
        no_stopwords = [wd for wd in no_stopwords if wd not in en_stop]

        handled_text = ' ' . join(no_stopwords)

        return handled_text



