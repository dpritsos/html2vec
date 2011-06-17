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
        ngrams = self.bs2tf.nf_dict( self.txt_sample )
        self.assertEqual(ngrams, self.expected_ngrams)


class Test_Html2TF__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tf = charngrams.Html2TF( self.n )
        self.html2tf_lowercase = charngrams.Html2TF( self.n, lowercase=True )
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
        self.expected_ngrams_lowercase = {u'le ': 1, u's i': 1, u't t': 1, u's.b': 1, u'f c': 1, u's a': 1, u'htm': 2, u'ram': 1,\
                                          u'rs ': 1, u'tf ': 1, u's f': 1, u'.ch': 1, u't f': 1, u' un': 1, u'2tf': 2, u'.ba': 1,\
                                          u'l2t': 1, u'l2v': 1, u's p': 1, u'ses': 1, u'mod': 1, u'tes': 1, u'ge/': 1, u'ams': 1,\
                                          u'or ': 2, u'cha': 1, u'est': 2, u'st ': 1, u'for': 2, u'tor': 1, u' is': 1, u'ing': 1,\
                                          u'cla': 1, u'e/m': 1, u'fd.': 1, u'ml2': 2, u'pac': 1, u'arn': 1, u'ngr': 1, u'r h': 2,\
                                          u'ule': 1, u'har': 1, u'is ': 2, u'tml': 2, u'ng2': 1, u' cl': 1, u'ass': 1, u'tri': 1,\
                                          u'his': 1, u'kag': 1, u'str': 1, u'2ve': 1, u'tfd': 1, u'gra': 1, u'rng': 1, u'ors': 1,\
                                          u'it ': 1, u'odu': 1, u' pa': 1, u'ect': 1, u'ase': 1, u'dul': 1, u' te': 1, u'nit': 1,\
                                          u'las': 1, u' a ': 1, u'rin': 1, u'g2t': 1, u'cka': 1, u'bas': 1, u'd.c': 1, u'ack': 1,\
                                          u'age': 1, u' ht': 2, u'ms.': 1, u'/mo': 1, u'thi': 1, u'ss ': 1, u'uni': 1, u'cto': 1,\
                                          u'vec': 1, u' fo': 2, u'a u': 1}
        self.pathto_htmls = "../unit_test_data/html/"
        self.xhtml_file_l = [ "../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../unit_test_data/txt/test_01.txt" ]
                         
    def test_html2tf_from_src(self):
        html_ngrams = self.html2tf.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_ngrams) 
    
    def test_html2tf_from_src_lowercase(self):
        html_ngrams = self.html2tf_lowercase.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_ngrams_lowercase) 
       
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
    
        