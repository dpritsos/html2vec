#
#    Module: TFTTools - Term-Frequency PyTables tools
# 
#    Author: Dimitrios Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.convert.tfttools: submodule of `html2vect` module defines the class TFTablesTools """

import tables as tb
import numpy as np
import scipy.sparse as scsp

   
class default_GenreTable_Desc(tb.IsDescription):
    id = tb.UInt32Col(pos=1)
    table_name = tb.StringCol(pos=2, itemsize=64)
    filename = tb.StringCol(pos=3, itemsize=256)
    terms_num = tb.UInt64Col(pos=4)
    status_code = tb.UInt32Col(pos=5)
    links_lst = tb.UInt64Col(pos=6, shape=(100))
    
class default_TF_3grams_desc(tb.IsDescription):
    terms = tb.StringCol(pos=1, itemsize=3)
    freq = tb.Float32Col(pos=2) 
    
default_GenreTable_dtype = np.dtype( [('wpg_id', 'uint64'), ('wpg_name', 'S256'), ('links_lst', 'uint64', 100)] )

default_TF_dtype = np.dtype( [('terms', 'S128'), ('freq', 'float32')] ) 
default_TF_3grams_dtype = np.dtype( [('terms', 'S3'), ('freq', 'float32')] )
default_TP_dtype = np.dtype( [('terms', 'S128'), ('pos', 'uint16')] )
default_TP_3grams_dtype = np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))] )
                    

class TFTablesTools(object):
    
    def __init__(self, h5file): 
        self.h5file = h5file
    
    def create(self, ttypes_structures_lst=["words", "trigrams"], inv_dict=True,\
                 corpus_name="Corpus", genres_lst=["Genre1"], corpus_paths_lst=""):
        #Create Corpus Group
        corpus_group = self.h5file.createGroup(self.h5file.root, corpus_name)
        corpus_group._v_attrs.paths = corpus_paths_lst
        corpus_group._v_attrs.genres_lst = genres_lst
        corpus_group._v_attrs.genres_num = len(genres_lst)
        #Create Terms Types Groups
        for grp in ttypes_structures_lst:
            self.h5file.createGroup(corpus_group, grp)
        #Create TermsType-Position-Frequency Tables for each genre
        for grp in ["/"+corpus_name+"/"+ttype for ttype in ttypes_structures_lst]:
            for gnr in genres_lst:
                self.h5file.createGroup(grp, gnr)
        return self.h5file
    
    def get(self):
        return self.h5file
    
    
    def merge_tfts2tfd(self, h5file, tbgroup, tb_name_lst, data_type):
        """ merge_tfts2tfd: TEMPRORERARLY IMPLEMENTATION 
            Returns:tf_d                        """
        
        #Terms-Frequency Dictionary to be returned 
        tf_d = dict()
        
        #Walk throught h5file of TF-Tables and use only the Tables in the tb_name_lst  
        for tf_tb in h5file.walkNodes(tbgroup, classname='Table'):
            if tf_tb.name in tb_name_lst: 
                #Count the Global Frequency of each terms in the TF-Tables Collection
                for tf_row in tf_tb.iterrows():
                    if tf_row['terms'] in tf_d:
                        tf_d[ tf_row['terms'] ] += tf_row['freq']
                    else:
                        tf_d[ tf_row['terms'] ] = tf_row['freq']
                        
        return tf_d
    
    
    def resize_tfd(self, tf_d, tfd_size):
        """ resize_tfd(): is getting a dictionary of Terms-Frequencies and 
            the amount of Terms to return as arguments. It is returning the number
            of Terms equal to the argument 'tfd_size' with the Highest Frequency.
            However if the subsequent terms have the same Frequency with the last
            one in the Returned dictionary then it will include this terms. """
        
        #Get the TF list
        tf_l = tf_d.items()
        #Short by Frequency Max frequency goes first (Descending Order)
        tf_l = sorted(tf_l, key=lambda tf_l: tf_l[1], reverse=True)    
        
        #Get the maximum index to keep - Having the same Frequency as the item located at tfd_size
        freq_l = [itm[1] for itm in tf_l]
        freq_arr = np.array(freq_l)
        #The + 1 is required for keeping the last item with the equal to the tfd_size-item's frequency
        max_idx = np.max( np.where( freq_arr==freq_arr[0:tfd_size] ) ) + 1
        
        #Keep the proper size of the new Dictionary and Rebuild it
        tf_d = dict( tf_l[0:max_idx] )
        
        return tf_d
    
    
    def TFTabels2EArray(self, earr, tbgroup, tb_name_lst, term_idx_d, data_type=np.float32):
        """ TEMPRORERARLY IMPLEMENTATION """
        len_term_idx_d = len(term_idx_d)
        pgtf_arr = np.zeros((1,len_term_idx_d), dtype=data_type)
        for tf_tb in self.h5file.walkNodes(tbgroup, classname='Table'):
            if tf_tb.name in tb_name_lst: 
                for row in tf_tb:
                    if row['terms'] in term_idx_d: 
                        #print row['terms'], term_idx_d[row['terms']], len_term_idx_d, row['freq']
                        #print term_idx_d[row['terms']]
                        #print pgtf_arr.shape  
                        pgtf_arr[0, term_idx_d[row['terms']] ] = row['freq'] 
                        #pgtf_arr[0, 0] = 0.0 #row['freq']
                earr.append(pgtf_arr)
                pgtf_arr = np.zeros((1,len_term_idx_d), dtype=data_type)
        return earr

    
   
            

        