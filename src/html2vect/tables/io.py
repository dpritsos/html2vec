#
#    Module: I/O
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.table.io: submodule of `html2vect` module defines the class IO() which overrides BaseIO"""

import tbtools 
import numpy as np

from ..base.io.baseio import BaseIO

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