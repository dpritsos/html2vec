#
#    Module: String2TF   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2tf.base.features.string2tf: submodule of `html2tf` module defines the class BaseString2TF """ 

import numpy as np


class BaseString2TF(object):
    """ BaseString2TF: Class
        Instance requires a TermsType Class to given as argument.
        TermsTypes Classces: 
            - html2vectors.termstypes.String2CNGramsList() : It creates a list of Character NGrams from a String
            - .
            - .
            - . 
        Methods:
            - tf_dict(text): is getting a Text and returns a TF in native Python Dictionary 
            - tf_narray(text, ndtype): is getting a Text and returns a TF in Numpy Array """
    
    def __init__(self, termstype):
        self.tt = termstype
    
    def tf_dict(self, text):
        
        #Create Terms List 
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Count Terms and Build the Terms-Frequency (TF) dictionary 
        TF_d = dict()
        for trm in terms_l:
            if trm in TF_d: #if the dictionary of terms has the 'terms' as a key 
                TF_d[ trm ] += 1
            else: 
                TF_d[ trm ] = 1
                 
        return TF_d  
    
    def tf_narray(self, text, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]) ):
        
        #Create Terms List
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Count Terms and Terms-Frequencies  
        terms, inds = np.unique1d(terms_l, return_inverse=True)
        freqs = np.bincount(inds)
        
        #Build Terms-Frequency (TF) dictionary
        #We need a Recored arrays to be created thus using numpy.rec.array.fromarrays() to be invoked as follows 
        #(alternatively fromarrays() can be used directly print terms
        TF_arr = np.rec.array([terms, freqs], dtype=ndtype)
        
        return TF_arr
    
    
     