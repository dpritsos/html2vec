#
#    Module: Convert - Converts from several Term-Frequency Dictionaries/NArrays/PyTables/Matricies to a 2D Matrix/Array etc. 
# 
#    Author: Dimitrios Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.convert.convert: submodule of `html2vect` module defines the class TFVects2Matrix2D """

import numpy as np
import scipy.sparse as ssp

from .tfdtools import TFDictTools
from .tfttools import TFTablesTools

import warnings

    
def TFVects2Matrix2D(h5file, Dictionary, DSize, tbgroup, tb_name_lst, data_type):
    
    #If no predefined Dictionary has given Build the Dictionary for the vector to be Projected (Aligned)   
    if not Dictionary:
        tf_d = merge_tfts2tfd(h5file, tbgroup, tb_name_lst, data_type)
        
        #In case it is required only sub-set of the created Dictionary it is kept only this and
        #the last few terms that have the same frequency to the last one user requested
        if DSize:
            tf_d = resize_tfd(tf_d, DSize)
        
        #The Terms-Indices Dictionary
        Dictionary = tf2tidx(tf_d)
        
    else:
        warnings.warn("Dictionary is already defined or created in previews usage of from_tables() function")
    
    #Row, Columns and Frequencies lists for csr_matrix()
    rows_l = list()
    cols_l = list()
    frequencies_l = list()  
    
    #Get frequencies for all terms in each Table and form the proper row and column indices
    rows_c = -1 #Counts the Tables only for the ones exists in tb_name_list
    for tf_tb in h5file.walkNodes(tbgroup, classname='Table'):
        if tf_tb.name in tb_name_lst:
            rows_c += 1
            
            for tf in tf_tb.iterrows():
                #Get the Index from the Dictionary as columns position and append it in the list - If term exists in the Dictionary
                if tf['terms'] in Dictionary:
                    idx_in_Dict = Dictionary[ tf['terms'] ]
                    cols_l.append( idx_in_Dict )
                    
                    #Append as row index the count number - As many times as the amount of terms(i.e. TFs) in the Table  
                    rows_l.append(rows_c)
                                            
                    #Append the frequency of for this term (in this table row)
                    frequencies_l.append( tf['freq'] )
                
    #Return Scipy CSR Sparse matrix - shape is really import for keeping consistency when several matrices are created using the same Dictionary
    return ssp.csr_matrix((frequencies_l, (rows_l, cols_l)), shape=(rows_c + 1, len(Dictionary)) , dtype=np.float32)

