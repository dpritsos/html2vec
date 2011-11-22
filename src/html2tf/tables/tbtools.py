""" """

import tables as tb
import numpy as np

   
class default_GenreTable_Desc(tb.IsDescription):
    wpg_id = tb.UInt64Col(pos=1)
    wpg_name = tb.StringCol(pos=2, itemsize=256)
    links_lst = tb.UInt64Col(pos=3, shape=(100)) 
    
default_GenreTable_dtype = np.dtype( [('wpg_id', 'uint64'), ('wpg_name', 'S256'), ('links_lst', 'uint64', 100)] )

default_TF_dtype = np.dtype( [('terms', 'S128'), ('freq', 'float32')] ) 
default_TF_3grams_dtype = np.dtype( [('terms', 'S3'), ('freq', 'float32')] )
default_TP_dtype = np.dtype( [('terms', 'S128'), ('pos', 'uint16')] )
default_TP_3grams_dtype = np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))] )
                    

class CorpusTable(object):
    
    def __init__(self): # genre_table=default_GenreTable_dtype, table_name="CorpusTable.h5", table_path="",\
                        #ttypes_structures_lst=["words", "trigrams"], inv_dict=True,\
                        #corpus_name="Corpus", genres_lst=["Genre1"], corpus_paths_lst=""):
        pass
    
    def create(self, genre_table=default_GenreTable_dtype, table_name="CorpusTable.h5", table_path="",\
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
        for grp in self.h5file.walkGroups(where="//"):
            for gnr in genres_lst:
                gtable = self.h5file.createTable(grp, gnr, genre_table)
                gtable.attrs.path_name = ""
        return self.h5file
    
    def get(self):
        return self.h5file
            

#if __name__ == "__main__": #SAMPLE CODE TO BE REMOVED WHEN UnitTest-File will be ready
    
#    testTable = CorpusTable()
    
#    testTable.create(default_GenreTable_Desc, table_name="Santinis.h5", corpus_name="Santinis_corpus", genres_lst=[ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"])
    
#    print testTable.get()
    
#    print testTable.get().root.Santinis_corpus._v_attrs.genres_lst
    
#    testTable.get().close()
             
    
       
        
        