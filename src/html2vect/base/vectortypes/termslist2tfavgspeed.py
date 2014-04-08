#
#    Module: String2TF   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.vectortypes.termslist2tfavgspeed: submodule of `html2tf` module defines the class BaseString2TPL """ 

import numpy as np
from termslist2tf import *


def trms2tpl_dict(terms_l):
     
    #In case None is returned then return None again. The outer code layer should handle this if caused due to error.
    if terms_l == None:
        return None 
    
    #Count Terms and Build the Terms-PositionsList (TP) dictionary 
    TPL_d = dict()
    for i, trm in enumerate(terms_l):
        if trm in TPL_d: #if the dictionary of terms has the 'terms' as a key 
            TPL_d[ trm ].append(i + 1)
        else: 
            TPL_d[ trm ] = [i + 1]
             
    return TPL_d        
    

def trms2tfspd_dict(terms_l, vocabulary=None):

    #Getting the terms positions lists dictionary.
    trms_pos = trms2tpl_dict(terms_l)

    #Gettring the terms frequencies dictionary.
    trms_tf = trms2tf_dict(terms_l, vocabulary)

    #Creating the list of average-frequency-speeds of terms found in terms_lst.
    tfs_list = [ (t, f / (float(max(trms_pos[t]) - min(trms_pos[t])) + 1.0) ) for t, f in trms_tf.items() ]

    #Retunring the terms dictonary of average-frequency-speeds.
    return dict(tfs_list)

    

