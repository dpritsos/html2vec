#
#    Module: Character NGrams -TF - from html row text/files to scipy.sparse.csr_matrix Character NGrams-TF
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.sparse.cngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from ..base.html2tf import BaseHtml2TF
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.io.basefilehandlers import file_list_frmpaths

import scipy.sparse as ssp
import numpy as np
import gensim as gsm
from ..utils import tfdutils


class Html2TF(BaseHtml2TF):

    # Define the TermsType to be produced from this class
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class
        super(Html2TF, self).__init__(*args, **kwrgs)

    def yield_(self, xhtml_file_l, tid_vocabulary, norm_func, encoding, error_handling):

        # Create the Dictionary from the given corpus if not given form the use
        if tid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            tf_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            tid_vocabulary = tfdutils.tf2tidx(tf_vocabulary)

        print "Creating NGrams-TF (Narray)"

        # The Frequnecy List.
        fq_lst = list()

        # Creating the NGrams-TF Sparse Matrix for the whole corpus
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                fq_lst.append(
                    self.tl2tf.trms2f_narray(
                        self.__class__.s2ngl.terms_lst(
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        ),
                        tid_vocabulary, norm_func
                    )
                )

        # Packing it as a sparse vstack and return it.
        copus_fq_array = np.vstack(fq_lst)
        return np.array(copus_fq_array, dtype=np.float), tid_vocabulary

    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, tid_vocabulary=None,
                   norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(xhtml_file_l, tid_vocabulary, norm_func, encoding, error_handling)

    def from_paths(self, basepath, filepath_l, tid_vocabulary=None, norm_func=None,
                   encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        matrix, tid_dict = self.from_files(
            xhtml_file_l, tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, tid_dict, xhtml_file_l)


# To Be Written
class Html2TPL(object):

    def __init__(self):
        pass


class Html2LSI(BaseHtml2TF):

    # Define the TermsType to be produced from this class
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class
        super(Html2LSI, self).__init__(*args, **kwrgs)

    def yield_(self,
               xhtml_file_l, dims,
               tid_vocabulary, norm_func, encoding, error_handling):

        # Create the Dictionary from the given corpus if not given form the use
        if tid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            tf_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            tid_vocabulary = tfdutils.tf2tidx(tf_vocabulary)

        print "Creating NGrams-TF (Narray)"

        id2trm = dict(zip(tid_vocabulary.values(), tid_vocabulary.keys()))

        lsi_mdl = gsm.models.LsiModel(num_topics=dims, id2word=id2trm)

        # The Frequnecy List.
        fq_lst = list()

        # Creating the NGrams-TF Sparse Matrix for the whole corpus
        for html_attrib in self.html_attrib_lst:

            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):

                fq_lst.append(
                    self.tl2tf.trms2f_narray(
                        self.__class__.s2ngl.terms_lst(
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        ),
                        tid_vocabulary, norm_func
                    )
                )

        # Packing it as a sparse vstack and return it.
        fq_array = np.array(np.vstack(fq_lst), dtype=np.float)

        # Training/Extending the LSI model squentially.
        lsi_mdl.add_documents(
            gsm.matutils.Dense2Corpus(fq_array[:, :].T)  # SOS: should this be Traspose?
        )

        # Training/Extending the LSI model squentially.
        lsi_mdl.add_documents(
            gsm.matutils.Dense2Corpus(fq_array[:, :].T)  # SOS: should this be Traspose?
        )

        # Creating LSI narray of the Corpus Projection in LSI model.
        lsi_array = gsm.matutils.corpus2dense(
            lsi_mdl[gsm.matutils.Dense2Corpus(fq_array[:, :].T)],
            num_terms=dims
        ).T

        return (lsi_array, fq_array, tid_vocabulary)

    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, dims,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(xhtml_file_l, dims, tid_vocabulary, norm_func, encoding, error_handling)

    def from_paths(self, basepath, filepath_l, dims,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        lsi_array, fq_earray, tid_vocabulary = self.from_files(
            xhtml_file_l, dims, tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (lsi_array, fq_earray, tid_vocabulary)
