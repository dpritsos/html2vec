""" Unit Test for regex.py """

import unittest
import words


class Test_BaseWordExtractionRegexTools(unittest.TestCase):
    
    def setUp(self):
        self.bwert = words.BaseWordExtractionRegexTools()
        self.htmlsample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                            <p>This is a unit test for <b>BaseRegexHtmlAttributes</b> class<br/>for htmlattrib.regex module</p>\
                            </body>\
                           </html>"
        self.expected_text = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module "
                           
    def test_get_proper_numbers(self):
        html_text = self.htmlattrib.text( self.htmlsample )
        self.assertEqual(html_text, self.expected_text)
            
    def test_get_comma_n_trms(self):
        pass
    
    def test_get_dot_n_trms(self):
        pass
    
    def test_get_propr_trms_n_symbs(self):
        pass
    
    def test_term_len_limit(self):
        pass
    

class Test_BaseString2TF(unittest.TestCase):
    
    def setUp(self):
        self.htmltext = words.BaseString2TF()
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
        
    def test_basestring2tf_tf_dict(self):
        pass
    
        
class Test_Html2TF(unittest.TestCase):
    
    def setUp(self):
        self.htmltext = words.Html2TF()
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
    
    def test_html2tf_save_consitency(self):
        expctd_txt = self.htmltext.load_files(["../unit_test_data/txt/test_01.txt"], encoding='utf-8', error_handling='strict')
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf-8', error_handling='strict' )
        fname_fstr_l = [ ["../unit_test_data/txt/test_02.txt", html_text[0] ] ]
        self.htmltext.save_files(None, fname_fstr_l, encoding='utf8', error_handling='strict')
        reloaded_txt = self.htmltext.load_files("../unit_test_data/txt/test_02.txt", encoding='utf-8', error_handling='strict')
        #import difflib
        #for i in difflib.context_diff(expctd_txt[0][0:-1], F.read()):
        #    print i
        self.assertEqual(reloaded_txt, expctd_txt[0][0:-1])
        

suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseWordExtractionRegexTools) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
    
        