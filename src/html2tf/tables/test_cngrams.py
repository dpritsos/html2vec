""" Unit Test for charngrams.py """

import unittest
import cngrams
import numpy as np
import tbtools
import htmlattrib.attrib as htmlre
import pickle
import tables as tb

class Test_BaseString2TFTP__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = cngrams.BaseString2TFTP(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_ngrams_freq_arr = np.array( [(' a ', 1.0), (' cl', 1.0), (' fo', 2.0), (' ht', 2.0), (' is', 1.0),\
                                                   (' pa', 1.0), (' te', 1.0), (' un', 1.0), ('.Ba', 1.0), ('.ch', 1.0),\
                                                   ('/mo', 1.0), ('2TF', 1.0), ('2tf', 1.0), ('2ve', 1.0), ('Bas', 1.0),\
                                                   ('F c', 1.0), ('Str', 1.0), ('TF ', 1.0), ('Thi', 1.0), ('a u', 1.0),\
                                                   ('ack', 1.0), ('age', 1.0), ('ams', 1.0), ('arn', 1.0), ('ase', 1.0),\
                                                   ('ass', 1.0), ('cha', 1.0), ('cka', 1.0), ('cla', 1.0), ('cto', 1.0),\
                                                   ('d.c', 1.0), ('dul', 1.0), ('e/m', 1.0), ('eSt', 1.0), ('ect', 1.0),\
                                                   ('est', 1.0), ('fd.', 1.0), ('for', 2.0), ('g2T', 1.0), ('ge/', 1.0),\
                                                   ('gra', 1.0), ('har', 1.0), ('his', 1.0), ('htm', 2.0), ('ing', 1.0),\
                                                   ('is ', 2.0), ('it ', 1.0), ('kag', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
                                                   ('las', 1.0), ('ml2', 2.0), ('mod', 1.0), ('ms.', 1.0), ('ng2', 1.0),\
                                                   ('ngr', 1.0), ('nit', 1.0), ('odu', 1.0), ('or ', 2.0), ('ors', 1.0),\
                                                   ('pac', 1.0), ('r h', 2.0), ('ram', 1.0), ('rin', 1.0), ('rng', 1.0),\
                                                   ('rs ', 1.0), ('s a', 1.0), ('s f', 1.0), ('s i', 1.0), ('s p', 1.0),\
                                                   ('s.B', 1.0), ('seS', 1.0), ('ss ', 1.0), ('st ', 1.0), ('t f', 1.0),\
                                                   ('t t', 1.0), ('tes', 1.0), ('tfd', 1.0), ('tml', 2.0), ('tor', 1.0),\
                                                   ('tri', 1.0), ('ule', 1.0), ('uni', 1), ('vec', 1)], dtype=tbtools.default_TF_3grams_dtype)                                            
        #Create expected Ngrams-Position Array
        ngrams_lst = [' a ', ' cl', ' fo', ' ht', ' is', ' pa', ' te', ' un', '.Ba', '.ch', '/mo', '2TF', '2tf', '2ve', 'Bas', 'F c',\
                      'Str', 'TF ', 'Thi', 'a u', 'ack', 'age', 'ams', 'arn', 'ase', 'ass', 'cha', 'cka', 'cla', 'cto', 'd.c', 'dul',\
                      'e/m', 'eSt', 'ect', 'est', 'fd.', 'for', 'g2T', 'ge/', 'gra', 'har', 'his', 'htm', 'ing', 'is ', 'it ', 'kag',\
                      'l2t', 'l2v', 'las', 'ml2', 'mod', 'ms.', 'ng2', 'ngr', 'nit', 'odu', 'or ', 'ors', 'pac', 'r h', 'ram', 'rin',\
                      'rng', 'rs ', 's a', 's f', 's i', 's p', 's.B', 'seS', 'ss ', 'st ', 't f', 't t', 'tes', 'tfd', 'tml', 'tor',\
                      'tri', 'ule', 'uni', 'vec']
        self.expected_ngrams_pos_arr = np.zeros(len(ngrams_lst) , dtype=tbtools.default_TP_3grams_dtype)
        self.expected_ngrams_pos_arr['terms'] = ngrams_lst
        ngrams_pos_arr_lst = [(np.array([7]),), (np.array([57]),), (np.array([19, 63]),), (np.array([23, 67]),), (np.array([4]),), (np.array([80]),),\
                              (np.array([14]),), (np.array([9]),), (np.array([43]),), (np.array([32]),), (np.array([88]),), (np.array([54]),), (np.array([28]),),\
                              (np.array([72]),), (np.array([44]),), (np.array([56]),), (np.array([48]),), (np.array([55]),), (np.array([0]),), (np.array([8]),),\
                              (np.array([82]),), (np.array([85]),), (np.array([40]),), (np.array([35]),), (np.array([45]),), (np.array([60]),), (np.array([33]),),\
                              (np.array([83]),), (np.array([58]),), (np.array([75]),), (np.array([31]),), (np.array([91]),), (np.array([87]),), (np.array([47]),),\
                              (np.array([74]),), (np.array([16]),), (np.array([30]),), (np.array([20, 64]),), (np.array([53]),), (np.array([86]),), (np.array([38]),),\
                              (np.array([34]),), (np.array([1]),), (np.array([24, 68]),), (np.array([51]),), (np.array([2, 5]),), (np.array([12]),), (np.array([84]),),\
                              (np.array([27]),), (np.array([71]),), (np.array([59]),), (np.array([26, 70]),), (np.array([89]),), (np.array([41]),), (np.array([52]),),\
                              (np.array([37]),), (np.array([11]),), (np.array([90]),), (np.array([21, 65]),), (np.array([77]),), (np.array([81]),), (np.array([22, 66]),),\
                              (np.array([39]),), (np.array([50]),), (np.array([36]),), (np.array([78]),), (np.array([6]),), (np.array([62]),), (np.array([3]),), (np.array([79]),),\
                              (np.array([42]),), (np.array([46]),), (np.array([61]),), (np.array([17]),), (np.array([18]),), (np.array([13]),), (np.array([15]),), (np.array([29]),),\
                              (np.array([25, 69]),), (np.array([76]),), (np.array([49]),), (np.array([92]),), (np.array([10]),), (np.array([73]),)] 
        for i, pos_arr in enumerate(ngrams_pos_arr_lst):
            self.expected_ngrams_pos_arr['pos'][i][0:len(pos_arr[0])] = pos_arr[0] + 1 
                           
    def test_basestring2tf_tf_array(self):
        ngrams_freq_arr = self.bs2tf.tf_array( self.txt_sample )
        for val, exp_val in zip(ngrams_freq_arr, self.expected_ngrams_freq_arr):
            self.assertEqual(val, exp_val)
        
    def test_basestring2tf_tpos_array(self):
        ngrams_pos_arr = self.bs2tf.tpos_array( self.txt_sample )
        for (val_term, val_pos_arr), (exp_val_term, exp_val_pos_arr) in zip(ngrams_pos_arr, self.expected_ngrams_pos_arr):
            self.assertEqual(val_term, exp_val_term)
            self.assertEqual(val_pos_arr[0], exp_val_pos_arr[0])
        

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
        self.expected_ngrams_freq_arr = np.array( [(' a ', 1.0), (' cl', 1.0), (' fo', 2.0), (' ht', 2.0), (' is', 1.0),\
                                                   (' pa', 1.0), (' te', 1.0), (' un', 1.0), ('.Ba', 1.0), ('.ch', 1.0),\
                                                   ('/mo', 1.0), ('2TF', 1.0), ('2tf', 1.0), ('2ve', 1.0), ('Bas', 1.0),\
                                                   ('F c', 1.0), ('Str', 1.0), ('TF ', 1.0), ('Thi', 1.0), ('a u', 1.0),\
                                                   ('ack', 1.0), ('age', 1.0), ('ams', 1.0), ('arn', 1.0), ('ase', 1.0),\
                                                   ('ass', 1.0), ('cha', 1.0), ('cka', 1.0), ('cla', 1.0), ('cto', 1.0),\
                                                   ('d.c', 1.0), ('dul', 1.0), ('e/m', 1.0), ('eSt', 1.0), ('ect', 1.0),\
                                                   ('est', 1.0), ('fd.', 1.0), ('for', 2.0), ('g2T', 1.0), ('ge/', 1.0),\
                                                   ('gra', 1.0), ('har', 1.0), ('his', 1.0), ('htm', 2.0), ('ing', 1.0),\
                                                   ('is ', 2.0), ('it ', 1.0), ('kag', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
                                                   ('las', 1.0), ('le ', 1.0), ('ml2', 2.0), ('mod', 1.0), ('ms.', 1.0),\
                                                   ('ng2', 1.0), ('ngr', 1.0), ('nit', 1.0), ('odu', 1.0), ('or ', 2.0),\
                                                   ('ors', 1.0), ('pac', 1.0), ('r h', 2.0), ('ram', 1.0), ('rin', 1.0),\
                                                   ('rng', 1.0), ('rs ', 1.0), ('s a', 1.0), ('s f', 1.0), ('s i', 1.0),\
                                                   ('s p', 1.0), ('s.B', 1.0), ('seS', 1.0), ('ss ', 1.0), ('st ', 1.0),\
                                                   ('t f', 1.0), ('t t', 1.0), ('tes', 1.0), ('tfd', 1.0), ('tml', 2.0),\
                                                   ('tor', 1.0), ('tri', 1.0), ('ule', 1.0), ('uni', 1), ('vec', 1)], dtype=tbtools.default_TF_3grams_dtype) 
        #NOTICE the 'le ':1 on the above dictionary which is extra 3gram compare toTest_BaseString2NgramList__3grams because of HTML clean-up process 
        self.expected_ngrams_freq_arr_lowercase = np.array( [(' a ', 1.0), (' cl', 1.0), (' fo', 2.0), (' ht', 2.0), (' is', 1.0),\
                                                             (' pa', 1.0), (' te', 1.0), (' un', 1.0), ('.ba', 1.0), ('.ch', 1.0),\
                                                             ('/mo', 1.0), ('2tf', 2.0), ('2ve', 1.0), ('a u', 1.0), ('ack', 1.0),\
                                                             ('age', 1.0), ('ams', 1.0), ('arn', 1.0), ('ase', 1.0), ('ass', 1.0),\
                                                             ('bas', 1.0), ('cha', 1.0), ('cka', 1.0), ('cla', 1.0), ('cto', 1.0),\
                                                             ('d.c', 1.0), ('dul', 1.0), ('e/m', 1.0), ('ect', 1.0), ('est', 2.0),\
                                                             ('f c', 1.0), ('fd.', 1.0), ('for', 2.0), ('g2t', 1.0), ('ge/', 1.0),\
                                                             ('gra', 1.0), ('har', 1.0), ('his', 1.0), ('htm', 2.0), ('ing', 1.0),\
                                                             ('is ', 2.0), ('it ', 1.0), ('kag', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
                                                             ('las', 1.0), ('le ', 1.0), ('ml2', 2.0), ('mod', 1.0), ('ms.', 1.0),\
                                                             ('ng2', 1.0), ('ngr', 1.0), ('nit', 1.0), ('odu', 1.0), ('or ', 2.0),\
                                                             ('ors', 1.0), ('pac', 1.0), ('r h', 2.0), ('ram', 1.0), ('rin', 1.0),\
                                                             ('rng', 1.0), ('rs ', 1.0), ('s a', 1.0), ('s f', 1.0), ('s i', 1.0),\
                                                             ('s p', 1.0), ('s.b', 1.0), ('ses', 1.0), ('ss ', 1.0), ('st ', 1.0),\
                                                             ('str', 1.0), ('t f', 1.0), ('t t', 1.0), ('tes', 1.0), ('tf ', 1.0),\
                                                             ('tfd', 1.0), ('thi', 1.0), ('tml', 2.0), ('tor', 1.0), ('tri', 1.0),\
                                                             ('ule', 1.0), ('uni', 1.0), ('vec', 1.0)], dtype=tbtools.default_TF_3grams_dtype)
        self.tables_filename="../../unit_test_data/hd5files/CorpusTable.h5"
        self.pathto_htmls = "../../unit_test_data/html/"
        self.xhtml_file_l = [ "../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../unit_test_data/txt/test_01.txt" ]
        
                         
    def test_html2tf_from_src(self):
        #html_ngrams = self.html2tf.from_src( self.html_sample )
        #self.assertEqual(html_ngrams, self.expected_ngrams_freq)
        pass 
    
    def test_html2tf_from_src_lowercase(self):
        #html_ngrams = self.html2tf_lowercase.from_src( self.html_sample )
        #self.assertEqual(html_ngrams, self.expected_ngrams_freq_lowercase)
        pass 
       
    def test_html2tf_from_files(self):
        #html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        #html_ngrams = self.html2tf.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        #ng_num_expected = len(html_text[0]) - self.n + 1
        #ng_num_real = 0
        #for nf in html_ngrams[0].values():
        #    ng_num_real += float(nf)
        #self.assertEqual(ng_num_real, ng_num_expected)
        pass

    def test_html2tf_from_paths(self):
        #html_text_l = self.htmltext.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        #html_ngrams_l = self.html2tf.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=False )
        ##ng_num_expected: contains the calculated expected number of N-grams given the text-string lenght
        #ng_num_expected = len(html_text_l[0][1]) - self.n + 1
        #ng_num_real = 0
        #for nf in html_ngrams_l[0][1].values():
        #    ng_num_real += float(nf)
        #self.assertEqual(ng_num_real, ng_num_expected)
        pass
    
    def test_html2tf_from_src2tbls(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, mode="w")
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method 
        #which is called again and again for each of the test_ methods into this Unit-test Class
        tb_trms_frq_arr = self.html2tf.from_src2tbls(h5file, group_h5, self.html_sample, tbname="tbarray1")
        for val, exp_val in zip(tb_trms_frq_arr.read(), self.expected_ngrams_freq_arr):
            self.assertEqual(val, exp_val)
        h5file.close()
    
    def test_html2tf_from_src2tbls_lowercase(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, mode="w")
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method 
        #which is called again and again for each of the test_ methods into this Unit-test Class
        tb_trms_frq_arr = self.html2tf_lowercase.from_src2tbls(h5file, group_h5, self.html_sample, tbname="tbarray1")
        for val, exp_val in zip(tb_trms_frq_arr.read(), self.expected_ngrams_freq_arr_lowercase):
            self.assertEqual(val, exp_val) 
        h5file.close()
       
    def test_html2tf_from_files2tbls(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, mode="w")
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        tb_trms_frq_arrz_group = self.html2tf.from_files2tbls(h5file, group_h5, self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        ng_num_expected = len(html_text[0]) - self.n + 1
        ng_num_real = 0
        test_table = h5file.getNode(tb_trms_frq_arrz_group, 'test_01_html') 
        ng_num_real += np.sum( test_table.read()['freq'] )        
        self.assertEqual(ng_num_real, ng_num_expected)
        self.assertEqual(test_table._v_attrs.filepath, self.xhtml_file_l[0]) 
        self.assertEqual(test_table._v_attrs.terms_num, ng_num_expected)
        h5file.close()
        
    def test_html2tf_from_paths2tbls(self):
        #Create the h5file and a test Group for the puropse of this Unit test
        h5file = tb.openFile(self.tables_filename, mode="w")
        group_h5 = h5file.createGroup(h5file.root, "testgroup")
        html_text = self.htmltext.from_files( self.xhtml_file_l, encoding='utf8', error_handling='strict' )
        tb_trms_frq_arrz_group = self.html2tf.from_paths2tbls(h5file, group_h5, 'GenrePageListTable', None, self.pathto_htmls, encoding='utf8', error_handling='strict' )
        #Assert for the Filename-List returned
        ### THIS IS A COMPLICTED STRUCTURE BE AWARE --> tb_trms_frq_arrz_group[1].read()['wpg_name']
        self.assertEqual(tb_trms_frq_arrz_group[1].read()['wpg_name'], ['../../unit_test_data/html/test_01.html'])
        #Assert for the amount of Ngrams greated
        ng_num_expected = len(html_text[0]) - self.n + 1
        ng_num_real = 0
        test_table = h5file.getNode(tb_trms_frq_arrz_group[0], 'test_01_html') 
        ng_num_real += np.sum( test_table.read()['freq'] )        
        self.assertEqual(ng_num_real, ng_num_expected)
        h5file.close()

"""           
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
        html_ngrams_tp_l = self.html2tp.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=False )
        #Be carefull html_ngrams_tp is a list of Dictionaries where each Dictionary has keys a terms an values List of Term's Positions
        #html_ngrams_tp_l[0][  0 <-- ] contains the filenames       
        for vals, expected_vals in zip(html_ngrams_tp_l[0][1].values(), pos_lst):
            self.assertEqual(vals, expected_vals)
           
    def test_html2tp_from_paths_low_mem(self):
        pos_lst_f = open(self.pckld_file_pos_list, "r")
        #load previously pickled list of Terms Positions pickle.dump(vals_ll, fl)
        pos_lst = pickle.load(pos_lst_f)
        html_ngrams_tp_l = self.html2tp.from_paths( None, self.pathto_htmls, encoding='utf8', error_handling='strict', low_mem=True )
        #Be carefull html_ngrams_tp is a list of Dictionaries where each Dictionary has keys a terms an values List of Term's Positions
        #html_ngrams_tp_l[0][  0 <-- ] contains the filenames       
        for vals, expected_vals in zip(html_ngrams_tp_l[0][1].values(), pos_lst):
            self.assertEqual(vals, expected_vals)
"""
    
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TFTP__3grams) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF__3grams) )
#suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TP__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        