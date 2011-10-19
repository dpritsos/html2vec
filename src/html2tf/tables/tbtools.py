""" """

import tables as tb


class TermPosFreq(tb.IsDescription):
    term = tb.StringCol()
    pos = tb.Int16Col()
    freq = tb.Float32Col()


class GenreTable(tb.IsDescription):
    wpg_id = tb.UInt64Col()
    wpg_name = tb.StringCol(itemsize=256) 
    tf = TermPosFreq()
    

class CorpusTable(object):
    
    def __init__(self, table_name="CorpusTable.h5", table_path="",\
                 ttypes_structures_lst=["words", "3grams", "inv-dictionaries"],\
                 cropus_name="Corpus", genres_lst=["Genre1"], coprus_paths_lst=""):
        table_name = table_path + table_name
        h5file = tb.openFile(table_name, mode="w")
        for group in ttypes_structures_lst:
            group1 = h5file.createGroup(h5file.root, group)
        #####
        table1 = h5file.createTable(group1, "table1", )
             
    
       
        
        