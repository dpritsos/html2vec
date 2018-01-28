#
#    Unit Test for html2vect.tables.cngrams
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#


import sys
sys.path.append('../../../')

import unittest

import numpy as np
import scipy.sparse as ssp
import tables as tb
#from html2vect.string.attrib_text import HtmlFullText
#self.htmltext = HtmlFullText(valid_html=True)

# from html2vect.base.vectortypes.termslist2tf import trms2tf_dict, trms2tf_narray
# from html2vect.base.vectortypes.termslist2tf import trms2f_sparse, trms2f_narray
from html2vec.tables.posgrams import Html2TF


if __name__ == '__main__':

    tb_fname = "../../unit_test_data/hd5files/CorpusTable.h5"
    xhtml_file_l = ["../../unit_test_data/html/test_01.html"]

    h2tf_pos = Html2TF(
        'english-bidirectional-distsim.tagger', html_attrib=['text'],
        str_case='lower', valid_html=False
    )

    #Create the h5file and a test Group for the puropse of this Unit test
    #h5file = tb.open_file(self.tables_filename, 'w')

    f_earray_extended = h2tf_pos.from_files(
        xhtml_file_l, tb_fname, tid_vocabulary=None,
        norm_func=None, encoding='utf8', error_handling='strict'
    )

    print f_earray_extended[0].read()


    """Cento Vergilianus de laudibus Christi is a fourth-century Latin poem arranged by Faltonia Betitia Proba after her conversion to Christianity. A cento rearranges verses written by other poets; this one repurposes Virgil to tell stories from the Old and New Testament of the Christian Bible. Much of the work focuses on the story of Jesus Christ. The poem was widely circulated, eventually being used in schools to teach the tenets of Christianity, often alongside Augustine of Hippo's De Doctrina Christiana. Although the poem was popular, critical reception was mixed. A pseudonymous work purportedly by Pope Gelasius I disparaged the poem, deeming it apocryphal, and St. Jerome may have written disapprovingly of it, and of Proba. Other thinkers like Isidore of Seville, Petrarch, and Giovanni Boccaccio wrote highly of her, and many praised her ingenuity. During the 19th and 20th centuries the poem was considered a work of poor quality, but recent scholars have held it in higher regard."""





"""
class Test_Html2TF__3grams(unittest.TestCase):

    def setUp(self):

        #Setting Character n-grams size.
        cngrams_size = 1

        #Instantiating Html2TF object with several different arguments.
        self.h2tf_c3grams = Html2TF(cngrams_size, html_attrib='text', lowercase=True, valid_html=False)

        #Defining the data files and paths required for this unit test.
        self.pathto_htmls = "../../../unit_test_data/html/"
        self.tables_filename = "../../../unit_test_data/hd5files/CorpusTable.h5"
        self.xhtml_file_l = [ "../../../unit_test_data/html/test_01.html" ]
        self.txt_file_l = [ "../../../unit_test_data/txt/test_01.txt" ]

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
                                                   ('tor', 1.0), ('tri', 1.0), ('ule', 1.0), ('uni', 1), ('vec', 1)],\
                                                   np.dtype([('terms', 'S3'), ('freq', 'float32')]))

        def test_html2tf_from_src(self):
            #Create the h5file and a test Group for the puropse of this Unit test
            h5file = tb.openFile(self.tables_filename, 'w')
            group_h5 = h5file.createGroup(h5file.root, "testgroup")

            self.h2tf_c3grams
            #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method
            #which is called again and again for each of the test_ methods into this Unit-test Class
            tb_trms_frq_arr = self.html2tf.from_src(h5file, group_h5, self.html_sample, tbname="tbarray1")

            for val, exp_val in zip(tb_trms_frq_arr.read(), self.expected_ngrams_freq_arr):
                self.assertEqual(val, exp_val)

            #Close the file for the next Loop of Unit-Test
            h5file.close()


        def test_html2tf_from_src_lowercase(self):
            #Create the h5file and a test Group for the puropse of this Unit test
            h5file = tb.openFile(self.tables_filename, 'w')
            group_h5 = h5file.createGroup(h5file.root, "testgroup")

            #NOTE: the above comands should run into this fucntion (ie on the fly) and not in the setUP() method
            #which is called again and again for each of the test_ methods into this Unit-test Class
            tb_trms_frq_arr = self.html2tf_lowercase.from_src(h5file, group_h5, self.html_sample, tbname="tbarray1")

            for val, exp_val in zip(tb_trms_frq_arr.read(), self.expected_ngrams_freq_arr_lowercase):
                self.assertEqual(val, exp_val)

            #Close the file for the next Loop of Unit-Test
            h5file.close()



    def test_html2tf_from_files(self):

        #Create the h5file and a test Group for the puropse of this Unit test
        #h5file = tb.open_file(self.tables_filename, 'w')

        f_earray_extended = self.h2tf_c3grams.from_files(self.xhtml_file_l, self.tables_filename, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict')

        #f_erray is a tuple where:
        #   f_earray_extended[0] == term's frequiencies expandable_array of pytables.
        #   f_earray_extended[1] == the HD5 Files given as input.
        #   f_earray_extended[2] == the terms-index (tid_dictionary) dictionary created from the input in case of tid_dictionary argument is equal to None.


        print f_earray_extended[0].read()


        #ng_num_expected = len(html_text[0]) - self.n + 1
        #ng_num_real = 0
        #test_table = h5file.getNode(tb_trms_frq_arrz_group, 'test_01_html')
        #g_num_real += np.sum( test_table.read()['freq'] )
        #self.assertEqual(ng_num_real, ng_num_expected)
        ##
        #self.assertEqual(test_table._v_attrs.terms_num, ng_num_expected)

        #Close the file for the next Loop of Unit-Test
        h5file.close()


suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TF__3grams) )
#suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_Html2TP__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)
"""
