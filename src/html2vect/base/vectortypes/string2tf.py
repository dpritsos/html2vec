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
            TF_d = dict()
            
            #Count Terms and Build the Terms-Frequency (TF) dictionary 
            for trm in terms_l:
                if trm in tid_vocabulary:
                    if trm in TF_d: #if the dictionary of terms has the 'terms' as a key 
                        TF_d[ trm ] += 1
                    else: 
                        TF_d[ trm ] = 1
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
            norm_freqs = freqs # If norm_func is None or 0 then do not normalise
        
        #Build Terms-Frequency (TF) dictionary
        #We need a Recored arrays to be created thus using numpy.rec.array.fromarrays() to be invoked as follows 
        #(alternatively fromarrays() can be used directly print terms
        TF_arr = np.rec.array([terms, norm_freqs], dtype=ndtype)
        
        return TF_arr
    
    
    def f_sparse(self, text, tid_dictionary, norm_func):
               
        #Create Term-Frequency Dictionary 
        tf_d = self.tf_dict(text)

        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if tf_d == None:
            return None 
        
        #Get Terms_l
        terms_l = tf_d.keys()
        
        #Get the indices for terms following the sequence occurs in terms_l  
        col_idx_l = [ tid_dictionary[term] for term in terms_l if term in tid_dictionary ]
        if not col_idx_l:
            col_idx_l = [ len(tid_dictionary) - 1 ]
        col_idx_a = np.array(col_idx_l)
        
        #Get the frequencies for terms following the sequence occurs in terms_l IN ORDER TO BE ALLIGNED WITH ids_l
        freq_l = [ tf_d[term] for term in terms_l if term in tid_dictionary ]
        if not freq_l:
            freq_l = [ 0 ]
        
        #Define Terms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms occurring at several Text's Positions
        f_mtrx = ssp.csr_matrix( ( freq_l, (np.zeros_like(col_idx_a), col_idx_a) ), shape=(1, len(tid_dictionary)), dtype=np.float32)
        
        #Get Normalised Smoothed Sums
        if norm_func:
            norm_f_mtrx = norm_func( f_mtrx, len(tid_dictionary))
        else:
            norm_f_mtrx = f_mtrx # If norm_func is None or 0 then do not normalise
            
            
        return ssp.csr_matrix( norm_f_mtrx, shape=norm_f_mtrx.shape, dtype=np.float32)


    def f_narray(self, text, tid_dictionary, norm_func, d2=False):

        #Getting the sparse matrix aligned along to the Terms-Index of the Corpus' Vocabulary
        sparse_mtrx = self.f_sparse(text, tid_dictionary, norm_func)

        #Convering the spaser matric to dense array
        dense_arr = sparse_mtrx.toarray()    

        #Getting the containent of the documents frequencies in 2d of 1d array depending on the argument
        if d2:
            freq_arr = dense_arr
        else:
            freq_arr = dense_arr[0]

        return freq_arr
    
     