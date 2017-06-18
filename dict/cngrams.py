#
#    Module: Character NGrams - from html row text/files to native python character...
#            ...ngrams TF dictionaries
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.dict.cngrams: submodule of `html2vect` module defines the
    classes: HtmlTF(), HtmlTPL() """

from ..base.html2tf import BaseHtml2TF
from ..base.termstypes.cngrams import String2CNGramsList


# ################################ NEEDS REFACTORING ####################################

class Html2TF(BaseHtml2TF):

    # Define the TermsType to be produced from this class
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initialise BaseHtml2TF Class
        super(Html2TF, self).__init__(*args, **kwrgs)

    def yield_(self, xhtml_str, tid_vocabulary):
        return self.tl2tf.trms2tf_dict(
            Html2TF.s2ngl.terms_lst(
                self.html_attrib(xhtml_str)
            ),
            tid_vocabulary
        )

    def from_src(self, xhtml_str, tid_vocabulary=None):

        # Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary is None:
            tid_vocabulary = self.build_vocabulary()

        return (self.yield_(xhtml_str, tid_vocabulary), tid_vocabulary)

    def from_files(self, xhtml_file_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):

        # Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary is None:
            tid_vocabulary = self.build_vocabulary()

        tfd_l = [
            self.yield_(html_str, id_vocabulary)
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling)
        ]

        return (tfd_l, tid_vocabulary)

    def from_paths(self, basepath, filepath_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):

        # Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary is None:
            tid_vocabulary = self.build_vocabulary()

        flist = self.file_list_frmpaths(basepath, filepath_l)
        wpg_txt_ll = list()

        for filename in flist:
            xhtml_src = self.load_files(filename, tid_vocabulary, encoding, error_handling)
            wpg_tfd_ll.append([filename, self.yield_(xhtml_src, tid_vocabulary)])

        return (wpg_tfd_ll, tid_vocabulary)


# Deleted from the previous version now is need to be re-written
class Html2TPL(object):

    def __init__(self):
        pass
