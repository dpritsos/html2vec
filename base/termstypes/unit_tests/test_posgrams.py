#
#    Unit Test for html2vect.base.termstypes.cngrams
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

import sys
sys.path.append('../../../../')

import unittest
from html2vec.base.termstypes.posgrams import String2POSGramsList


if __name__ == '__main__':

    st = String2POSGramsList()
    print st.terms_lst(
        "Cento Vergilianus de laudibus Christi is a fourth-century Latin poem arranged by Faltonia Betitia Proba after her conversion to Christianity. A cento rearranges verses written by other poets; this one repurposes Virgil to tell stories from the Old and New Testament of the Christian Bible. Much of the work focuses on the story of Jesus Christ. The poem was widely circulated, eventually being used in schools to teach the tenets of Christianity, often alongside Augustine of Hippo's De Doctrina Christiana. Although the poem was popular, critical reception was mixed. A pseudonymous work purportedly by Pope Gelasius I disparaged the poem, deeming it apocryphal, and St. Jerome may have written disapprovingly of it, and of Proba. Other thinkers like Isidore of Seville, Petrarch, and Giovanni Boccaccio wrote highly of her, and many praised her ingenuity. During the 19th and 20th centuries the poem was considered a work of poor quality, but recent scholars have held it in higher regard."
    )

"""
class Test_String2CNGramsList__3grams(unittest.TestCase):


    def setUp(self):
        self.str2cng = String2CNGramsList(n=1)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_terms_lst = [
            'Thi', 'his', 'is ', 's i', ' is', 'is ', 's a', ' a ', 'a u', ' un', 'uni', 'nit', 'it ', 't t',\
            ' te', 'tes', 'est', 'st ', 't f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2t',\
            '2tf', 'tfd', 'fd.', 'd.c', '.ch', 'cha', 'har', 'arn', 'rng', 'ngr', 'gra', 'ram', 'ams', 'ms.',\
            's.B', '.Ba', 'Bas', 'ase', 'seS', 'eSt', 'Str', 'tri', 'rin', 'ing', 'ng2', 'g2T', '2TF', 'TF ',\
            'F c', ' cl', 'cla', 'las', 'ass', 'ss ', 's f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml',\
            'ml2', 'l2v', '2ve', 'vec', 'ect', 'cto', 'tor', 'ors', 'rs ', 's p', ' pa', 'pac', 'ack', 'cka',\
            'kag', 'age', 'ge/', 'e/m', '/mo', 'mod', 'odu', 'dul', 'ule'
        ]


    def test_terms_lst(self):
        self.str2cng.N = 3
        terms_l = self.str2cng.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2CNGramsList__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)
"""
