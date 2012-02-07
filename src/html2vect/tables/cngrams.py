#
#    Module: Character NGrams - from html row text/files to native python character ngrams TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.cngrams: submodule of `html2tf` module defines the classes:
    HtmlTF(), HtmlTP()"""

__package__ = "html2tf.dict.cngrams"

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.features.string2tf import BaseString2TF
from ..base.features.string2tp import BaseString2TPL
from ..base.io.baseio import BaseIO
import tbtools 


class IO(BaseIO):
    
    def from_src(self, fileh, tablesGroup, xhtml_str, tbname="tbarray1"):
        T_F_or_P_arr = self._attrib(xhtml_str)
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
            terms_tb_arr = self.from_src2tbls(fileh, tablesGroup, xhtml_str, tbname=table_name)
            terms_tb_arr._v_attrs.filepath = xhtml_file_l[ i ] 
            terms_tb_arr.flush()
        return tablesGroup  
        
    def from_paths(self, fileh, tablesGroup, grn_wpg_tbl_name, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        tablesGroup = self.from_files2tbls(fileh, tablesGroup, xhtml_file_l, encoding, error_handling)
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

 
class Html2TF(BaseString2TF, BaseHTML2Attributes, IO):
    
    def __init__(self, n, lowercase, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TF.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tf_array( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_array( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TPL, BaseHTML2Attributes, IO):
    
    def __init__(self, n, lowercase, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TPL.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tpl_array( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tpl_array( self.text( xhtml_str ).lower() )


    