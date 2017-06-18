#
#    Module: LowBOW (Local Weighted Bag of Words) - from html row text/files to scipy.sparse.csr_matrix LowBOW
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.sparse.lowbow: submodule of `html2vect` module defines the classes: Html2LBN(), Html2LBW()"""

from ..base.html2tf import BaseHtml2TF
from ..base.vectortypes.string2lowbow import BaseString2LB
from ..base.termstypes.cngrams import String2CNGramsList

import scipy.sparse as ssp
import numpy as np
from scipy import stats
import string



class Html2TLoW(BaseHtml2TF):

    #Define the TermsType to be produced from this class
    s2ngl = String2CNGramsList()


    def __init__(self, n, attrib, lowercase, valid_html, smoothing_kernel=stats.norm, norm_func=None):

        #Initialise BaseHtml2TF Class
        super(Html2TLoW, self).__init__(n, attrib, lowercase, valid_html)

        #String to Lowbow Class using String to Character N-Grams Class as argument
        self.s2lb = BaseString2LB( self.__class__.s2ngl, smoothing_kernel, norm_func)


    def yield_(self, xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling):

        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            tid_dictionary = self.__build_vocabulery(xhtml_file_l, encoding, error_handling)

        print "Creating LowBOWs"
        #Create the LowBow Sparse Matrix for the whole corpus
        lowbow_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            lowbow_lst.append( self.s2lb.lowbow( self.html_attrib( html_str ), smth_pos_l, smth_sigma, tid_dictionary) )

        #Pack it as a sparse vstack and return it
        smth_copus_mtrx = ssp.vstack( lowbow_lst )
        return ( ssp.csr_matrix(smth_copus_mtrx, shape=smth_copus_mtrx.shape, dtype=np.float), tid_dictionary )


    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")


    def from_files(self, xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary=None, encoding='utf8', error_handling='strict'):
        return self.yield_(xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling)


    def from_paths(self, basepath, filepath_l, smth_pos_l, smth_sigma, tid_dictionary=None, encoding='utf8', error_handling='strict'):

        #Get the filenames located in the paths given
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)

        #Create the lowbow vectors sparse matrix for this files
        lowbow_matrix, tid_dict = self.from_files(xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling)

        #Return the lowbow matrix, the dictionary created and the xhtml_files_list
        return (lowbow_matrix, tid_dict, xhtml_file_l)



class Html2TLoW4SEG(Html2TLoW):

    def __init__(self, *args, **kwrgs):

        #Initialise Html2LBN Class
        Html2LBN.__init__(self, *args, **kwrgs)


    def yield_(self, xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling):

        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            print "Creating Dictionary"
            tf_d = dict()
            #Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_d = tfdtools.merge_tfds( tf_d, self.tf_dict( self.html_attrib( html_str ) ) )

            #Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = tfdtools.tf2tidx( tf_d )

        print "Creating LowBOWs"
        #Create the LowBow Sparse Matrix for the whole corpus
        lowbow_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            lowbow_lst.append( self.s2lb.lowbow4seg( self.html_attrib( html_str ), smth_pos_l, smth_sigma, tid_dictionary) )

        #Pack it as a sparse vstack and return it
        smth_copus_mtrx = ssp.vstack( lowbow_lst )
        return ( ssp.csr_matrix(smth_copus_mtrx, shape=smth_copus_mtrx.shape, dtype=np.float), tid_dictionary )
