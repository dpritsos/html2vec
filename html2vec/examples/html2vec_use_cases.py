# -*- coding: utf-8 -*-

import sys

sys.path.append('../')

# Santini's 7-genres Corpus
corpus_filepath = "/media/dimitrios/TurnstoneDisk/7Genres/"

genres = ["blog", "eshop", "faq", "frontpage", "listing", "php", "spage"]
# genres = [
#     "article", "discussion", "download", "help", "linklist", "portrait", "portrait_priv", "shop"
# ]



###################################### STRING ##########################################

import html2vec.string.attrib_text as html2txt

# Character N-grams.
char_n_gram_size = 4

html2text = html2txt.HtmlFullText(valid_html=False)
# html2text = html2txt.HtmlTagText(valid_html=False)  NOTE: HTML Tags
# html2text = html2txt.HtmlScriptText(valid_html=False) NOTE: JavaScript
# html2text = html2txt.HtmlStyleText(valid_html=False)  NOTE: CSS

html_texts_lst = html2text.from_files(
    xhtml_file_l=list(self.html_file_l), encoding='utf-8', error_handling='replace'
)

print html_texts_lst


"""

###################################### ARRAY ##########################################

# Returning an array of N-Grams (Word, Character, etc), and the respective Vocabulary from the...
# ...input corpus, or it is using the External Vocabulary to drive the n-grams-array creation...
# ...process.

import html2vec.narray.cngrams as h2v_cng
import html2vec.narray.wngrams as h2v_wng
# import html2vec.narray.posngrams as h2v_pos  NOTE: It requires the POS tagger Lib from MIT.


# Word N-grams.-
word_n_gram_size = 1

narray_wng = h2v_wng.Html2TF(
    word_n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)

corpus_wng, vocab_wng = narray_wng.from_files(
    xhtml_file_l=list(self.html_file_l),
    tid_vocabulary=None, norm_func=None,
    encoding='utf-8', error_handling='replace'
)

print narray_wng


# Character N-grams.
char_n_gram_size = 4

narray_cng = h2v_cng.Html2TF(
    char_n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)

corpus_cng, vocab_cng = narray_cng.from_files(
    xhtml_file_l=list(self.html_file_l),
    tid_vocabulary=None, norm_func=None,
    encoding='utf-8', error_handling='replace'
)


print narray_cng



"""

