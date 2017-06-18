#
#     Module: LowBOW (Local Weighted Bag of Words) - from html row text/files to scipy.sparse.csr_matrix LowBOW
#
#     Author: Dimitiros Pritsos
#
#     License: BSD Style
#
#     Last update: Please refer to the GIT tracking
#

""" html2vect.sparse.lowbow: submodule of `html2vect` module definesthe
    classes: Html2LBN(), Html2LBW()"""

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2lowbow import BaseString2LB
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.io.baseio import BaseIO
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.termstypes.words import String2WNGramsList
from ..tools import tfdtools

import scipy.sparse as ssp
import numpy as np
from scipy import stats
import string


class Html2LBC(BaseIO):

    def __init__(self, n, attrib, lowercase, valid_html,
                 smoothing_kernel=stats.norm, norm_func=None):

        # Initialise IO Class
        BaseIO.__init__(self)

        # HTML to attributes Class
        self.h2attr = BaseHTML2Attributes(valid_html)

        # String to Term Frequency Class using String to Character N-Grams Class as argument
        self.s2tf = BaseString2TF(String2CNGramsList(n))

        # String to Lowbow Class using String to Character N-Grams Class as argument
        self.s2lb = BaseString2LB(String2CNGramsList(n), smoothing_kernel, norm_func)

        if attrib == "text":
            self._attrib_ = self.h2attr.text
        elif attrib == "tags":
            self._attrib_ = self.s2tf.tags

        if lowercase:
            self._attrib_ = self._lower(self._attrib_)

    def _attrib(self, xhtml_file_l, smth_pos_l, smth_sigma,
                tid_dictionary, encoding, error_handling):

        # Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary is None:
            print "Creating Dictionary"
            tf_d = dict()
            # Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_d = tfdtools.merge_tfds(tf_d, self.s2tf.tf_dict(self._attrib_(html_str)))

            # Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = tfdtools.tf2tidx(tf_d)

        print "Creating LowBOWs"
        # Create the LowBow Sparse Matrix for the whole corpus
        lowbow_lst = list()
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                lowbow_lst.append(
                    self.s2lb.lowbow(
                        self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str)),
                        smth_pos_l, smth_sigma, tid_dictionary
                    )
                )

        # Pack it as a sparse vstack and return it
        smth_copus_mtrx = ssp.vstack(lowbow_lst)
        return (
            ssp.csr_matrix(smth_copus_mtrx, shape=smth_copus_mtrx.shape, dtype=np.float),
            tid_dictionary
        )

    def _lower(self, methd):

        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()

        return lowerCase

    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, smth_pos_l, smth_sigma,
                   tid_dictionary=None, encoding='utf8', error_handling='strict'):
        return self._attrib(
            xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling
        )

    def from_paths(self, basepath, filepath_l, smth_pos_l, smth_sigma,
                   tid_dictionary=None, encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)

        # Create the lowbow vectors sparse matrix for this files
        lowbow_matrix, tid_dict = self.from_files(
            xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling
        )

        # Return the lowbow matrix, the dictionary created and the xhtml_files_list
        return (lowbow_matrix, tid_dict, xhtml_file_l)


class Html2LBC4SEG(Html2LBN):

    def __init__(self, n, attrib, lowercase, valid_html,
                 smoothing_kernel=stats.norm, norm_func=None):

        # Initialise Html2LBN Class
        Html2LBN.__init__(self, n, attrib, lowercase, valid_html,
                          smoothing_kernel=stats.norm, norm_func=None)

    def _attrib(self, xhtml_file_l, smth_pos_l, smth_sigma,
                tid_dictionary, encoding, error_handling):

        # Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary issubclass None:
            print "Creating Dictionary"
            tf_d = dict()
            # Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_attrib in self.html_attrib_lst:
                for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                    tf_d = tfdtools.merge_tfds(
                        tf_d,
                        self.tf_dict(
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        )
                    )

            # Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = tfdtools.tf2tidx(tf_d)

        print "Creating LowBOWs"
        # Create the LowBow Sparse Matrix for the whole corpus
        lowbow_lst = list()
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                lowbow_lst.append(
                    self.s2lb.lowbow4seg(
                        self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str)),
                        smth_pos_l, smth_sigma, tid_dictionary))

        # Pack it as a sparse vstack and return it
        smth_copus_mtrx = ssp.vstack(lowbow_lst)
        return (
            ssp.csr_matrix(smth_copus_mtrx, shape=smth_copus_mtrx.shape, dtype=np.float32),
            tid_dictionary
        )


class Html2LBW(Html2LBN):

    def __init__(self, attrib, lowercase, valid_html, smoothing_kernel=stats.norm, norm_func=None):

        # Initialise Html2LBN Class
        Html2LBN.__init__(self, n, attrib, lowercase, valid_html)

        # String to Term Frequency Class using String to Character N-Grams Class as argument
        self.s2tf = BaseString2TF(String2WNGramsList(n))

        # String to Lowbow Class using String to Character N-Grams Class as argument
        self.s2lb = BaseString2LB(String2WNGramsList(n), smoothing_kernel, norm_func)
