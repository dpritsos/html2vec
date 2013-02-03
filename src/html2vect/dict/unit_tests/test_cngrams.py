#
#    Unit Test for html2vect.dict.cngrams
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
import html2vect.dict.cngrams as cngrams
from html2vect.string.attrib_text import HtmlFullText 
import pickle


class Test_Html2TF__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tf = cngrams.Html2TF( self.n, lowercase=False, valid_html=True )
        self.html2tf_lowercase = cngrams.Html2TF( self.n, lowercase=True, valid_html=True )
        self.htmltext = HtmlFullText(valid_html=True)
        
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>html2tfd.charngrams.BaseString2TF</b> class for html2vectors package/module</p>\
                            </body>\
                           </html>"
        
        self.expected_ngrams_freq = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                     '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                     'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                     ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                     'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                     'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                     'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                     'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                     'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                     'vec': 1, ' fo': 2, 'a u': 1, 'le ': 1} 
        
        #NOTICE the 'le ':1 on the above dictionary which is extra 3gram compare toTest_BaseString2NgramList__3grams because of HTML clean-up process 
        self.expected_ngrams_freq_lowercase = {u'le ': 1, u's i': 1, u't t': 1, u's.b': 1, u'f c': 1, u's a': 1, u'htm': 2, u'ram': 1,\
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
        
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../../unit_test_data/txt/test_01.txt" ]
                         
                         
    def test_html2tf_from_src(self):
        html_ngrams = self.html2tf.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_ngrams_freq) 
    
    
    def test_html2tf_from_src_lowercase(self):
        html_ngrams = self.html2tf_lowercase.from_src( self.html_sample )
        self.assertEqual(html_ngrams, self.expected_ngrams_freq_lowercase) 
       
       
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
        
        html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict')
        
        #ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
        ng_num_expected = len(html_text_l[0][1]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams_l[0][1].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)
        
