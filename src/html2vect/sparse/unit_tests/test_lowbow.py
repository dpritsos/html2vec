#
#    Unit Test for html2vect.sparse.lowbow
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
import html2vect.sparse.lowbow as lowbow
from html2vect.string.attrib_text import HtmlFullText 
#import pickle

from scipy import stats 


class Test_Html2LBN__3grams_GausseKernel(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2lbn = lowbow.Html2LBN( self.n, lowercase=False, valid_html=True , smoothing_kernel=stats.norm)
        self.html2lbn_lowercase = lowbow.Html2LBN( self.n, lowercase=True, valid_html=True , smoothing_kernel=stats.norm)
        self.htmltext = HtmlFullText(valid_html=True)
                        
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../../unit_test_data/txt/test_01.txt" ]
                         
                         
    def test_html2lbn_from_src(self):
        #html_ngrams = self.html2tf.from_src( self.html_sample )
        #self.assertEqual(html_ngrams, self.expected_ngrams_freq)
        pass
        
        
    def test_html2lbn_from_files(self):
        #html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        html_lowbow = self.html2lbn.from_files( self.xhtml_file_l, [1,2,3,4,5], 0.5, tid_dictionary=None, encoding='utf8', error_handling='strict' )
        
        print html_lowbow[0].todense()
        
        #ng_num_expected = len(html_text[0]) - self.n + 1
        #ng_num_real = 0
        #for nf in html_ngrams[0].values():
        #    ng_num_real += float(nf)
        #self.assertEqual(ng_num_real, ng_num_expected)
   
"""
    def test_html2lbn_from_files_lowercase(self):
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        html_ngrams = self.html2tf.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        
        ng_num_expected = len(html_text[0]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams[0].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)     


    def test_html2lbn_from_paths(self):
        html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        
        html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict')
        
        #ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
        ng_num_expected = len(html_text_l[0][1]) - self.n + 1
        ng_num_real = 0
        for nf in html_ngrams_l[0][1].values():
            ng_num_real += float(nf)
        self.assertEqual(ng_num_real, ng_num_expected)
        
        
 
class Test_Html2LBW__3grams(unittest.TestCase):
    
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
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2LBN__3grams_GausseKernel) )
#suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TPL__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        