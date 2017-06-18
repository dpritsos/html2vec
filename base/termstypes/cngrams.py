#
#    Module: cngrams - Character NGrams
#
#    Author: Dimitrios Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.termstypes.cngrams: submodule of `html2vect` module defines
    the class String2CNGramsList """


class String2CNGramsList(object):
    """ String2CNGramsList: Class
        Instance requires the size of NGrams.
        Methods:
            - terms_lst(text): is getting a Text and returns a list of NGrams with size
                equal to the size defined while instantiation """

    def __init__(self, n=1):

        # N-Grams size
        self.n = n

    @property
    def N(self):
        return self.n

    @N.setter
    def N(self, value):
        self.n = value

    def terms_lst(self, text):

        # In case not text is given it returns None. The outer code layer should handle...
        # ...this if caused due to error.
        if not text:
            return None

        # Cut the text into tokens size defined in instantiation of this class...
        # ...and put them in a List

        terms_l = list()

        for i in range(len(text) - self.n + 1):
            terms_l.append(text[i: i+self.n])

        return terms_l

    def terms_lst_segments(self, text):

        # In case not text is given it returns None. The outer code layer should handle...
        # ...this if caused due to error.
        if not text:
            return None

        # Cut the text into tokens size defined in instantiation of this class and put...
        # ...them in a List

        terms_l_seg = list()

        for j in range(12):  # range(len(text) - self.n + 1):
            terms_l_seg.append(
                [text[j+i: j+i+self.n] for i in range(0, len(text) - j - self.n + 1, 3)]
            )

        return terms_l_seg
