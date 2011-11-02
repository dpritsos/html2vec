""" """

import tables as tb
import numpy as np


class TermPosFreq(tb.IsDescription):
    term = tb.StringCol(itemsize=128)
    pos = tb.UInt16Col()
    freq = tb.Float32Col()
    
default_GenreTable_dtype = np.dtype([('wpg_id', 'uint64'),\
                               ('wpg_name', 'S256'),\
                               ('links_lst', 'uint64', 100),\
                               ('TF', "S128, uint16, float32", 500)
                               ]) # Still Working on it!

default_TF_dtype = np.dtype( [('term', 'S128'), ('pos', 'uint16'), ('freq', 'float32')] ) #OK!
                            

#default_TF_dtype = np.dtype([('term', 'S128')])

#class default_GenreTable(tb.IsDescription):
#    wpg_id = tb.UInt64Col()
#    wpg_name = tb.StringCol(itemsize=256)
#    links_lst = tb.UInt64Col(shape=(100)) 
#    TF = tb.Col.from_dtype( dtype=default_TF_dtype )
   

class CorpusTable(object):
    
    def __init__(self, genre_table=default_GenreTable_dtype, table_name="CorpusTable.h5", table_path="",\
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
                gtable = self.h5file.createTable(grp, gnr, genre_table) #GenreTable is a Nested-Table
                gtable.attrs.path_name = ""
    
    def get(self):
        return self.h5file
            

if __name__ == "__main__": #SAMPLE CODE TO BE REMOVED WHEN UnitTest-File will be ready
    
    testTable = CorpusTable(np.zeros(1,dtype=default_GenreTable_dtype), table_name="Santinis.h5", corpus_name="Santinis_corpus", genres_lst=[ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"])
    
    print testTable.get()
    
    print testTable.get().root.Santinis_corpus._v_attrs.genres_lst
    
    testTable.get().close()
             
    
       
        
        