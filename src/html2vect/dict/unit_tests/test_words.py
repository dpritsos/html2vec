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
import html2vect.dict.words as words
from html2vect.string.attrib_text import HtmlFullText 
from html2vect.base.termstypes.words import String2WordList
import pickle


################################### REQUIRES A UNIT TEST FOR words.Html2TPL Class ################################# 

               
class Test_Html2TF(unittest.TestCase):
    
    def setUp(self):
        self.html2tf = words.Html2TF( lowercase=False, valid_html=True )
        self.html2tf_lowercase = words.Html2TF( lowercase=True, valid_html=True )
        self.htmltext = HtmlFullText(valid_html=True)
        self.str2wl = String2WordList()
        
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test (IT IS!) for <b>html2tfd.charngrams.BaseString2TF.</b> class, @package/module html2vectors</p>\
                            </body>\
                           </html>"
        
        self.expected_words = {u'a': 1, u'@': 1, u',': 1, u'html2vectors': 1, u'for': 1, u'This': 1, u'(': 1,\
                               u'is': 1, u'IT': 1, u'.': 1, u')': 1, u'test': 1, u'package/module': 1, u'IS!': 1,\
                               u'class': 1, u'html2tfd.charngrams.BaseString2TF': 1, u'unit': 1, u'': 1} 
         
        self.expected_words_lowercase = {u'a': 1, u'@': 1, u',': 1, u'html2vectors': 1, u'for': 1, u'this': 1, u'(': 1,\
                                         u'is': 1, u'it': 1, u'.': 1, u')': 1, u'test': 1, u'package/module': 1, u'is!': 1,\
                                         u'class': 1, u'html2tfd.charngrams.basestring2tf': 1, u'unit': 1, u'': 1}
        
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
                          
                          
    def test_html2tf_from_src(self):
        words = self.html2tf.from_src( self.html_sample )
        self.assertEqual(words, self.expected_words) 


    def test_html2tf_from_src_lowercase(self):
        html_ngrams = self.html2tf_lowercase.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_words_lowercase) 
        
       
    def test_html2tf_from_files(self):
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        words_lst = self.str2wl.terms_lst(html_text[0])
        html_words = self.html2tf.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        #Count the Length of Words List returned
        tf_num_expected = len(words_lst)
        
        #Count the total amount of Frequencies of the TF returned 
        tf_num_real = 0
        for tf in html_words[0].values():
            tf_num_real += float(tf)
            
        #Do the AssertEqual where the lists should be equal
        self.assertEqual(tf_num_real, tf_num_expected)

  
    def test_html2tf_from_paths(self):
        html_text = self.htmltext.from_paths(None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        words_lst = self.str2wl.terms_lst(html_text[0][1])
        html_words = self.html2tf.from_paths(None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        
        #Count the Length of Words List returned
        tf_num_expected = len(words_lst)
        
        #Count the total amount of Frequencies of the TF returned 
        tf_num_real = 0
        for tf in html_words[0][1].values():
            tf_num_real += float(tf)
            
        #Do the AssertEqual where the lists should be equal in:
        #The amount of Terms found
        self.assertEqual(tf_num_real, tf_num_expected)
        
        #The Files (i.e. filenames) found in the paths
        self.assertEqual(html_words[0][0], self.xhtml_file_l[0])
 

suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
            