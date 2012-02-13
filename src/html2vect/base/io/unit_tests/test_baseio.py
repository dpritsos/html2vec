#
#    Unit Test for html2vect.base.io.baseio
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#


### html2vect.base.io.baseio defines only an Abstract Class therefore it is it will be unit-tested from the the child-class overrids _attrib() method ###
##### Soon the code below will be Deprecated ##### 


import unittest

class Test_HtmlText(unittest.TestCase):
    
    def setUp(self):
        self.htmltext = attrib.HtmlText(valid_html=True)
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
                         
                         
    def test_htmltxt_from_src(self):
        html_text = self.htmltext.from_src( self.htmlsample )
        self.assertEqual(html_text, self.expected_text)
        
        
    def test_htmltxt_from_files(self):
        expctd_txt = self.htmltext.load_files(self.txt_file_l, encoding='utf-8', error_handling='strict').next() #Note next()
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        self.assertEqual(html_text[0], expctd_txt[0:-1])


    def test_htmltxt_from_paths(self):
        expctd_txt = self.htmltext.load_files(self.txt_file_l, encoding='utf-8', error_handling='strict').next()
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict') 
        self.assertEqual(html_text_l[0][1], expctd_txt[0:-1])

    
    def test_htmltxt_save_consitency(self):
        expctd_txt = self.htmltext.load_files(["../unit_test_data/txt/test_01.txt"], encoding='utf-8', error_handling='strict').next()
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf-8', error_handling='strict' )
        fname_fstr_l = [ ["../unit_test_data/txt/test_02.txt", html_text[0] ] ]
        self.htmltext.save_files(None, fname_fstr_l, encoding='utf8', error_handling='strict')
        reloaded_txt = self.htmltext.load_files("../unit_test_data/txt/test_02.txt", encoding='utf-8', error_handling='strict')
        self.assertEqual(reloaded_txt, expctd_txt[0:-1])
        
    

suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_HtmlText) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    