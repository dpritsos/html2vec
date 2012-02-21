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


class TFVects2Matrix2D(TFDictTools, TFTablesTools):
    
    def __init__(self, Dictionary=None):
        self.Dictionary = Dictionary
        
    
    def from_tables(self, h5file, tbgroup, tb_name_lst, data_type):
        
        #If no predefined Dictionary has given Build the Dictionary for the vector to be Projected (Aligned)   
        if not self.Dictionary:
            tf_d = self.merge_tfts2tfd(h5file, tbgroup, tb_name_lst, data_type)
            self.Dictionary = self.tf2tidx(tf_d)
        else:
            warnings.warn("Dictionary is already defined or created in previews usage of from_tables() function")
        
        #Row, Columns and Frequencies lists for csr_matrix()
        rows_l = list()
        cols_l = list()
        frequencies_l = list()  
        
        #Get frequencies for all terms in each Table and form the proper row and column indices
        row_c = -1 #Counts the Tables only for the ones exists in tb_name_list
        for tf_tb in h5file.walkNodes(tbgroup, classname='Table'):
            if tf_tb.name in tb_name_lst:
                row_c += 1 
                for tf in tf_tb.iterrows():
                    #Get the Index from the Dictionary as columns position and append it in the list - If term exists in the Dictionary
                    if tf['terms'] in self.Dictionary:
                        idx_in_Dict = self.Dictionary[ tf['terms'] ]
                        cols_l.append( idx_in_Dict )
                        #Append as row index the count number - As many times as the amount of terms(i.e. TFs) in the Table  
                        rows_l.append(row_c)
                        #Append the frequency of for this term (in this table row)
                        frequencies_l.append( tf['freq'] )
                    
        #Return Scipy CSR Sparse matrix 
        return ssp.csr_matrix((frequencies_l, (rows_l, cols_l)), dtype=np.float32)
    
    
    def from_dicts(self):
        pass
    
    def from_narrays(self):
        pass
    
    def from_matrixs(self):
        pass
    

 