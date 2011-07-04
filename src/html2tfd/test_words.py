""" Unit Test for html2tfd.charngrams.py """

import unittest
import words
#import htmlattrib.regex as htmlre

class Test_BaseString2TF(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = words.BaseString2TF()
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF. class, @package/module html2vectors"
        self.expected_words = {'a': 1, '@': 1, 'html2vectors': 1, 'for': 1, 'This': 1, 'is': 1, ',': 1,\
                               '.': 1, 'test': 1, 'package/module': 1, 'html2tfd.charngrams.BaseString2TF': 1,\
                               'class': 1, 'unit': 1}
                           
    def test_basestring2tf_nf_dict(self):
        words = self.bs2tf.tf_dict( self.txt_sample )
        self.assertEqual(words, self.expected_words)
        
        
class Test_Html2TF(unittest.TestCase):
    
    def setUp(self):
        self.html2tf = words.Html2TF()
        self.html2tf_lowercase = words.Html2TF(lowercase=True )
        #self.htmltext = htmlre.HtmlText()
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test (IT IS!) for <b>html2tfd.charngrams.BaseString2TF.</b> class, @package/module html2vectors</p>\
                            </body>\
                           </html>"
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_words = {u'a': 1, u'@': 1, u'html2vectors': 1, u'for': 1, u'!)': 1, u'(': 1, u'IS': 1, u',': 1,\
                               u'.': 1, u'html2tfd.charngrams.BaseString2TF': 1, u'This': 1, u'test': 1, u'package/module': 1,\
                               u'IT': 1, u'class': 1, u'is': 1, u'unit': 1} 
        self.expected_words_lowercase = {u'a': 1, u'@': 1, u'html2vectors': 1, u'for': 1, u'!)': 1, u'(': 1, u'is': 2,\
                                         u',': 1, u'.': 1, u'this': 1, u'test': 1, u'it': 1, u'package/module': 1,\
                                         u'html2tfd.charngrams.basestring2tf': 1, u'class': 1, u'unit': 1}
        self.expec_xhtmls_dict_len = 1118
        self.pathto_htmls = "../unit_test_data/html/"
        self.xhtml_file_l = [ "../unit_test_data/html/test_01.html" ]
                         
    def test_html2tf_from_src(self):
        words = self.html2tf.from_src( self.html_sample )
        self.assertEqual(words, self.expected_words) 

    def test_html2tf_from_src_lowercase(self):
        html_ngrams = self.html2tf_lowercase.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_words_lowercase) 
       
    def test_html2tf_from_files(self):
        #html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        html_words = self.html2tf.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        self.assertEqual(len(html_words[0]), self.expec_xhtmls_dict_len)

    def test_html2tf_from_paths(self):
        #html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        html_words_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=False )
        self.assertEqual(len(html_words_l[0][1]), self.expec_xhtmls_dict_len)
           
    def test_html2tf_from_paths_low_mem(self):
        #html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        html_words_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
        self.assertEqual(len(html_words_l[0][1]), self.expec_xhtmls_dict_len)
    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
            