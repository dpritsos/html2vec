#
#    Module: String2TF   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.vectortypes.string2tf: submodule of `html2vect` module defines the class BaseString2TF """ 

import numpy as np
import scipy.sparse as ssp



class BaseString2TF(object):
    """ BaseString2TF: Class
        Instance requires a TermsType Class to given as argument.
        TermsTypes Classces: 
            - html2vectors.termstypes.String2CNGramsList() : It creates a list of Character NGrams from a String
            - .
            - .
            - . 
        Methods:
            - tf_dict(text,[tid_vocabulary* Optional]): is getting a Text and returns a TF in native Python Dictionary 
            - tf_narray(text, ndtype): is getting a Text and returns a TF in Numpy Array 
            - f_sparse(text, tid_vocabulary): ......"""
             
    def __init__(self, termstype):
        
        #Initialise Term Types
        self.tt = termstype
    
       
    def tf_dict(self, text, tid_vocabulary=None):
        
        #Create Terms List 
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Use the Vocabulary argument if any
        if tid_vocabulary:
            #If a Vocabulary was given as argument
            TF_d = dict( [(voc_term, 0) for voc_term in tid_vocabulary] )
            
            #Count Terms and Build the Terms-Frequency (TF) dictionary 
            for trm in terms_l:
                if trm in TF_d: #if the dictionary of terms has the 'terms' as a key 
                    TF_d[ trm ] += 1
                #else: 
                    #Not in the Vocabulary DROP THEM
            
        else:
            #If a Vocabulary was None
            TF_d = dict()
        
            #Count Terms and Build the Terms-Frequency (TF) dictionary 
            for trm in terms_l:
                if trm in TF_d: #if the dictionary of terms has the 'terms' as a key 
                    TF_d[ trm ] += 1
                else: 
                    TF_d[ trm ] = 1
                 
        return TF_d  
    
    
    def tf_narray(self, text, norm_func, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])):
        
        #Create Terms List
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Count Terms and Terms-Frequencies  
        terms, inds = np.unique1d(terms_l, return_inverse=True)
        freqs = np.bincount(inds)
        
        #Get Normalised Smoothed Sums
        if norm_func:
            norm_freqs = norm_func( freqs, len(terms_l))
        else:
            norm_freqs = freqs /  freqs.max() # OR f_mtrx.sum() 
        
        #Build Terms-Frequency (TF) dictionary
        #We need a Recored arrays to be created thus using numpy.rec.array.fromarrays() to be invoked as follows 
        #(alternatively fromarrays() can be used directly print terms
        TF_arr = np.rec.array([terms, norm_freqs], dtype=ndtype)
        
        return TF_arr
    
    
    def f_sparse(self, text, tid_dictionary, norm_func):
        
        #The Dictionary/Vocabulary 
        self.tid_d = tid_dictionary
        
        #Create Term-Frequency Dictionary 
        tf_d = self.tf_dict(text)
        
        #Get Terms_l
        terms_l = tf_d.keys()
        
        #Get the indices for terms following the sequence occurs in terms_l  
        col_idx_l = [ self.tid_d[term] for term in terms_l if term in self.tid_d ]
        if not col_idx_l:
            col_idx_l = [ len(self.tid_d) - 1 ]
        col_idx_a = np.array(col_idx_l)
        
        #Get the frequencies for terms following the sequence occurs in terms_l IN ORDER TO BE ALLIGNED WITH ids_l
        freq_l = [ tf_d[term] for term in terms_l if term in self.tid_d ]
        if not freq_l:
            freq_l = [ 0 ]
        
        #Define Terms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms occurring at several Text's Positions
        f_mtrx = ssp.csr_matrix( ( freq_l, (np.zeros_like(col_idx_a), col_idx_a) ), shape=(1, len(self.tid_d)), dtype=np.float32)
        
        #Get Normalised Smoothed Sums
        if norm_func:
            norm_f_mtrx = norm_func( f_mtrx, len(self.tid_d))
        else:
            norm_f_mtrx = f_mtrx /  f_mtrx.todense().max() # OR f_mtrx.sum() 
            
            
        return ssp.csr_matrix( norm_f_mtrx, shape=norm_f_mtrx.shape, dtype=np.float32)
    
    
     