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


class BaseString2LB(object):
    """ BaseString2LB: Class
        tid_dictionary must have index starting from 1 """
    
    def __init__(self, termstype, smoothing_kernel=stats.norm):
        self.tt = termstype
        self.kernel = smoothing_kernel 
    
    
    def lowbow(self, text, smth_pos_l, smth_sigma, tid_dictionary):
        
        #The Dictionary/Vocabulary 
        self.tid_d = tid_dictionary
        
        #Create Terms List 
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Define Terms Sequence Sparse Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms occurring at several Text's Positions
        ts_mtrx = ssp.dok_matrix( (len(self.tid_d), len(terms_l)), dtype='f')
        rows_idx_l = [ self.tid_d[term] for term in terms_l ]
        ts_mtrx[rows_idx_l, 0:len(terms_l)] = 1.0
        print "Done"
        ts_mtrx = ts_mtrx.tocoo()
        print "Done"
        
        #Prepare positions to be Smoothed-out 
        
        text_posz = np.arange(1, len(terms_l)+1)
        text_posz = (text_posz - 0.5) / text_posz.shape[0]  
        
        #Smoothing Process for all Smooting positions
        smoothd_sums = ssp.lil_matrix((len(smth_pos_l), len(self.tid_d)), dtype='f')
        for i, smth_pos in enumerate(smth_pos_l):
            smth_k = self.kernel.pdf([text_posz], smth_pos, smth_sigma)
            
            #Normalise Smoothing Kernel
            smth_k = smth_k / smth_k.sum()
            
            #Define Diagonal 2D matrix as Smoothing Kernel for one step weighting process (Cools trick with Matrices)
            smth_k_mtrx = ssp.dia_matrix((smth_k,[0]), shape=(smth_k.shape[1], smth_k.shape[1]))
            
            if ts_mtrx.shape[0] == 1:
                smoothd = ts_mtrx.tocsr() * smth_k_mtrx.tocsr().T #TRaspose maybe
            else:
                smoothd = (ts_mtrx.tocsr() * smth_k_mtrx.tocsr()).sum(1).T #TRaspose maybe

            smoothd_sums[i,:] = smoothd[0, rows_idx_l]
         
        #Sum up and return the sparse matrix for this string/text
        return ssp.csr_matrix( smoothd_sums.sum(0) )   
    
    