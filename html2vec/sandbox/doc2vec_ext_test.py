
import os
import sys
sys.path.append('../../')

import tables as tb

# THIS IS THE MOST IMPORTANT
import html2vec.tables.cngrams as h2v_cng
import html2vec.tables.wngrams as h2v_wng
import html2vec.narray.cngrams as h2v_cng_narr
import html2vec.narray.wngrams as h2v_wng_narr


# THIS IS THE MOST IMPORTANT ALSO
n_gram_size = 3
tables_cng = h2v_cng.Html2GsmVec(
    n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)
tables_wng = h2v_wng.Html2GsmVec(
    n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)

narray_cng = h2v_cng_narr.Html2GsmVec(
    n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)
narray_wng = h2v_wng_narr.Html2GsmVec(
    n_gram_size, html_attrib=["text"], str_case='lower', valid_html=False
)


# The rest is always the same!!!!
corpus_filepath = "/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/"
state_saving_path = "/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/TEST2/"
if not os.path.exists(state_saving_path):
    os.mkdir(state_saving_path)

pytables_corpus_tmp_file = '/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/TEST2/TEST.h5'
pytables_corpus_tmp_file2 = '/home/dimitrios/Synergy-Crawler/Santinis_7-web_genre/TEST2/TEST2.h5'

subfolders_lst = ['eshop/html/']

cret = tables_cng.from_paths(
    corpus_filepath, subfolders_lst,
    # NOTE THE PARAMETERS
    dims=3, min_trm_fq=0, win_size=8, algo='PV-DM',
    alpha=0.025, min_alpha=0.025, epochs=10, decay=0.002,
    # The rest is the same as in LSI
    h5_fname=pytables_corpus_tmp_file,
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

wret = tables_wng.from_paths(
    corpus_filepath, subfolders_lst,
    # NOTE THE PARAMETERS
    dims=3, min_trm_fq=0, win_size=8, algo='PV-DM',
    alpha=0.025, min_alpha=0.025, epochs=10, decay=0.002,
    # The rest is the same as in LSI
    h5_fname=pytables_corpus_tmp_file2,
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

cret_narr = narray_cng.from_paths(
    corpus_filepath, subfolders_lst,
    # NOTE THE PARAMETERS
    dims=3, min_trm_fq=0, win_size=8, algo='PV-DM',
    alpha=0.025, min_alpha=0.025, epochs=10, decay=0.002,
    # The rest is the same as in LSI
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

wret_narr = narray_wng.from_paths(
    corpus_filepath, subfolders_lst,
    # NOTE THE PARAMETERS
    dims=3, min_trm_fq=0, win_size=8, algo='PV-DM',
    alpha=0.025, min_alpha=0.025, epochs=10, decay=0.002,
    # The rest is the same as in LSI
    tid_vocabulary=None,
    norm_func=None, encoding='utf8', error_handling='replace'
)

print cret[0][:, :].T
print
print wret[0][:, :].T
print
print cret_narr[0][:, :].T
print
print wret_narr[0][:, :].T
print
print

# Second Retured argument is tha TF matrix in all cases (like LSI) same here.
print cret[1][:, :].T
print
print wret[1][:, :].T
print
print cret_narr[1][:, :].T
print
print wret_narr[1][:, :].T
print
