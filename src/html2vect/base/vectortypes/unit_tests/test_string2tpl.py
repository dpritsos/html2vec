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
        
        self.expected_words_pos = {'a': [3], 'for': [6, 8], 'This': [1], 'is': [2], 'html2vectors': [9], 'test': [5], 'package/module': [10],\
                                   'html2tfd.charngrams.BaseString2TF': [0], 'class': [7], 'unit': [4]}
        
        #Create expected Ngrams-Position Array
        ngrams_lst = [' a ', ' cl', ' fo', ' ht', ' is', ' pa', ' te', ' un', '.Ba', '.ch', '/mo', '2TF', '2tf', '2ve', 'Bas', 'F c',\
                      'Str', 'TF ', 'Thi', 'a u', 'ack', 'age', 'ams', 'arn', 'ase', 'ass', 'cha', 'cka', 'cla', 'cto', 'd.c', 'dul',\
                      'e/m', 'eSt', 'ect', 'est', 'fd.', 'for', 'g2T', 'ge/', 'gra', 'har', 'his', 'htm', 'ing', 'is ', 'it ', 'kag',\
                      'l2t', 'l2v', 'las', 'ml2', 'mod', 'ms.', 'ng2', 'ngr', 'nit', 'odu', 'or ', 'ors', 'pac', 'r h', 'ram', 'rin',\
                      'rng', 'rs ', 's a', 's f', 's i', 's p', 's.B', 'seS', 'ss ', 'st ', 't f', 't t', 'tes', 'tfd', 'tml', 'tor',\
                      'tri', 'ule', 'uni', 'vec']
        
        self.expected_ngrams_pos_arr = np.zeros(len(ngrams_lst) , dtype=np.dtype( [('terms', 'S128'), ('pos', 'uint16', (200,))]) )
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
            
        ('This', [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('a', [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('class', [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('for', [7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('html2tfd.charngrams.BaseString2TF', [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('html2vectors', [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('is', [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('package/module', [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('test', [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 ('unit', [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        #Create expected Words-Position Array
        #words_lst = ['This', 'a', 'class', 'for', 'html2tfd.charngrams.BaseString2TF',  ]
        
        #self.expected_ngrams_pos_arr = np.zeros(len(ngrams_lst) , dtype=np.dtype( [('terms', 'S3'), ('pos', 'uint16', (200,))]) )
        #self.expected_ngrams_pos_arr['terms'] = ngrams_lst
        
        #ngrams_pos_arr_lst = [(np.array([7]),), (np.array([57]),), (np.array([19, 63]),), (np.array([23, 67]),), (np.array([4]),), (np.array([80]),),\
        #                      (np.array([14]),), (np.array([9]),), (np.array([43]),), (np.array([32]),), (np.array([88]),), (np.array([54]),), (np.array([28]),),\
        #                      (np.array([72]),), (np.array([44]),), (np.array([56]),), (np.array([48]),), (np.array([55]),), (np.array([0]),), (np.array([8]),),\
        #                      (np.array([82]),), (np.array([85]),), (np.array([40]),), (np.array([35]),), (np.array([45]),), (np.array([60]),), (np.array([33]),),\
        #                      (np.array([83]),), (np.array([58]),), (np.array([75]),), (np.array([31]),), (np.array([91]),), (np.array([87]),)]
         
        #for i, pos_arr in enumerate(ngrams_pos_arr_lst):
        #    self.expected_ngrams_pos_arr['pos'][i][0:len(pos_arr[0])] = pos_arr[0] + 1
        


#################################### ERROR ERROR ERROR IN POSISTION RETURNED CHECK AGAIN THE LIST RETURNED INITIALY! ################################




                           
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
        print words_pos_arr    
        for val, exp_val in zip(words_pos_arr, self.expected_ngrams_pos_arr):
            self.assertEqual(val[0], exp_val[0])
            for lst, exp_lst in zip(val[1], exp_val[1]):
                self.assertEqual(lst, exp_lst)
    
        
    
    
    
    #def test_tf_array_words(self):
    #    word_freq_arr = self.bs2tf_words.tf_narray( self.txt_sample )
    #    for val, exp_val in zip(word_freq_arr, self.expected_words_freq_arr):
    #        self.assertEqual(val, exp_val)    
        
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TPL) )
unittest.TextTestRunner(verbosity=2).run(suite)    
