#
#    Module: String2TF
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.vectortypes.termslist2tf: submodule of `html2vect` module"""

import numpy as np
import scipy.sparse as ssp


def trms2tf_dict(terms_l, vocabulary=None):

    # In case None is returned then return None again. The outer code layer should handle this...
    # ...if caused due to error.
    if terms_l is None:
        return None

    # Use the Vocabulary argument if any
    TF_d = dict()
    if vocabulary:
        # If a Vocabulary was given as argument
        # Count Terms and Build the Terms-Frequency (TF) dictionary
        for trm in terms_l:
            if trm in vocabulary:
                if trm in TF_d:  # if the dictionary of terms has the 'terms' as a key
                    TF_d[trm] += 1
                else:
                    TF_d[trm] = 1
            # else:
                # Not in the Vocabulary DROP THEM

    else:
        # If a Vocabulary was None
        # Count Terms and Build the Terms-Frequency (TF) dictionary
        for trm in terms_l:
            if trm in TF_d:  # if the dictionary of terms has the 'terms' as a key
                TF_d[trm] += 1
            else:
                TF_d[trm] = 1

    return TF_d


def trms2tf_narray(terms_l, vocabulary=None, norm_func=None,
                   ndtype=np.dtype([('terms', 'S128'), ('freq', 'float')])):

    # In case None is returned then return None again. The outer code layer should handle this...
    # ...if caused due to error.
    if terms_l is None:
        return None

    if vocabulary:

        tf_d = trms2tf_dict(terms_l, vocabulary=vocabulary)
        terms = np.array(tf_d.keys())
        freqs = np.array(tf_d.values())

    else:
        # Count Terms and Terms-Frequencies
        terms, inds = np.unique(terms_l, return_inverse=True)
        freqs = np.bincount(inds)

    # Get Normalized Smoothed Sums
    if norm_func:
        norm_freqs = norm_func(freqs, len(terms_l))
    else:
        norm_freqs = freqs   # If norm_func is None or 0 then do not normalise

    # Build Terms-Frequency (TF) dictionary
    # We need a Recored arrays to be created thus using numpy.rec.array.fromarrays() to be...
    # ...invoked as follows
    # (alternatively fromarrays() can be used directly print terms
    TF_arr = np.rec.array([terms, norm_freqs], dtype=ndtype)

    return TF_arr


def trms2f_sparse(terms_l, tid_vocabulary, norm_func=None, ndtype=np.float):

    # Checking prerecusites: Vocabulary (Terms-Index) should not be None or empty.
    if not tid_vocabulary or not isinstance(tid_vocabulary, dict):
        raise ValueError("tid_vocabulary (2nd) argument should be a non-empty python dictionary.")

    # Create Term-Frequency Dictionary Keeping only the terms of interest given into...
    # ...Terms-Index Vocabulary
    tf_d = trms2tf_dict(terms_l, vocabulary=tid_vocabulary)

    # In case None is returned then return None again. The outer code layer should handle this...
    # ...if caused due to error.
    if tf_d is None:
        return None

    # Getting the indices for the terms of our interest. In particular tf_d contained the terms...
    # ...that both are occurring into the input Vocabulary and the input terms-list. Following...
    # ...the sequence stored into the current python dictionary tf_d.
    col_idx_l = [tid_vocabulary[trm] for trm in tf_d.keys()]
    col_idx_a = np.array(col_idx_l)

    # Since the return value will be a sparse vector first dimension of the matrix will...
    # ...be 0 for all terms.
    dim0 = np.zeros(len(col_idx_l))

    # Getting the frequencies for terms of interest in order to be aligned idxs-list.
    freq_l = tf_d.values()

    if not freq_l:
        freq_l = [0]
        col_idx_a = np.array([0])
        dim0 = np.array([0])

    # # # Defining Terms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms...
    # ...occurring at several Text's Positions

    # Finding the proper output vector size, which it should be as the size of the...
    # ...Vocabulary-Index or +1 in case the index of
    # the Vocabulary-Index start at 1 and not at 0.
    if min(tid_vocabulary.values()) == 0:
        outp_vect_size = len(tid_vocabulary)
    else:
        outp_vect_size = len(tid_vocabulary) + 1

    # Now defining the Terms-Sequence-Sparse-Matrix with the proper output-vector-size.
    f_mtrx = ssp.csr_matrix((freq_l, (dim0, col_idx_a)), shape=(1, outp_vect_size), dtype=ndtype)

    # # #

    # Get Normalized Smoothed Sums
    if norm_func:
        norm_f_mtrx = norm_func(f_mtrx, len(tid_vocabulary))
    else:
        norm_f_mtrx = f_mtrx  # If norm_func is None or 0 then do not normalize.

    return ssp.csr_matrix(norm_f_mtrx, shape=norm_f_mtrx.shape, dtype=ndtype)


def trms2f_narray(terms_l, tid_vocabulary, norm_func=None, d2=False, ndtype=np.float):

    # Getting the sparse matrix aligned along to the Terms-Index of the Corpus' Vocabulary
    sparse_mtrx = trms2f_sparse(terms_l, tid_vocabulary, norm_func, ndtype)

    # Converting the sparse matrix to dense array
    dense_arr = sparse_mtrx.toarray()

    # Getting the document's terms frequencies in 2d of 1d array depending on the argument.
    if d2:
        freq_arr = dense_arr
    else:
        freq_arr = dense_arr[0]

    return freq_arr
