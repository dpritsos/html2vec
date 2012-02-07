#
#    Module: String2TF   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.features.string2tpl: submodule of `html2tf` module defines the class BaseString2TPL """ 

import numpy as np


class BaseString2TPL(object):
    """ BaseString2TPL: Class
        Instance requires a TermsType Class to given as argument.
        TermsTypes Classces: 
            - html2vectors.termstypes.String2CNGramsList() : It creates a list of Character NGrams from a String
            - .
            - .
            - . 
        Methods:
            - tpl_dict(text): is getting a Text and returns a TPL in native Python Dictionary of positions-list 
            - tpl_narray(text, ndtype): is getting a Text and returns a TPL in Numpy Array of positions-list"""
    
    def __init__(self, termstype):
        self.tt = termstype
    
    
    def tpl_dict(self, text):
        
        #Create Terms List    
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None 
        
        #Count Terms and Build the Terms-PositionsList (TP) dictionary 
        TPL_d = dict()
        for i, trm in enumerate(terms_l):
            if trm in TPL_d: #if the dictionary of terms has the 'terms' as a key 
                TPL_d[ trm ].append(i)
            else: 
                TPL_d[ trm ] = [i]
                 
        return TPL_d        
    
    
    def tpl_array(self, text, ndtype=np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))] ) ):
        
        #NOTE REQUIRES RE-FACTORING
        
        #Create Terms List    
        terms_l = self.tt.terms_lst(text)
        
        #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
        if terms_l == None:
            return None
        
        #Count Terms and Terms-Frequencies 
        ##Find unique Terms and their occurrences in the text
        terms, inds = np.unique1d(terms_l, return_inverse=True)
        TPL_arr = np.zeros(len(terms), dtype=ndtype)
        
        ##Put the terms in place
        TPL_arr['terms'] = terms
        
        ##Put the Lists in place
        pos_arr_arr =[np.where(inds == idx) for idx in np.arange(len(terms))]
        for i, pos_arr in enumerate(pos_arr_arr):
            TPL_arr['pos'][i][0:len(pos_arr[0])] = pos_arr[0] + 1
            
        return TPL_arr