"""      
class Test_Html2TPL__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tp = cngrams.Html2TPL( self.n, lowercase=False, valid_html=True )
        self.html2tp_lowercase = cngrams.Html2TPL( self.n, lowercase=True, valid_html=True )
        self.htmltext = HtmlFullText(valid_html=True)
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>html2tfd.charngrams.BaseString2TF</b> class for html2vectors package/module</p>\
                            </body>\
                           </html>"
        
        #NOTICE the 'le ':1 on the bellow dictionary which is extra 3gram compare toTest_BaseString2NgramList__3grams because of HTML clean-up process
        self.expected_ngrams_pos = {u'le ': [94], u's i': [4], u't t': [14], u'ase': [46], u's a': [7], u'htm': [25, 69], u'ram': [40], u'rs ': [79],\
                                    u'TF ': [56], u's f': [63], u'.ch': [33], u't f': [19], u' un': [10], u'2tf': [29], u'l2t': [28],\
                                    u'l2v': [72], u's p': [80], u'eSt': [48], u'tes': [16], u'ge/': [87], u'ams': [41], u'or ': [22, 66],\
                                    u'cha': [34], u'est': [17], u'st ': [18], u'Str': [49], u'for': [21, 65], u'tor': [77], u' is': [5],\
                                    u'ing': [52], u'cla': [59], u'e/m': [88], u'fd.': [31], u'ml2': [27, 71], u'pac': [82], u'arn': [36],\
                                    u'ngr': [38], u'r h': [23, 67], u'2TF': [55], u'har': [35], u'is ': [3, 6], u'tml': [26, 70], u'F c': [57],\
                                    u'ass': [61], u'tri': [50], u'g2T': [54], u'his': [2], u'kag': [85], u'Bas': [45], u'2ve': [73], u'tfd': [30],\
                                    u'gra': [39], u'rng': [37], u'ors': [78], u'it ': [13], u'odu': [91], u'mod': [90], u' pa': [81], u'ect': [75],\
                                    u'ule': [93], u'Thi': [1], u's.B': [43], u' te': [15], u'.Ba': [44], u'nit': [12], u'las': [60], u' a ': [8],\
                                    u'rin': [51], u'seS': [47], u'cka': [84], u' cl': [58], u'd.c': [32], u'dul': [92], u'ack': [83], u'age': [86],\
                                    u' ht': [24, 68], u'ms.': [42], u'/mo': [89], u'ng2': [53], u'ss ': [62], u'uni': [11], u'cto': [76], u'vec': [74],\
                                    u' fo': [20, 64], u'a u': [9]}
            
        self.expected_ngrams_freq_lowercase = {u'le ': [94], u's i': [4], u't t': [14], u's.b': [43], u'f c': [57], u's a': [7], u'htm': [25, 69], u'ram': [40],\
                                               u'rs ': [79], u'tf ': [56], u's f': [63], u'.ch': [33], u't f': [19], u' un': [10], u'2tf': [29, 55], u'.ba': [44],\
                                               u'l2t': [28], u'l2v': [72], u's p': [80], u'ses': [47], u'mod': [90], u'tes': [16], u'ge/': [87], u'ams': [41],\
                                               u'or ': [22, 66], u'cha': [34], u'est': [17, 48], u'st ': [18], u'for': [21, 65], u'tor': [77], u' is': [5],\
                                               u'ing': [52], u'cla': [59], u'e/m': [88], u'fd.': [31], u'ml2': [27, 71], u'pac': [82], u'arn': [36], u'ngr': [38],\
                                               u'r h': [23, 67], u'ule': [93], u'har': [35], u'is ': [3, 6], u'tml': [26, 70], u'ng2': [53], u' cl': [58],\
                                               u'ass': [61], u'tri': [50], u'his': [2], u'kag': [85], u'str': [49], u'2ve': [73], u'tfd': [30], u'gra': [39],\
                                               u'rng': [37], u'ors': [78], u'it ': [13], u'odu': [91], u' pa': [81], u'ect': [75], u'ase': [46], u'dul': [92],\
                                               u' te': [15], u'nit': [12], u'las': [60], u' a ': [8], u'rin': [51], u'g2t': [54], u'cka': [84], u'bas': [45],\
                                               u'd.c': [32], u'ack': [83], u'age': [86], u' ht': [24, 68], u'ms.': [42], u'/mo': [89], u'thi': [1], u'ss ': [62],\
                                               u'uni': [11], u'cto': [76], u'vec': [74], u' fo': [20, 64], u'a u': [9]}
        
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
        self.pckld_file_pos_list = "../../../unit_test_data/pickled/pckled_pos_lst.pkl"
        
                         
    def test_html2tp_from_src(self):
        html_ngrams_pos = self.html2tp.from_src( self.html_sample )
        self.assertEqual(html_ngrams_pos, self.expected_ngrams_pos) 

    
    def test_html2tp_from_src_lowercase(self):
        html_ngrams_pos = self.html2tp_lowercase.from_src( self.html_sample )
        self.assertEqual(html_ngrams_pos, self.expected_ngrams_freq_lowercase) 

       
    def test_html2tp_from_files(self):
        pos_lst_f = open(self.pckld_file_pos_list, "r")
        
        #load previously pickled list of Terms Positions pickle.dump(vals_ll, fl)
        pos_lst = pickle.load(pos_lst_f)
        html_ngrams_tp = self.html2tp.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        self.assertEqual(html_ngrams_tp, pos_lst)       


    def test_html2tp_from_paths(self):
        pos_lst_f = open(self.pckld_file_pos_list, "r")
        
        #load previously pickled list of Terms Positions pickle.dump(vals_ll, fl)
        pos_lst = pickle.load(pos_lst_f)
        html_ngrams_tp_l = self.html2tp.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict')
        
        #html_ngrams_tp_l[0][  0 <-- ] contains the filenames
        self.assertEqual(html_ngrams_tp_l[0][1], pos_lst[0])
         """
    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF__3grams) )
#suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TPL__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        