#
#    Module: TFDUtils - Term-Frequency Dictionary (Native Python) Utilities
#
#    Author: Dimitrios Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.convert.tfdutils: submodule of `html2vect` """


def merge_tfds(*terms_d):
    """ mege_tfds(): is getting a set of term-frequency dictionaries as list of
        arguments and return a dictionary of common terms with their sum of frequencies
        of occurred in all dictionaries containing these terms. """

    tf_d = dict()
    tf_l = list()

    for tr_dict in terms_d:
        tf_l.extend(tr_dict.items())

    for i in range(len(tf_l)):
        if tf_l[i][0] in tf_d:
            tf_d[tf_l[i][0]] += tf_l[i][1]
        else:
            tf_d[tf_l[i][0]] = tf_l[i][1]

    return tf_d


def merge_tfds_frmlist(tf_d_l):
    """ gen_tfds_frmlist(): is getting a list of Term-Frequency Dictionaries and creates a
        TF Dictionary of all terms occurred in the list. """

    return merge_tfds(*tf_d_l)


def tf2tidx(term_d):
    """ tf2tidx(): is getting a Term-Frequency dictionary and returns one
        with terms-index number. The index number is just their position in the
        descending order sorted list of dictionary keys. """

    # Get the TF list
    tf_l = term_d.items()
    # Short by Frequency Max frequency goes first (Descending Order)
    tf_l = sorted(tf_l, key=lambda tf_l: tf_l[1], reverse=True)

    # Create the Terms-Index Dictionary
    terms_l = [tf[0] for tf in tf_l]
    idx = range(len(terms_l))
    term_idx_d = dict(zip(terms_l, idx))

    return term_idx_d


def _tf2idxf(tf_d, tidx_d):
    """ _tf2idxf(): Don't use it directly, use tf2idxf instead.
        This function is getting a TF dictionary representing the TF Vector,
        and a TF-Index. It returns a Index-Frequency dictionary where each term of the TF
        dictionary has been replaced with the Index number of the TF-Index. In case the term of the
        TF Dictionary is not in the TF-Index then the term is just Dropped. Therefore,
        the Index-Frequency dictionary it will no more include the missing (from TF-Index) term. """

    idxed_d = dict()

    for term, freq in tf_d.items():
        if term in tidx_d:
            idxed_d[tidx_d[term]] = freq
        #  else: DROP THE TERM

    return idxed_d


def tf2idxf(tf_d_l, tf_idx_d):
    """ tf2idxf(): is getting a TF-Dictionary or a list of TF-Dictionaries and TF-Index. It applies
        the VHutils._tf2idxf() function to the dictionaries and returns a list or single
        TF-Dictionary depending on the input. """

    if isinstance(tf_d_l, list):
        idxed_d = list()

        for tf_d in tf_d_l:
            idxed_d.append(__tf2idxf(tf_d, tf_idx_d))

        return idxed_d

    elif isinstance(tf_d_l, dict):
        return _tf2idxf(tf_d_l, tf_idx_d)
    else:
        raise Exception("Dictionary or a List of Dictionaries was expected as fist input argument")


def keep_most(terms_d, terms_amout):
    """ keep_most(): is getting a SHORTED dictionary of Terms-Frequencies and
        the amount of Terms to return as arguments. It is returning the number
        of Terms equal to the argument 'terms_amount' with the Highest Frequency. """
    terms_l = [(v, k) for (k, v) in terms_d.iteritems()]
    terms_l.sort()
    terms_l.reverse()

    most_terms_l = terms_l[0: terms_amout]
    terms_d = dict([(k, v) for (v, k) in most_terms_l])

    return terms_d


def keep_atleast(term_d, terms_amount):
    """ keep_atleast(): is getting a dictionary of Terms-Frequencies and
        the amount of Terms to return as arguments. It is returning the number
        of Terms equal to the argument 'terms_amount' with the Highest Frequency.
        However if the subsequent terms have the same Frequency with the last
        one if the Returned dictionary then it will include this terms. """

    #  Get the TF list
    tf_l = term_d.items()

    #  Short by Frequency Max frequency goes first (Descending Order)
    tf_l = sorted(tf_l, key=lambda tf_l: tf_l[1], reverse=True)

    atleast_tf_l = tf_l[0:terms_amount]

    last_freq = atleast_tf_l[-1][1]

    for term, freq in tf_l[terms_amount:]:
        if freq == last_freq:
            atleast_tf_l.append((term, freq))

    terms_d = dict(atleast_tf_l)

    return terms_d


def keep_min_fq(term_d, min_freq):
    """ keep_min_fq(): is getting a dictionary of Terms-Frequencies and
        the minimum frequnecy value and retruns only the terms with this
        frequency and above. """

    return dict([(term, freq) for term, freq in term_d.items() if freq >= min_freq])
