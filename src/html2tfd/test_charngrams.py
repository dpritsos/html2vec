""" Unit Test for html2tfd.charngrams.py """

import unittest
import charngrams
import htmlattrib.regex as htmlre

class Test_BaseString2TF__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = charngrams.BaseString2TF(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_ngrams = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                'vec': 1, ' fo': 2, 'a u': 1}
                           
    def test_basestring2tf_nf_dict(self):
        #ngrams = self.bs2tf.nf_dict( self.txt_sample )
        #self.assertEqual(ngrams, self.expected_ngrams)
        pass

class Test_Html2TF__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tf = charngrams.Html2TF( self.n )
        self.htmltext = htmlre.HtmlText()
        
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>html2tfd.charngrams.BaseString2TF</b> class for html2vectors package/module</p>\
                            </body>\
                           </html>"
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_ngrams = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                'vec': 1, ' fo': 2, 'a u': 1, 'le ': 1}
        self.pathto_htmls = "../unit_test_data/html/"
        self.xhtml_file_l = [ "../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../unit_test_data/txt/test_01.txt" ]
                         
    def test_html2tf_from_src(self):
        html_ngrams = self.html2tf.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_ngrams) 
       
    def test_html2tf_from_files(self):
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        html_ngrams = self.html2tf.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        ng_num_expected = len(html_text[0]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams[0].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)

    def test_html2tf_from_paths(self):
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=False )
        #ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
        ng_num_expected = len(html_text_l[0][1]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams_l[0][1].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)
           
    def test_html2tf_from_paths_low_mem(self):
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
        #ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
        ng_num_expected = len(html_text_l[0][1]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams_l[0][1].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)

    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF__3grams) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        