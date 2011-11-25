""" Unit Test for html2tfd.charngrams.py """

import unittest
import cngrams
import htmlattrib.attrib as htmlre
import pickle

class Test_BaseString2NgramList__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tl = cngrams.BaseString2NgramList(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_terms_lst = ['Thi', 'his', 'is ', 's i', ' is', 'is ', 's a', ' a ', 'a u', ' un', 'uni', 'nit', 'it ', 't t',\
                                   ' te', 'tes', 'est', 'st ', 't f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2t',\
                                   '2tf', 'tfd', 'fd.', 'd.c', '.ch', 'cha', 'har', 'arn', 'rng', 'ngr', 'gra', 'ram', 'ams', 'ms.',\
                                   's.B', '.Ba', 'Bas', 'ase', 'seS', 'eSt', 'Str', 'tri', 'rin', 'ing', 'ng2', 'g2T', '2TF', 'TF ',\
                                   'F c', ' cl', 'cla', 'las', 'ass', 'ss ', 's f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml',\
                                   'ml2', 'l2v', '2ve', 'vec', 'ect', 'cto', 'tor', 'ors', 'rs ', 's p', ' pa', 'pac', 'ack', 'cka',\
                                   'kag', 'age', 'ge/', 'e/m', '/mo', 'mod', 'odu', 'dul', 'ule']
    
    def test_terms_lst(self):
        terms_l = self.bs2tl.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


class Test_BaseString2TFTP__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = cngrams.BaseString2TFTP(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_ngrams_freq = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                     '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                     'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                     ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                     'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                     'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                     'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                     'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                     'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                     'vec': 1, ' fo': 2, 'a u': 1}
        self.expected_ngrams_pos = {'s i': [3], 't t': [13], 'ase': [45], 's a': [6], 'htm': [24, 68], 'ram': [39], 'rs ': [78],\
                                    'TF ': [55], 's f': [62], '.ch': [32], 't f': [18], ' un': [9], '2tf': [28], 'l2t': [27],\
                                    'l2v': [71], 's p': [79], 'eSt': [47], 'tes': [15], 'ge/': [86], 'ams': [40], 'or ': [21, 65],\
                                    'cha': [33], 'est': [16], 'st ': [17], 'Str': [48], 'for': [20, 64], 'tor': [76], ' is': [4],\
                                    'ing': [51], 'cla': [58], 'e/m': [87], 'fd.': [30], 'ml2': [26, 70], 'pac': [81], 'arn': [35],\
                                    'ngr': [37], 'r h': [22, 66], '2TF': [54], 'har': [34], 'is ': [2, 5], 'tml': [25, 69], 'F c': [56],\
                                    'ass': [60], 'tri': [49], 'g2T': [53], 'his': [1], 'kag': [84], 'Bas': [44], '2ve': [72], 'tfd': [29],\
                                    'gra': [38], 'rng': [36], 'ors': [77], 'it ': [12], 'odu': [90], 'mod': [89], ' pa': [80], 'ect': [74],\
                                    'ule': [92], 'Thi': [0], 's.B': [42], ' te': [14], '.Ba': [43], 'nit': [11], 'las': [59], ' a ': [7],\
                                    'rin': [50], 'seS': [46], 'cka': [83], ' cl': [57], 'd.c': [31], 'dul': [91], 'ack': [82], 'age': [85],\
                                    ' ht': [23, 67], 'ms.': [41], '/mo': [88], 'ng2': [52], 'ss ': [61], 'uni': [10], 'cto': [75], 'vec': [73],\
                                    ' fo': [19, 63], 'a u': [8]}
                           
    def test_basestring2tf_nf_dict(self):
        ngrams_freq = self.bs2tf.nf_dict( self.txt_sample )
        self.assertEqual(ngrams_freq, self.expected_ngrams_freq)
        
    def test_basestring2tf_npos_dict(self):
        ngrams_pos = self.bs2tf.npos_dict( self.txt_sample )
        self.assertEqual(ngrams_pos, self.expected_ngrams_pos)


class Test_Html2TF__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tf = cngrams.Html2TF( self.n )
        self.html2tf_lowercase = cngrams.Html2TF( self.n, lowercase=True )
        self.htmltext = htmlre.HtmlText()
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>html2tfd.charngrams.BaseString2TF</b> class for html2vectors package/module</p>\
                            </body>\
                           </html>"
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
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
        self.pathto_htmls = "../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../unit_test_data/txt/test_01.txt" ]
                         
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
    
    #### DEPRICATED ####      
    #def test_html2tf_from_paths_low_mem(self):
    #    html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
    #    html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
    #    #ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
    #    ng_num_expected = len(html_text_l[0][1]) - self.n + 1
    #    ng_num_real = 0
    #    for nf in html_ngrams_l[0][1].values():
    #        ng_num_real += float(nf)
    #    self.assertEqual(ng_num_real, ng_num_expected)
        
        
class Test_Html2TP__3grams(unittest.TestCase):
    
    def setUp(self):
        self.n = 3
        self.html2tp = cngrams.Html2TP( self.n )
        self.html2tp_lowercase = cngrams.Html2TP( self.n, lowercase=True )
        self.htmltext = htmlre.HtmlText()
        self.html_sample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                             <p>This is a unit test for <b>html2tfd.charngrams.BaseString2TF</b> class for html2vectors package/module</p>\
                            </body>\
                           </html>"
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        #NOTICE the 'le ':1 on the bellow dictionary which is extra 3gram compare toTest_BaseString2NgramList__3grams because of HTML clean-up process
        self.expected_ngrams_pos = {u'le ': [93], u's i': [3], u't t': [13], u'ase': [45], u's a': [6], u'htm': [24, 68], u'ram': [39], u'rs ': [78],\
                                    u'TF ': [55], u's f': [62], u'.ch': [32], u't f': [18], u' un': [9], u'2tf': [28], u'l2t': [27],\
                                    u'l2v': [71], u's p': [79], u'eSt': [47], u'tes': [15], u'ge/': [86], u'ams': [40], u'or ': [21, 65],\
                                    u'cha': [33], u'est': [16], u'st ': [17], u'Str': [48], u'for': [20, 64], u'tor': [76], u' is': [4],\
                                    u'ing': [51], u'cla': [58], u'e/m': [87], u'fd.': [30], u'ml2': [26, 70], u'pac': [81], u'arn': [35],\
                                    u'ngr': [37], u'r h': [22, 66], u'2TF': [54], u'har': [34], u'is ': [2, 5], u'tml': [25, 69], u'F c': [56],\
                                    u'ass': [60], u'tri': [49], u'g2T': [53], u'his': [1], u'kag': [84], u'Bas': [44], u'2ve': [72], u'tfd': [29],\
                                    u'gra': [38], u'rng': [36], u'ors': [77], u'it ': [12], u'odu': [90], u'mod': [89], u' pa': [80], u'ect': [74],\
                                    u'ule': [92], u'Thi': [0], u's.B': [42], u' te': [14], u'.Ba': [43], u'nit': [11], u'las': [59], u' a ': [7],\
                                    u'rin': [50], u'seS': [46], u'cka': [83], u' cl': [57], u'd.c': [31], u'dul': [91], u'ack': [82], u'age': [85],\
                                    u' ht': [23, 67], u'ms.': [41], u'/mo': [88], u'ng2': [52], u'ss ': [61], u'uni': [10], u'cto': [75], u'vec': [73],\
                                    u' fo': [19, 63], u'a u': [8]}    
        self.expected_ngrams_freq_lowercase = {u'le ': [93], u's i': [3], u't t': [13], u's.b': [42], u'f c': [56], u's a': [6], u'htm': [24, 68], u'ram': [39],\
                                               u'rs ': [78], u'tf ': [55], u's f': [62], u'.ch': [32], u't f': [18], u' un': [9], u'2tf': [28, 54], u'.ba': [43],\
                                               u'l2t': [27], u'l2v': [71], u's p': [79], u'ses': [46], u'mod': [89], u'tes': [15], u'ge/': [86], u'ams': [40],\
                                               u'or ': [21, 65], u'cha': [33], u'est': [16, 47], u'st ': [17], u'for': [20, 64], u'tor': [76], u' is': [4],\
                                               u'ing': [51], u'cla': [58], u'e/m': [87], u'fd.': [30], u'ml2': [26, 70], u'pac': [81], u'arn': [35], u'ngr': [37],\
                                               u'r h': [22, 66], u'ule': [92], u'har': [34], u'is ': [2, 5], u'tml': [25, 69], u'ng2': [52], u' cl': [57],\
                                               u'ass': [60], u'tri': [49], u'his': [1], u'kag': [84], u'str': [48], u'2ve': [72], u'tfd': [29], u'gra': [38],\
                                               u'rng': [36], u'ors': [77], u'it ': [12], u'odu': [90], u' pa': [80], u'ect': [74], u'ase': [45], u'dul': [91],\
                                               u' te': [14], u'nit': [11], u'las': [59], u' a ': [7], u'rin': [50], u'g2t': [53], u'cka': [83], u'bas': [44],\
                                               u'd.c': [31], u'ack': [82], u'age': [85], u' ht': [23, 67], u'ms.': [41], u'/mo': [88], u'thi': [0], u'ss ': [61],\
                                               u'uni': [10], u'cto': [75], u'vec': [73], u' fo': [19, 63], u'a u': [8]}
        self.pathto_htmls = "../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../unit_test_data/txt/test_01.txt" ]
        self.pckld_file_pos_list = "../../unit_test_data/pickled/pckled_pos_lst.pkl"
                         
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
        #Be carefull html_ngrams_tp is a list of Dictionaries where each Dictionary has keys a terms an values List of Term's Positions
        for vals, expected_vals in zip(html_ngrams_tp[0].values(), pos_lst):
            self.assertEqual(vals, expected_vals)

    def test_html2tp_from_paths(self):
        pos_lst_f = open(self.pckld_file_pos_list, "r")
        #load previously pickled list of Terms Positions pickle.dump(vals_ll, fl)
        pos_lst = pickle.load(pos_lst_f)
        html_ngrams_tp_l = self.html2tp.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict')
        #Be carefull html_ngrams_tp is a list of Dictionaries where each Dictionary has keys a terms an values List of Term's Positions
        #html_ngrams_tp_l[0][  0 <-- ] contains the filenames       
        for vals, expected_vals in zip(html_ngrams_tp_l[0][1].values(), pos_lst):
            self.assertEqual(vals, expected_vals)
    
    #### DEPRICATED ####      
    #def test_html2tp_from_paths_low_mem(self):
    #    pos_lst_f = open(self.pckld_file_pos_list, "r")
    #    #load previously pickled list of Terms Positions pickle.dump(vals_ll, fl)
    #    pos_lst = pickle.load(pos_lst_f)
    #    html_ngrams_tp_l = self.html2tp.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
    #    #Be carefull html_ngrams_tp is a list of Dictionaries where each Dictionary has keys a terms an values List of Term's Positions
    #    #html_ngrams_tp_l[0][  0 <-- ] contains the filenames       
    #    for vals, expected_vals in zip(html_ngrams_tp_l[0][1].values(), pos_lst):
    #        self.assertEqual(vals, expected_vals)

    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2NgramList__3grams) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TFTP__3grams) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF__3grams) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TP__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        