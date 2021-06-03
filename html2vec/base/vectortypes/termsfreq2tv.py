from .termslist2tf import *
from operator import itemgetter


def tf2tv_dict(tf_dict, rtchar_size, var_vocab=None):

    tvftl_dict = {}

    if var_vocab:

        # Create a Term-Variance dict for every term in the term-frequency dict.
        for trm, frq in tf_dict.items():

            if trm[0:rtchar_size] in var_vocab:

                if trm[0:rtchar_size] in tvftl_dict:

                    tvftl_dict[trm[0:rtchar_size]][0] = tvftl_dict[trm[0:rtchar_size]][1] + frq

                    if trm not in tvftl_dict[trm[0:rtchar_size]][2]:

                        tvftl_dict[trm[0:rtchar_size]][1] = tvftl_dict[trm[0:rtchar_size]][1] + 1

                        tvftl_dict[trm[0:rtchar_size]][2].append(trm)

                elif len(trm[0:rtchar_size]) == rtchar_size:

                    tvftl_dict[trm[0:rtchar_size]] = [1, frq,  [trm]]

            # else: DROPING the RootTerm
    else:

        # For every term in the term-frequency dict.
        for trm, frq in tf_dict.items():

            # Adding the new frequecy of the RootTerm, if already excists...
            # ... In case the term is new add +1 to its RootTerm and apped it to the terms-list...
            # ... having the same RootTerm.
            if trm[0:rtchar_size] in tvftl_dict:

                tvftl_dict[trm[0:rtchar_size]][0] = tvftl_dict[trm[0:rtchar_size]][1] + frq

                if trm not in tvftl_dict[trm[0:rtchar_size]][2]:

                    tvftl_dict[trm[0:rtchar_size]][1] = tvftl_dict[trm[0:rtchar_size]][1] + 1

                    tvftl_dict[trm[0:rtchar_size]][2].append(trm)

            elif len(trm[0:rtchar_size]) == rtchar_size:

                tvftl_dict[trm[0:rtchar_size]] = [1, frq,  [trm]]

    return tvftl_dict


def tf2rtv_dict(tf_dict, rtchar_size, var_vocab=None):

    # NOTE: This is a quick-and-dirty solution. It can be greatly optimized.

    tvftl_dict = tf2tv_dict(tf_dict, rtchar_size, var_vocab)

    # Getting max frequency as normalization factor.
    max_tf = np.max([vals[1] for vals in tvftl_dict.values()])

    rtv_dict = dict()
    for rtrm, vals in tvftl_dict.items():
        rtv_dict[rtrm] = vals[0] * (vals[1] / float(max_tf))

    return rtv_dict


def terms2v_sparse(terms_l, rtchar_size, rtid_vocabulary, norm_func=None, ndtype=np.float):

    # Checking prerecusites: Vocabulary (RootTerms-Index) should not be None or empty.
    if not rtid_vocabulary or not isinstance(rtid_vocabulary, dict):
        raise ValueError("rtid_vocabulary (2nd) argument should be a non-empty python dictionary.")

    # Creating RootTerm-Variance Dictionary Keeping only the RootTerms of interest given into...
    # ...RootTerms-Index Vocabulary
    rtv_d = tf2rtv_dict(trms2tf_dict(terms_l), rtchar_size, var_vocab=rtid_vocabulary)

    # In case None is returned then return None again. The outer code layer should handle this...
    # ...if caused due to error.
    if rtv_d is None:
        return None

    # Getting the indices for the RootTerms of our interest. In particular rtf_d contained the...
    # ...rootterms. that both are occurring into the input Vocabulary and the input...
    # ...RootTerms-list. Following the sequence stored into the current python dictionary rtf_d.
    col_idx_l = [rtid_vocabulary[rtrm] for rtrm in rtv_d.keys()]
    col_idx_a = np.array(col_idx_l)

    # Since the return value will be a sparse vector first dimension of the matrix will...
    # ...be 0 for all terms.
    dim0 = np.zeros(len(col_idx_l))

    # Getting the variances for terms of interest in order to be aligned idxs-list.
    vars_l = rtv_d.values()

    if not vars_l:
        vars_l = [0]
        col_idx_a = np.array([0])
        dim0 = np.array([0])

    # # # Defining RootTerms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs...
    # ...RootTerms occurring at several Text's Positions.

    # Finding the proper output vector size, which it should be as the size of the...
    # ...RootVocabulary-Index or +1 in case the index of the Vocabulary-Index start...
    # ...at 1 and not at 0.
    if min(rtid_vocabulary.values()) == 0:
        outp_vect_size = len(rtid_vocabulary)
    else:
        outp_vect_size = len(rtid_vocabulary) + 1

    # Now defining the Terms-Sequence-Sparse-Matrix with the proper output-vector-size.
    vars_mtrx = ssp.csr_matrix((vars_l, (dim0, col_idx_a)), shape=(1, outp_vect_size), dtype=ndtype)

    # # #

    # Get Normalized Smoothed Sums
    if norm_func:
        norm_vars_mtrx = norm_func(vars_mtrx, len(rtid_vocabulary))
    else:
        norm_vars_mtrx = vars_mtrx  # If norm_func is None or 0 then do not normalize.

    return ssp.csr_matrix(norm_vars_mtrx, shape=norm_vars_mtrx.shape, dtype=ndtype)


def terms2v_narray(
        terms_l, rtchar_size, rtid_vocabulary, norm_func=None, d2=False, ndtype=np.float):

    # Getting the sparse matrix aligned along to the Terms-Index of the Corpus' Vocabulary
    sparse_mtrx = terms2v_sparse(terms_l, rtchar_size, rtid_vocabulary, norm_func, ndtype)

    # Converting the sparse matrix to dense array
    dense_arr = sparse_mtrx.toarray()

    # Getting the document's terms frequencies in 2d of 1d array depending on the argument.
    if d2:
        vars_arr = dense_arr
    else:
        vars_arr = dense_arr[0]

    return vars_arr


def MISC():

    med_list = []
    final_dict = {}

    # tvftl_dict2 = tvftl_dict
    # tvftl_dict2 = copy.deepcopy(tvftl_dict)

    for key2, val2 in tvftl_dict.items():
        val2.append(key2)
        med_list.append(val2)
        # print val2

    sort_med_list = sorted(
        sorted(med_list, key=itemgetter(sec_short_crit), reverse=True),
        key=itemgetter(prim_short_crit), reverse=True
    )

    sort_med_list

    for idx, val3 in enumerate(sort_med_list):
        # print val3

        for word in val3[2]:
            final_dict[word] = [val3[3], idx, val3[1]]
        '''
        tvftl_dict[val3[3]].append(idx)
        print val3
        '''
    # print '--------------------'
    # med_list.sort(key=lambda x: x[fq_var_sort])

    '''
    for key3, val4 in tvftl_dict.items():
        # print val4
        for val5 in val4[2]:
            final_dict[val5] =[key3, val4[3]]
    '''

    return final_dict
