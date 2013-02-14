#
#    Module: Character NGrams - from html row text/files to PyTables EArrays character ngrams TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.cngrams: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTPL()"""

from ..base.html2terms import BaseHtml2TF
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.vectortypes.string2tpl import BaseString2TPL


class Html2TF(BaseHtml2TF):
    
    #Define the TermsType to be produced from this class 
    s2ngl = String2CNGramsList()
    
       
    def __init__(self, *args, **kwrgs):
            
        #Initialise BaseHtml2TF Class   
        super(Html2TF, self).__init__(*args, **kwrgs)
            
                
    def yield_(self, xhtml_str):
        return self.s2tf.tf_narray( self.h2attr.text( xhtml_str ), self.ndtype )
    
    
    def from_src(self, fileh, tablesGroup, xhtml_str, tbname="tbarray1"):
        T_F_or_P_arr = self.yield_(xhtml_str)
        #This line has been add to prevent error when None is returned from cngrams.BaseString2TFTP methods
        status_code = 0
        if T_F_or_P_arr == "":
            T_F_or_P_arr = np.zeros(1 ,dtype=tbtools.default_TF_dtype)
            status_code = 1
        terms_tb_arr = fileh.createTable(tablesGroup, tbname, T_F_or_P_arr)
        terms_tb_arr._v_attrs.terms_num = np.sum(terms_tb_arr.read()['freq'])
        terms_tb_arr._v_attrs.status = status_code
        return terms_tb_arr
        
        
    def from_files(self, fileh, tablesGroup, xhtml_file_l, encoding='utf8', error_handling='strict'):
        for i, xhtml_str in enumerate(self.load_files(xhtml_file_l, encoding, error_handling)):
            table_name = xhtml_file_l[ i ].split('/')[-1]
            table_name = table_name.replace('.','_')
            table_name = table_name.replace('-','__')
            table_name = table_name.replace(' ','')
            terms_tb_arr = self.from_src(fileh, tablesGroup, xhtml_str, tbname=table_name)
            terms_tb_arr._v_attrs.filepath = xhtml_file_l[ i ] 
            terms_tb_arr.flush()
        return tablesGroup  
    
        
    def from_paths(self, fileh, tablesGroup, grn_wpg_tbl_name, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        tablesGroup = self.from_files(fileh, tablesGroup, xhtml_file_l, encoding, error_handling)
        GenrePageListTable = fileh.createTable(tablesGroup, grn_wpg_tbl_name, tbtools.default_GenreTable_Desc)
        for i, file_tb in enumerate(fileh.walkNodes(tablesGroup, classname='Table')):
            #This line preventing to update the GenrePageListTable with its own meta-attributes (not available anyway) 
            if file_tb.name == GenrePageListTable.name: 
                continue 
            GenrePageListTable.row['id'] = i
            GenrePageListTable.row['table_name'] = file_tb.name
            GenrePageListTable.row['filename'] = file_tb._v_attrs.filepath
            GenrePageListTable.row['terms_num'] = file_tb._v_attrs.terms_num 
            GenrePageListTable.row['status_code'] = file_tb._v_attrs.status
            #GenrePageListTable.row['link_lst' ] = np.zeros(100)
            GenrePageListTable.row.append()
        GenrePageListTable.flush() 
        return (tablesGroup, GenrePageListTable) 
    
    
    
class Html2TPL(Html2TF):
    
    #Define the TermsType to be produced from this class 
    s2ngl = String2CNGramsList()
    
       
    def __init__(self, *args, **kwrgs):
            
        #Initialise BaseHtml2TF Class   
        super(Html2TPL, self).__init__(*args, **kwrgs)
        
        #Initialise BaseString2TPL class
        self.s2tpl = BaseString2TPL(self.__class__.s2ngl)
            
                
    def yield_(self, xhtml_str):
        return self.s2tpl.tpl_narray( self.h2attr.text( xhtml_str ), self.ndtype)
    



    