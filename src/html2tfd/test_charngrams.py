""" Unit Test for html2tfd.charngrams.py """

import unittest
import charngrams

class Test_BaseString2TF(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = charngrams.BaseString2TF(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.txt_sample_shifted_right = " This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_text = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module "
                           
    def test_basestring2tf_nf_dict_3grams(self):
        ngrams = self.bs2tf.nf_dict( self.txt_sample_shifted_right )
        print ngrams
        self.assertEqual(self.txt_sample, self.txt_sample)

""" 
class Test_Html2TF(unittest.TestCase):
    
    def setUp(self):
        self.htmltext = charngrams.Html2TF()
        self.htmlsample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>BaseRegexHtmlAttributes</b> class<br/>for htmlattrib.regex module</p>\
                            </body>\
                           </html>"
        self.pathto_htmls = "../unit_test_data/html/"
        self.xhtml_file_l = [ "../unit_test_data/html/test_01.html" ]
        self.expected_text = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module "
        self.txt_file_l = [ "../unit_test_data/txt/test_01.txt" ]
                         
    def test_html2tf_from_src(self):
        html_text = self.htmltext.from_src( self.htmlsample )
        self.assertEqual(html_text, self.expected_text)
        
    def test_html2tf_from_files(self):
        expctd_txt = self.htmltext.load_files(self.txt_file_l, encoding='utf-8', error_handling='strict')
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        self.assertEqual(html_text[0], expctd_txt[0][0:-1])
    
    def test_html2tf_from_paths(self):
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=False )
        expctd_txt = self.htmltext.load_files(self.txt_file_l, encoding='utf-8', error_handling='strict')
        self.assertEqual(html_text_l[0][1], expctd_txt[0][0:-1])
        
    def test_html2tf_from_paths_low_mem(self):
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
        expctd_txt = self.htmltext.load_files(self.txt_file_l, encoding='utf-8', error_handling='strict')
        self.assertEqual(html_text_l[0][1], expctd_txt[0][0:-1])
"""   
    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF) )
#suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        