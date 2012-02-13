#
#    Unit Test for html2vect.base.vectortypes.string2tpl
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
from html2vect.base.vectortypes.string2tpl import BaseString2TPL
from html2vect.base.termstypes.cngrams import String2CNGramsList
from html2vect.base.termstypes.words import String2WordList
import numpy as np


class Test_BaseString2TPL(unittest.TestCase):
    
    def setUp(self):
        
        self.bs2tpl_3grams = BaseString2TPL( termstype=String2CNGramsList(n=3) )
        self.bs2tpl_words = BaseString2TPL( termstype=String2WordList() )
        
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
                
        self.expected_ngrams_pos = {'s i': [4], 't t': [14], 'ase': [46], 's a': [7], 'htm': [25, 69], 'ram': [40], 'rs ': [79],\
                                    'TF ': [56], 's f': [63], '.ch': [33], 't f': [19], ' un': [10], '2tf': [29], 'l2t': [28],\
                                    'l2v': [72], 's p': [80], 'eSt': [48], 'tes': [16], 'ge/': [87], 'ams': [41], 'or ': [22, 66],\
                                    'cha': [34], 'est': [17], 'st ': [18], 'Str': [49], 'for': [21, 65], 'tor': [77], ' is': [5],\
                                    'ing': [52], 'cla': [59], 'e/m': [88], 'fd.': [31], 'ml2': [27, 71], 'pac': [82], 'arn': [36],\
                                    'ngr': [38], 'r h': [23, 67], '2TF': [55], 'har': [35], 'is ': [3, 6], 'tml': [26, 70], 'F c': [57],\
                                    'ass': [61], 'tri': [50], 'g2T': [54], 'his': [2], 'kag': [85], 'Bas': [45], '2ve': [73], 'tfd': [30],\
                                    'gra': [39], 'rng': [37], 'ors': [78], 'it ': [13], 'odu': [91], 'mod': [90], ' pa': [81], 'ect': [75],\
                                    'ule': [93], 'Thi': [1], 's.B': [43], ' te': [15], '.Ba': [44], 'nit': [12], 'las': [60], ' a ': [8],\
                                    'rin': [51], 'seS': [47], 'cka': [84], ' cl': [58], 'd.c': [32], 'dul': [92], 'ack': [83], 'age': [86],\
                                    ' ht': [24, 68], 'ms.': [42], '/mo': [89], 'ng2': [53], 'ss ': [62], 'uni': [11], 'cto': [76], 'vec': [74],\
                                    ' fo': [20, 64], 'a u': [9]}
        
        self.expected_words_pos = {'a': [3], 'for': [6, 9], 'This': [1], 'is': [2], 'html2vectors': [10], 'test': [5], 'package/module': [11],\
                                   'html2tfd.charngrams.BaseString2TF': [8], 'class': [7], 'unit': [4]}
        
        #Create expected Ngrams-Position Array
        ngrams_lst = [' a ', ' cl', ' fo', ' ht', ' is', ' pa', ' te', ' un', '.Ba', '.ch', '/mo', '2TF', '2tf', '2ve', 'Bas', 'F c',\
                      'Str', 'TF ', 'Thi', 'a u', 'ack', 'age', 'ams', 'arn', 'ase', 'ass', 'cha', 'cka', 'cla', 'cto', 'd.c', 'dul',\
                      'e/m', 'eSt', 'ect', 'est', 'fd.', 'for', 'g2T', 'ge/', 'gra', 'har', 'his', 'htm', 'ing', 'is ', 'it ', 'kag',\
                      'l2t', 'l2v', 'las', 'ml2', 'mod', 'ms.', 'ng2', 'ngr', 'nit', 'odu', 'or ', 'ors', 'pac', 'r h', 'ram', 'rin',\
                      'rng', 'rs ', 's a', 's f', 's i', 's p', 's.B', 'seS', 'ss ', 'st ', 't f', 't t', 'tes', 'tfd', 'tml', 'tor',\
                      'tri', 'ule', 'uni', 'vec']
        
        self.expected_ngrams_pos_arr = np.zeros(len(ngrams_lst) , dtype=np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))]) )
        self.expected_ngrams_pos_arr['terms'] = ngrams_lst
        
        ngrams_pos_arr_lst = [(np.array([8]),), (np.array([58]),), (np.array([20, 64]),), (np.array([24, 68]),), (np.array([5]),), (np.array([81]),),\
                              (np.array([15]),), (np.array([10]),), (np.array([44]),), (np.array([33]),), (np.array([89]),), (np.array([55]),),\
                              (np.array([29]),), (np.array([73]),), (np.array([45]),), (np.array([57]),), (np.array([49]),), (np.array([56]),),\
                              (np.array([1]),), (np.array([9]),), (np.array([83]),), (np.array([86]),), (np.array([41]),), (np.array([36]),),\
                              (np.array([46]),), (np.array([61]),), (np.array([34]),), (np.array([84]),), (np.array([59]),), (np.array([76]),),\
                              (np.array([32]),), (np.array([92]),), (np.array([88]),), (np.array([48]),), (np.array([75]),), (np.array([17]),),\
                              (np.array([31]),), (np.array([21, 65]),), (np.array([54]),), (np.array([87]),), (np.array([39]),), (np.array([35]),),\
                              (np.array([2]),), (np.array([25, 69]),), (np.array([52]),), (np.array([3, 6]),), (np.array([13]),), (np.array([85]),),\
                              (np.array([28]),), (np.array([72]),), (np.array([60]),), (np.array([27, 71]),), (np.array([90]),), (np.array([42]),),\
                              (np.array([53]),), (np.array([38]),), (np.array([12]),), (np.array([91]),), (np.array([22, 66]),), (np.array([78]),),\
                              (np.array([82]),), (np.array([23, 67]),), (np.array([40]),), (np.array([51]),), (np.array([37]),), (np.array([79]),),\
                              (np.array([7]),), (np.array([63]),), (np.array([4]),), (np.array([80]),), (np.array([43]),), (np.array([47]),),\
                              (np.array([62]),), (np.array([18]),), (np.array([19]),), (np.array([14]),), (np.array([16]),), (np.array([30]),),\
                              (np.array([26, 70]),), (np.array([77]),), (np.array([50]),), (np.array([93]),), (np.array([11]),), (np.array([74]),)]
         
        for i, pos_arr in enumerate(ngrams_pos_arr_lst):
            self.expected_ngrams_pos_arr['pos'][i][0:len(pos_arr[0])] = pos_arr[0]
        
        #Create expected Words-Position Array       
        words_lst = ['This', 'a', 'class', 'for', 'html2tfd.charngrams.BaseString2TF', 'html2vectors', 'is', 'package/module', 'test', 'unit']
        self.exp_words_pos_arr = np.zeros(len(words_lst) , dtype=np.dtype( [('terms', 'S128'), ('pos', 'uint16', (200,))]) )
        self.exp_words_pos_arr['terms'] = words_lst
        
        words_pos_arr_lst = [(np.array([1]),), (np.array([3]),), (np.array([7]),), (np.array([6, 9]),), (np.array([8]),), (np.array([10]),),\
                              (np.array([2]),), (np.array([11]),), (np.array([5]),), (np.array([4]),)]
         
        for i, pos_arr in enumerate(words_pos_arr_lst):
            #print self.exp_words_pos_arr['terms'][i]
            self.exp_words_pos_arr['pos'][i][0:len(pos_arr[0])] = pos_arr[0]
        

    def test_tpl_dict_3grams(self):
        ngrams_pos_dict = self.bs2tpl_3grams.tpl_dict( self.txt_sample )
        self.assertEqual(ngrams_pos_dict, self.expected_ngrams_pos)
    
        
    def test_tpl_array_3grams(self):
        ngrams_pos_arr = self.bs2tpl_3grams.tpl_array( self.txt_sample, ndtype=np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))] ) )
        for val, exp_val in zip(ngrams_pos_arr, self.expected_ngrams_pos_arr):
            self.assertEqual(val[0], exp_val[0])
            for lst, exp_lst in zip(val[1], exp_val[1]):
                self.assertEqual(lst, exp_lst)
    
    
    def test_tpl_dict_words(self):
        words_pos_dict = self.bs2tpl_words.tpl_dict( self.txt_sample )
        self.assertEqual(words_pos_dict, self.expected_words_pos)
        
        
    def test_tpl_array_words(self):
        words_pos_arr = self.bs2tpl_words.tpl_array( self.txt_sample, ndtype=np.dtype( [('terms', 'S128'), ('pos', 'uint16', (200,))] ) )   
        for val, exp_val in zip(words_pos_arr, self.exp_words_pos_arr):
            self.assertEqual(val[0], exp_val[0])
            for lst, exp_lst in zip(val[1], exp_val[1]):
                self.assertEqual(lst, exp_lst)
  
          
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TPL) )
unittest.TextTestRunner(verbosity=2).run(suite)    
