#
#     Module: html2terms.
#
#     Author: Dimitiros Pritsos.
#
#     License: BSD Style.
#
#     Last update: Please refer to the GIT tracking.
#

""" html2vect.base.html2terms: submodule of `html2vect` module defines the classes: BaseHtml2TF"""

import abc
import warnings
from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes import termslist2tf
from ..base.io.basefilehandlers import BaseFileHandler
from ..utils import tfdutils


class BaseHtml2TF(BaseFileHandler):
    __metaclass__ = abc.ABCMeta

    def __init__(self, n, html_attrib, str_case, valid_html):

        # Initializing BaseFileHandler Class.
        super(BaseHtml2TF, self).__init__()

        # HTML to attributes Class.
        self.h2attr = BaseHTML2Attributes(valid_html)

        # Initialized the TermsType to be produced from this class stored in as class attribute.
        self.__class__.s2ngl.N = n

        # String to Term Frequency Class using.
        self.tl2tf = termslist2tf

        # Converting the single sting to a sting list.
        if isinstance(html_attrib, str) or isinstance(html_attrib, list):
            self.html_attrib_lst = list(html_attrib)
        else:
            raise Exception(
                "Invalid HTML attribute argument: Only string or string list are valid options."
            )

        # Checking if the reqested HTML atrributes list is valid.
        if not set(self.html_attrib_lst) < set(dir(self.h2attr)):
            raise Exception(
                "Invalid HTML attribute: HTML attributes can be exacted are " +
                ", ".join([attr for attr in dir(self.h2attr) if attr[0] != '_'])
            )

        # Keeping the setting for string case, whether it will be Upper of Lower.
        self.str_case = str_case

    def _string_case(self, strg):
        return strg.__getattribute__(self.str_case)()

    def build_vocabulary(self, xhtml_file_l, encoding, error_handling):

        # The TF Dictionary.
        tf_vocabulary = dict()

        # Merge All Term-Frequency Dictionaries created by the Raw Texts for all...
        # ...HTML attributes requested.
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_vocabulary = tfdutils.merge_tfds(
                    tf_vocabulary,
                    self.tl2tf.trms2tf_dict(
                        self.__class__.s2ngl.terms_lst(
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        )
                    )
                )

        return tf_vocabulary

    def _build_vocabulary(self, *args, **kwrgs):

        # Warning that a Vocabulary will automatically be build..
        wrn = "Automated Vocabulary Building has been triggered:" +\
                " NONE tid_vocabulary has been given as argument"
        warnings.warn(wrn)

        # Build and return the Vocabulary.
        return self.build_vocabulary(*args, **kwrgs)

    @abc.abstractmethod
    def yield_(self, xhtml_str, tid_vocabulary):
        # The main method that will produce the Term-Frequency or Frequency Dictionaries/Lists.
        pass

    @abc.abstractmethod
    def from_src(self, xhtml_str, tid_vocabulary=None):
        pass

    @abc.abstractmethod
    def from_files(self, xhtml_file_l, tid_vocabulary=None,
                   encoding='utf8', error_handling='strict'):
        pass

    @abc.abstractmethod
    def from_paths(self, basepath, filepath_l, tid_vocabulary=None,
                   encoding='utf8', error_handling='strict'):
        pass
