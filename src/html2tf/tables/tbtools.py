""" """

import tables as tb
import numpy as np
import scipy.sparse as scsp
#from html2tf.dictionaries.tfdtools import TFdictHandler 

   
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
                    

class TFTablesHandler(object):
    
    def __init__(self, h5file): 
        self.h5file = h5file
    
    def create(self, table_name="CorpusTable.h5", table_path="",\
                 ttypes_structures_lst=["words", "trigrams"], inv_dict=True,\
                 corpus_name="Corpus", genres_lst=["Genre1"], corpus_paths_lst=""):
        #Create HD5 file in user defined path
        table_name = table_path + table_name
        self.h5file = tb.openFile(table_name, mode="w")
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
    
    def pagetf_EArray(self, h5f_tmp, EArr, fileh, tbgroup, pagename_lst, term_idx_d, data_type=np.float32):
        """  """
        len_term_idx_d = len(term_idx_d)
        pgtf_arr = np.zeros((1,len_term_idx_d), dtype=data_type)
        #print np.shape(pgtf_arr)
        for irow_pgtf, pg_name in enumerate(pagename_lst):
            pg_tb = fileh.getNode(tbgroup, pg_name, classname='Table')
            for row in pg_tb:
                if row['terms'] in term_idx_d: 
                    #print row['terms'], term_idx_d[row['terms']], len_term_idx_d, row['freq'] 
                    pgtf_arr[0, term_idx_d[row['terms']] ] = row['freq'] 
                    #pgtf_arr[0, 0] = 0.0 #row['freq']
            EArr.append(pgtf_arr)
            pgtf_arr = np.zeros((1,len_term_idx_d), dtype=data_type)
        #h5f_tmp.flush()
        return EArr
    
    def TFTables2TFDict_n_TFArr(self, tbgroup, tb_name_lst, data_type):
        """ Merge_TFtbls2TFarray: TEMPRORERARLY IMPLEMENTATION 
            Returns:tf_arr                                        """
        tf_d = dict()
        for tf_tb in self.h5file.walkNodes(tbgroup, classname='Table'):
            if tf_tb.name in tb_name_lst: 
                print tf_tb.name
                for tf_row in tf_tb.iterrows():
                    if tf_row['terms'] in tf_d: 
                        tf_d[ tf_row['terms'] ] += tf_row['freq']
                    else:
                        tf_d[ tf_row['terms'] ] = tf_row['freq']
        tf_arr = np.rec.array(tf_d.items(), dtype=data_type)
        tf_arr.sort(order='freq')
        tf_arr = tf_arr[::-1]
        idxs = range( len(tf_arr) )
        #print idxs[0], idxs[-1], len(tf_arr) 
        term_idx_d = dict( zip( tf_arr['terms'] , idxs ) )
        return term_idx_d, tf_arr

    
    def merge_tf_tbls_Dicts(self, fileh, tb_diz_lst, saveto_grp, data_type=default_TF_3grams_dtype):
        """ mege_tf_tbls(): TEMPRORERARLY IMPLEMENTATION 
            is getting a set of term-frequency dictionaries as list of
            arguments and return a dictionary of common terms with their sum of frequencies
            of occurred in all dictionaries containing these terms. """
        tf_d = dict()
        for tf_tb in tb_diz_lst:
            if isinstance(tf_tb, str):
                tf_tb = fileh.getNode("/".join(tf_tb.split('/')[0:-1]), tf_tb.split('/')[-1])
            for tf_row in tf_tb.iterrows():
                if tf_row['terms'] in tf_d: 
                    tf_d[ tf_row['terms'] ] += tf_row['freq']
                else:
                    tf_d[ tf_row['terms'] ] = tf_row['freq']
        tf_arr = np.rec.array(tf_d.items(), dtype=data_type)
        #self.dcttmp_l.append( tf_d )
        dictionary_tb = fileh.createTable(saveto_grp, 'CorpusGlobalDictionaryNormMax', tf_arr)
        dictionary_tb.flush()
        del tf_arr
        return dictionary_tb
    
    def pagetf_array_old(self, fileh, tbgroup, pagename_lst, term_idx_d, data_type=np.float32):
        """  """
        len_tidd = len(term_idx_d)
        len_pgnlst= len(pagename_lst)
        
        pgtf_arr = np.zeros(len_tidd, dtype=data_type)
        for pg_name in pagename_lst:
            pg_tb = fileh.getNode(tbgroup, pg_name, classname='Table')
            pg_vect = np.zeros(len_tidd, dtype=data_type)
            for row in pg_tb:
                if row['terms'] in term_idx_d: 
                    pg_vect[ term_idx_d[row['terms']] - 1 ] = row['freq'] 
            pgtf_arr = np.vstack((pgtf_arr, pg_vect))
        return np.array( pgtf_arr[1:, :] ) 
    
    def pagetf_array_non_sparse(self, fileh, tbgroup, pagename_lst, term_idx_d, data_type=np.float32):
        """  """
        pgtf_arr = scsp.coo_matrix((len(pagename_lst), len(term_idx_d)), dtype=data_type)
        for irow_pgtf, pg_name in enumerate(pagename_lst):
            pg_tb = fileh.getNode(tbgroup, pg_name, classname='Table')
            for row in pg_tb:
                if row['terms'] in term_idx_d: 
                    pgtf_arr[irow_pgtf,  term_idx_d[row['terms']] - 1 ] = row['freq'] 
        return pgtf_arr
    
    
    def pagetf_array(self, fileh, tbgroup, pagename_lst, term_idx_d, data_type=np.float32):
        """  """
        pgtf_arr = np.zeros((len(pagename_lst), len(term_idx_d)), dtype=data_type)
        for irow_pgtf, pg_name in enumerate(pagename_lst):
            pg_tb = fileh.getNode(tbgroup, pg_name, classname='Table')
            for row in pg_tb:
                if row['terms'] in term_idx_d: 
                    pgtf_arr[irow_pgtf,  term_idx_d[row['terms']] ] = row['freq'] 
        return pgtf_arr
    
   
            

             
    
       
        
        