
import os
import sys
sys.path.append('../../')

import tables as tb

# THIS IS THE MOST IMPORTANT
import html2vec.tables.cngrams as h2v_cng
import html2vec.tables.wngrams as h2v_wng
import html2vec.narray.cngrams as h2v_arr_cng

char_n_gram_size = 3
# tables_wng = h2v_wng.Html2LSI(
tables_cng = h2v_cng.Html2LSI(
    char_n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)

narray_cng = h2v_arr_cng.Html2LSI(
    char_n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)


# The rest is always the same!!!!

corpus_filepath = "/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/"
state_saving_path = "/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/TEST/"
if not os.path.exists(state_saving_path):
    os.mkdir(state_saving_path)

pytables_corpus_tmp_file = '/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/TEST/TEST.h5'

subfolders_lst = ['eshop/html/']

ret = tables_cng.from_paths(
    corpus_filepath, subfolders_lst,
    dims=6,
    h5_fname=pytables_corpus_tmp_file,
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

ret2 = narray_cng.from_paths(
    corpus_filepath, subfolders_lst,
    dims=6,
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

print ret[0][:, :].T
print ret2[0][:, :].T
