""" """

import tables as tb
import numpy as np

   
class default_GenreTable_Desc(tb.IsDescription):
    wpg_id = tb.UInt64Col(pos=1)
    wpg_name = tb.StringCol(pos=2, itemsize=256)
    terms_num = tb.UInt64Col(pos=3)
    status_code = tb.UInt32Col(pos=4)
    links_lst = tb.UInt64Col(pos=5, shape=(100))
    
class default_TF_3grams_desc(tb.IsDescription):
    terms = tb.StringCol(pos=1, itemsize=3)
    freq = tb.Float32Col(pos=2) 
    
default_GenreTable_dtype = np.dtype( [('wpg_id', 'uint64'), ('wpg_name', 'S256'), ('links_lst', 'uint64', 100)] )

default_TF_dtype = np.dtype( [('terms', 'S128'), ('freq', 'float32')] ) 
default_TF_3grams_dtype = np.dtype( [('terms', 'S3'), ('freq', 'float32')] )
default_TP_dtype = np.dtype( [('terms', 'S128'), ('pos', 'uint16')] )
default_TP_3grams_dtype = np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))] )
                    

class TFTablesHandler(object):
    
    def __init__(self): # genre_table=default_GenreTable_dtype, table_name="CorpusTable.h5", table_path="",\
                        #ttypes_structures_lst=["words", "trigrams"], inv_dict=True,\
                        #corpus_name="Corpus", genres_lst=["Genre1"], corpus_paths_lst=""):
        pass
    
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
    
    def merge_tf_tbls(self, fileh, tbgroup, tb_not=None):
        """ mege_tf_tbls(): TEMPRORERARLY IMPLEMENTATION 
            is getting a set of term-frequency dictionaries as list of
            arguments and return a dictionary of common terms with their sum of frequencies
            of occurred in all dictionaries containing these terms. """
        #dictionary_tb = fileh.getNode( tbgroup + '/Dictionary' )
        #print dictionary_tb
        #if not dictionary_tb: 
        dictionary_tb = fileh.createTable(tbgroup, 'Dictionary', default_TF_3grams_desc)
        for tf_tb in fileh.walkNodes(tbgroup, classname='Table'):
            if tf_tb.name == tb_not: continue
            for tf_row in tf_tb.iterrows():
                print tf_row['terms'].replace('"', '\\"')
                idx_lst = dictionary_tb.getWhereList('terms == "'+tf_row['terms'].replace('"', '\\"')+'"' )
                if len(idx_lst) > 1:
                    print idx_lst
                    print tf_row['terms']
                    raise Exception("IT SUPOSE NOT TO HAVE MORE THAN ONE IDEXES RETURED")
                if idx_lst:
                    row = dictionary_tb[ idx_lst[0] ].row
                    row['freq'] += tf_row['freq']
                    row.update()
                else:
                    row = dictionary_tb.row
                    row['terms'] = tf_row['terms']
                    row['freq'] = tf_row['freq']
                    row.append()
            dictionary_tb.flush
        return dictionary_tb
    
    #def gen_tfd_frmlist(self, tf_d_l):
    #    """ gen_tfd_frmlist(): is getting a list of Term-Frequency Dictionaries and creates a 
    #        TF Dictionary of all terms occurred in the list. """
    #    return self.merge_tf_dicts( *tf_d_l )
    
    #def tf2tidx(self, term_d):
    #    """ tf2tidx(): is getting a Term-Frequency dictionary and returns one
    #        with terms-index number. The index number is just their position in the
    #        descending order sorted list of dictionary keys. """
    #    term_l = term_d.keys()
    #    term_l.sort()
    #    idx = range( len(term_l) + 1 )
    #    term_idx_d = dict( zip( term_l , idx[1:] ) )
    #    return term_idx_d
                    
    #def __tf2idxf(self, tf_d, tidx_d):
    #    """ __tf2idxf(): Don't use it directly, use tf2idxf instead.
    #        This function is getting a TF dictionary representing the TF Vector,
    #        and a TF-Index as defined in VHTools.tf_dict_idxing(). It returns
    #        a Index-Frequency dictionary where each term of the TF dictionary has been 
    #        replaced with the Index number of the TF-Index. In case the term of the 
    #        TF Dictionary is not in the TF-Index then the term is just Dropped. Therefore,
    #        the Index-Frequency dictionary it will no more include the missing (from TF-Index) term. """
    #    idxed_d = dict() 
    #    for term, freq in tf_d.items():
    #        if term in tidx_d:
    #            idxed_d[ tidx_d[term] ] = freq
    #        #else: DROP THE TERM
    #    return idxed_d
    
    #def tf2idxf(self, tf_d_l, tf_idx_d):
    #    """ tf2idxf(): is getting a TF-Dictionary or a list of TF-Dictionaries and TF-Index. It applies
    #        the VHTools.__tf2idxf() function to the dictionaries and returns a list or single TF-Dictionary
    #        depending on the input. """
    #    if isinstance(tf_d_l, list):
    #        idxed_d = list()
    #        for tf_d in tf_d_l:
    #            idxed_d.append( self.__tf2idxf(tf_d, tf_idx_d) )
    #        return idxed_d
    #    elif isinstance(tf_d_l, dict):
    #        return self.__tf2idxf(tf_d_l, tf_idx_d)
    #    else:
    #        raise Exception("Dictionary or a List of Dictionaries was expected as fist input argument")
    
    #def keep_atleast(self, terms_d, terms_amount):
    #    """ keep_most(): is getting a dictionary of Terms-Frequencies and 
    #        the amount of Terms to return as arguments. It is returning the number
    #        of Terms equal to the argument 'terms_amount' with the Highest Frequency.
    #        However if the subsequent terms have the same Frequency with the last
    #        one if the Returned dictionary then it will include this terms. """
    #    terms_l = [(v, k) for (k, v) in terms_d.iteritems()]
    #    terms_l.sort()
    #    terms_l.reverse()
    #    atlest_terms_l = terms_l[0:terms_amount]
    #    last_freq = atlest_terms_l[-1][0]
    #    print last_freq
    #    for freq, term in terms_l[terms_amount:]:
    #        if freq == last_freq:
    #            atlest_terms_l.append( (freq, term) )
    #    terms_d = dict( [ (k, v) for (v, k) in atlest_terms_l ] )
    #    return terms_d

    #def keep_most(self, terms_d, terms_amout):
    #    """ keep_most(): is getting a dictionary of Terms-Frequencies and 
    #        the amount of Terms to return as arguments. It is returning the number
    #        of Terms equal to the argument 'terms_amount' with the Highest Frequency. """
    #    terms_l = [(v, k) for (k, v) in terms_d.iteritems()]
    #    terms_l.sort()
    #    terms_l.reverse()
    #    most_terms_l = terms_l[0: terms_amout]
    #    terms_d = dict( [ (k, v) for (v, k) in most_terms_l ] )
    #    return terms_d    
            

if __name__ == "__main__": #SAMPLE CODE TO BE REMOVED WHEN UnitTest-File will be ready
    
    testTable = CorpusTable()
    
    testTable.create(table_name="Santinis.h5", corpus_name="Santinis_corpus", genres_lst=[ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"])
    
    print testTable.get()
    
    print testTable.get().root.Santinis_corpus._v_attrs.genres_lst
    
    testTable.get().close()
             
    
       
        
        