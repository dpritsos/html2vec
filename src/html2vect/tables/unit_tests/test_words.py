#
#    Unit Test for html2vect.dict.words
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
import html2vect.tables.words as words
from html2vect.string.attrib_text import HtmlFullText 
from html2vect.base.termstypes.words import String2WordList

import numpy as np
import tables as tb
import pickle

################################### REQUIRES A UNIT TEST FOR words.Html2TPL Class ################################# 

class Test_Html2TF(unittest.TestCase):
    
    def setUp(self):
        self.html2tf = words.Html2TF(lowercase=False, valid_html=True, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))
        self.html2tf_lowercase = words.Html2TF(lowercase=True, valid_html=True, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]) )
        self.htmltext = HtmlFullText(valid_html=True)
        self.str2wl = String2WordList()
        
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test (IT IS!) for <b>html2tfd.charngrams.BaseString2TF.</b> class, @package/module html2vectors</p>\
                            </body>\
                           </html>"
        
        self.expected_words_arr = np.array( [('', 1.0), ('(', 1.0), (')', 1.0), (',', 1.0), ('.', 1.0), ('@', 1.0),\
                                             ('IS!', 1.0), ('IT', 1.0), ('This', 1.0), ('a', 1.0), ('class', 1.0),\
                                             ('for', 1.0), ('html2tfd.charngrams.BaseString2TF', 1.0), ('html2vectors', 1.0),\
                                             ('is', 1.0), ('package/module', 1.0), ('test', 1.0), ('unit', 1.0)],\
                                             np.dtype([('terms', 'S128'), ('freq', 'float32')]) )
         
        self.expected_words_freq_arr_lowercase = np.array( [('', 1.0), ('(', 1.0), (')', 1.0), (',', 1.0), ('.', 1.0), ('@', 1.0),\
                                                            ('a', 1.0), ('class', 1.0), ('for', 1.0), ('html2tfd.charngrams.basestring2tf', 1.0),\
                                                            ('html2vectors', 1.0), ('is', 1.0), ('is!', 1.0), ('it', 1.0), ('package/module', 1.0),\
                                                            ('test', 1.0), ('this', 1.0), ('unit', 1.0)],\
                                                            np.dtype([('terms', 'S128'), ('freq', 'float32')]) )
        
       
        self.tables_filename = "../../../unit_test_data/hd5files/CorpusTable.h5"
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
        
        
    def test_html2tf_from_src(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, 'w')
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        
        #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method 
        #which is called again and again for each of the test_ methods into this Unit-test Class
        words_arr = self.html2tf.from_src(h5file, group_h5, self.html_sample, tbname="tbarray1")
        
        #Assert the Results
        for val, exp_val in zip(words_arr.read(), self.expected_words_arr):
            self.assertEqual(val, exp_val)
        
        #Close the file for the next Loop of Unit-Test
        h5file.close()
    
    
    def test_html2tf_from_src_lowercase(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, 'w')
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        
        #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method 
        #which is called again and again for each of the test_ methods into this Unit-test Class
        words_arr = self.html2tf_lowercase.from_src(h5file, group_h5, self.html_sample, tbname="tbarray1")
        
        for val, exp_val in zip(words_arr.read(), self.expected_words_freq_arr_lowercase):
            self.assertEqual(val, exp_val)
            
        #Close the file for the next Loop of Unit-Test 
        h5file.close()
                         
       
    def test_html2tf_from_files(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, 'w')
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        words_lst = self.str2wl.terms_lst(html_text[0])
        words_arrz_group = self.html2tf.from_files(h5file, group_h5, self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        ng_num_expected = len(words_lst)
        ng_num_real = 0
        test_table = h5file.getNode(words_arrz_group, 'test_01_html') 
        ng_num_real += np.sum( test_table.read()['freq'] )        
        self.assertEqual(ng_num_real, ng_num_expected)
        self.assertEqual(test_table._v_attrs.filepath, self.xhtml_file_l[0]) 
        self.assertEqual(test_table._v_attrs.terms_num, ng_num_expected)
        
        #Close the file for the next Loop of Unit-Test
        h5file.close()
        
      
    def test_html2tf_from_paths(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, 'w')
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        words_lst = self.str2wl.terms_lst(html_text[0])
        words_arrz_group = self.html2tf_lowercase.from_paths(h5file, group_h5, 'GenrePageListTable', None,\
                                                                   self.pathto_htmls, encoding='utf8', error_handling='strict' )
        
        #Assert for the Filename-List returned
        ### THIS IS A COMPLICTED STRUCTURE BE AWARE --> tb_trms_frq_arrz_group[1].read()['wpg_name']
        self.assertEqual(words_arrz_group[1].read()['filename'], self.xhtml_file_l)
        
        #Assert for the amount of Ngrams greated
        ng_num_expected = len(words_lst)
        ng_num_real = 0
        test_table = h5file.getNode(words_arrz_group[0], 'test_01_html') 
        ng_num_real += np.sum( test_table.read()['freq'] )        
        self.assertEqual(ng_num_real, ng_num_expected)
        
        #Close the file for the next Loop of Unit-Test
        h5file.close()

    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF) )

unittest.TextTestRunner(verbosity=2).run(suite)        
    
            