#
#    Module: String2Lowbow
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.vectortypes.string2lowbow: submodule of `html2vect` module defines the class BaseString2LB """

from scipy import stats
import scipy.sparse as ssp
import numpy as np
import warnings


class BaseString2LB(object):
    """ BaseString2LB: Class
        tid_dictionary must have index starting from 1 """

    def __init__(self, termstype, smoothing_kernel=stats.norm, norm_func=None):
        self.tt = termstype
        self.kernel = smoothing_kernel
        self.norm_func = norm_func


    def _lowbow(self, terms_l, smth_pos_l, smth_sigma, tid_dictionary):

        trm_l_len = len(terms_l)
        #Get the indices for rows based on the Dictionary - Required for Terms-Sequence-Sparse-Matrix
        rows_idx_l = [ self.tid_d[term] for term in terms_l if term in self.tid_d ]
        if not rows_idx_l:
            rows_idx_l = [ len(self.tid_d) - 1 ]

        #Get the term_l left based on the Available Dictionary - Required for Terms-Sequence-Sparse-Matrix
        terms_l = [ term for term in terms_l if term in self.tid_d ]
        if not terms_l:
            terms_l = [ 0 ]

        #Define Terms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms occurring at several Text's Positions
        ts_mtrx = ssp.csr_matrix( (np.ones(len(terms_l), dtype=np.float), (np.array(rows_idx_l), np.arange(len(terms_l))) ),\
                                    shape=(len(self.tid_d), len(terms_l)) )

        #Prepare positions to be Smoothed-out
        text_posz = np.arange(1, len(terms_l)+1)
        text_posz = (text_posz - 0.5) / text_posz.shape[0]

        #Smoothing Process for all Smoothing positions
        smoothd_sums = ssp.lil_matrix((len(smth_pos_l), len(self.tid_d)), dtype=np.float)
        for i, smth_pos in enumerate(smth_pos_l):
            #PDF Re-Normalised based for the range [0,1]
            smth_k = self.kernel.pdf([text_posz], smth_pos, smth_sigma) / (self.kernel.cdf(1, smth_pos, smth_sigma) - self.kernel.cdf(0, smth_pos, smth_sigma))
            #Normalise Smoothing Kernel
            smth_k = smth_k / smth_k.sum()

            #Define Diagonal 2D matrix as Smoothing Kernel for one step weighting process (Cools trick with Matrices)
            smth_k_mtrx = ssp.dia_matrix((smth_k,[0]), shape=(smth_k.shape[1], smth_k.shape[1]))

            if ts_mtrx.shape[0] == 1:
                smoothd = ts_mtrx.tocsr() * smth_k_mtrx.tocsr().T #TRaspose maybe
            else:
                smoothd = (ts_mtrx.tocsr() * smth_k_mtrx.tocsr()).sum(1).T #TRaspose maybe

            #Get the proper weights respectively to the row indices and put them to the smoothd_sums matrix
            if smoothd[0, rows_idx_l].shape[1] != 1:
                ##print smoothd[0, rows_idx_l]
                smoothd_sums[i, rows_idx_l] = smoothd[0, rows_idx_l]
            else:
                #if there is only one element requires direct assignment
                smoothd_sums[i, rows_idx_l[0]] = smoothd[0, rows_idx_l[0]]

        #Get Normalised Smoothed Sums
        if self.norm_func:
            norm_smoothd_sums = self.norm_func( smoothd_sums, trm_l_len)
        else:
            norm_smoothd_sums = self.normalise( smoothd_sums )

        return ssp.csr_matrix( norm_smoothd_sums, shape=norm_smoothd_sums.shape, dtype=np.float)


    def lowbow(self, text, smth_pos_l, smth_sigma, tid_dictionary):

        #The Dictionary/Vocabulary
        self.tid_d = tid_dictionary

        #Create Terms List
        terms_l = self.tt.terms_lst(text)

        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None

        return self._lowbow(terms_l, smth_pos_l, smth_sigma, tid_dictionary)


    def yield_lowbow4seg(self, text, smth_pos_l, smth_sigma, tid_dictionary):

        #The Dictionary/Vocabulary
        self.tid_d = tid_dictionary

        #Create Terms List
        terms_l_seg = self.tt.terms_lst_segments(text)

        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l_seg == None:
            return None

        segment_lst = list()
        for terms_l in terms_l_seg:
            #print len(terms_l)
            segment_lst.append( self._lowbow(terms_l, smth_pos_l, smth_sigma, tid_dictionary) )

        segments2matrix = ssp.vstack(segment_lst)

        #Get Normalised Segments Sums
        if self.norm_func:
            norm_segments2matrix = self.norm_func( segments2matrix )
        else:
            #Warn that default normalisation will be performed
            warnings.warn('norm_func argument was None. Default normalisation will be performed (division by max value)')
            #Perform default normilisation
            norm_segments2matrix = self.normalise( segments2matrix )

        return ssp.csr_matrix(norm_segments2matrix, shape=norm_segments2matrix.shape, dtype=np.float)


    def normalise(self, smoothd_sums):

        #Sum up and return the sparse matrix for this string/text
        smoothd_sums_sum = smoothd_sums.sum(0)

        #Get Normalised Sum of Sums
        norm_smoothd_sums_sum = smoothd_sums_sum / np.max(smoothd_sums_sum)

        return norm_smoothd_sums_sum
