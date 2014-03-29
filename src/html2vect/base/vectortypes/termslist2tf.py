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
     
    #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
    if terms_l == None:
        return None 
    
    #Use the Vocabulary argument if any
    if vocabulary:
        #If a Vocabulary was given as argument
        TF_d = dict()
        
        #Count Terms and Build the Terms-Frequency (TF) dictionary 
        for trm in terms_l:
            if trm in vocabulary:
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


def trms2tf_narray(terms_l, norm_func, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])):
    
    #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
    if terms_l == None:
        return None 
    
    #Count Terms and Terms-Frequencies  
    terms, inds = np.unique(terms_l, return_inverse=True)
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


def trms2f_sparse(terms_l, tid_vocabulary, norm_func=None, ndtype=np.float32):
           
    #Create Term-Frequency Dictionary Keeping only the terms of interest given into Terms-Index Vocabulary
    tf_d = trms2tf_dict(terms_l, vocabulary=tid_vocabulary)

    #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
    if tf_d == None:
        return None 
     
    #Getting the indices for terms indeceis for. Following the sequence stored into the current python dictionary.
    col_idx_l = tid_vocabulary.values()

    #Sice the return value will be a sparce vector first dimention of the matrix will be 0 for all terms.
    dim0 = np.zeros(len(col_idx_l))
    
    #Getting the frequencies for terms of interst in order to be alligned idxs-list.
    freq_l = [ tf_d[term] for term in tid_vocabulary.keys() ]
    if not freq_l:
        freq_l = [ 0 ]

    #Define Terms-Sequence-Sparse-Matrix i.e a 2D matrix of Dictionary(Rows) vs Terms occurring at several Text's Positions
    f_mtrx = ssp.csr_matrix( ( freq_l, (dim0, col_idx_l) ), shape=(1, len(col_idx_l)), dtype=ndtype)
    
    #Get Normalised Smoothed Sums
    if norm_func:
        norm_f_mtrx = norm_func( f_mtrx, len(tid_vocabulary))
    else:
        norm_f_mtrx = f_mtrx # If norm_func is None or 0 then do not normalise
        
    return ssp.csr_matrix( norm_f_mtrx, shape=norm_f_mtrx.shape, dtype=ndtype)


def trms2f_narray(terms_l, tid_vocabulary, norm_func=None, d2=False, ndtype=np.float32):

    #Getting the sparse matrix aligned along to the Terms-Index of the Corpus' Vocabulary
    sparse_mtrx = trms2f_sparse(terms_l, tid_vocabulary, norm_func, ndtype)

    #Convering the spaser matric to dense array
    dense_arr = sparse_mtrx.toarray()    

    #Getting the containent of the documents frequencies in 2d of 1d array depending on the argument
    if d2:
        freq_arr = dense_arr
    else:
        freq_arr = dense_arr[0]

    return freq_arr

 