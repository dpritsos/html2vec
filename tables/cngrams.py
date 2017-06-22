#
#    Module: Character NGrams - from html row text/files to PyTables EArrays character...
#            ...NGrams Frequencies.
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.tables.cngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from ..base.html2tf import BaseHtml2TF
from ..base.html2tv import BaseHtml2TV
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.io.basefilehandlers import file_list_frmpaths

import numpy as np
import tables as tb
import gensim as gsm
from ..utils import tfdutils


class Html2TF(BaseHtml2TF):

    # Define the TermsType to be produced from this class.
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class.
        super(Html2TF, self).__init__(*args, **kwrgs)

    def yield_(self, xhtml_file_l, h5_fname, tid_vocabulary, norm_func, encoding, error_handling):

        # Creating the Dictionary from the given corpus if not given form the use
        if tid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            tf_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            tid_vocabulary = tfdutils.tf2tidx(tf_vocabulary)

        # Creating h5file.
        h5f = tb.open_file(h5_fname, 'w')

        # Defining pyTables Filters.
        filters = tb.Filters(complevel=1, complib='lzo', shuffle=True, fletcher32=False)

        # Initializing EArray. NOTE: expected row is critical for very large scale corpora.
        # NOTE: It has to be tb.Float64Atom() in case a limit -> 0 will be used in farther...
        # ...Text Classification or other vector calculations.
        fq_earray = h5f.create_earray(
            '/', 'corpus_earray', tb.Float64Atom(), shape=(0, len(tid_vocabulary)),
            expectedrows=len(xhtml_file_l), filters=filters
        )

        print "Creating NGrams-TF"
        # Create the NGrams-TF Sparse Matrix for all...
        # ...HTML attributes requested.
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                # Creating the pytables Earray for the data.
                fq_earray.append(
                    # Appending an numpy.array 2D to expandable array of pytables.
                    self.tl2tf.trms2f_narray(
                        # Getting the Character or Word n-grams list.
                        # NOTE: self.__class__.terms_lst is the only way to work correctly when...
                        # this class will be used as Parent class.
                        self.__class__.s2ngl.terms_lst(
                            # Getting the HTML attributes (usually text) as requested at Object...
                            # ...Initialization.
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        ),
                        # Setting some parameters required here.
                        tid_vocabulary, norm_func, d2=True
                        # Parameter dtype has omitted and letting the default value to be applied.
                    )
                )

        # Return Corpus Frequencies'-per-Document EArray
        return (fq_earray, h5f, tid_vocabulary)

    def from_src(self, xhtml_str, tid_vocabulary=None):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, h5_fname, tid_vocabulary=None, norm_func=None,
                   encoding='utf8', error_handling='strict'):
        return self.yield_(
            xhtml_file_l, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

    def from_paths(self, basepath, filepath_l, h5_fname, tid_vocabulary=None, norm_func=None,
                   encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        matrix, h5f, tid_dict = self.from_files(
            xhtml_file_l, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, h5f, tid_dict, xhtml_file_l)


class Html2TV(BaseHtml2TV):

    # Define the TermsType to be produced from this class.
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class.
        super(Html2TV, self).__init__(*args, **kwrgs)

    def yield_(self, xhtml_file_l, h5_fname, rtid_vocabulary, norm_func, encoding, error_handling):

        # Creating the Dictionary from the given corpus if not given form the use
        if rtid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            rtv_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            rtid_vocabulary = tfdutils.tf2tidx(rtv_vocabulary)

        # Creating h5file.
        h5f = tb.open_file(h5_fname, 'w')

        # Defining pyTables Filters.
        filters = tb.Filters(complevel=1, complib='lzo', shuffle=True, fletcher32=False)

        # Initializing EArray. NOTE: expected row is critical for very large scale corpora.
        # NOTE: It has to be tb.Float64Atom() in case a limit -> 0 will be used in farther...
        # ...Text Classification or other vector calculations.
        vars_earray = h5f.create_earray(
            '/', 'corpus_earray', tb.Float64Atom(), shape=(0, len(rtid_vocabulary)),
            expectedrows=len(xhtml_file_l), filters=filters
        )

        print "Creating NGrams-RootTermsVariance"
        # Create the NGrams-RootTermsVariance Matrix for all...
        # ...HTML attributes requested.
        for html_attrib in self.html_attrib_lst:
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                # Creating the pytables Earray for the data.
                vars_earray.append(
                    # Appending an numpy.array 2D to expandable array of pytables.
                    self.tf2tv.terms2v_narray(
                        # Getting the Character or Word n-grams list.
                        # NOTE: self.__class__.terms_lst is the only way to work correctly when...
                        # this class will be used as Parent class.
                        self.__class__.s2ngl.terms_lst(
                            # Getting the HTML attributes (usually text) as requested at Object...
                            # ...Initialization.
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        ),
                        # Setting some parameters required here.
                        self.rt_size, rtid_vocabulary, norm_func, d2=True
                        # Parameter dtype has omitted and letting the default value to be applied.
                    )


                )

        # Return Corpus Frequencies'-per-Document EArray
        return (vars_earray, h5f, rtid_vocabulary)

    def from_src(self, xhtml_str, tid_vocabulary=None):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, h5_fname, tid_vocabulary=None, norm_func=None,
                   encoding='utf8', error_handling='strict'):
        return self.yield_(
            xhtml_file_l, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

    def from_paths(self, basepath, filepath_l, h5_fname, tid_vocabulary=None, norm_func=None,
                   encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        matrix, h5f, rtid_dict = self.from_files(
            xhtml_file_l, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, h5f, rtid_dict, xhtml_file_l)


# To Be Written
class Html2TPL(object):

    def __init__(self):
        pass


class Html2LSI(BaseHtml2TF):

    # Define the TermsType to be produced from this class.
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class.
        super(Html2LSI, self).__init__(*args, **kwrgs)

    def yield_(self,
               xhtml_file_l, dims, h5_fname,
               tid_vocabulary, norm_func, encoding, error_handling):

        # Creating the Dictionary from the given corpus if not given form the use
        if tid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            tf_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            tid_vocabulary = tfdutils.tf2tidx(tf_vocabulary)

        # Creating h5file.
        h5f = tb.open_file(h5_fname, 'w')

        # Defining pyTables Filters.
        filters = tb.Filters(complevel=1, complib='lzo', shuffle=True, fletcher32=False)

        # Initializing EArray. NOTE: expected row is critical for very large scale corpora.
        # NOTE: It has to be tb.Float64Atom() in case a limit -> 0 will be used in farther...
        # ...Text Classification or other vector calculations.
        fq_earray = h5f.create_earray(
            '/', 'corpus_earray', tb.Float64Atom(), shape=(0, len(tid_vocabulary)),
            expectedrows=len(xhtml_file_l), filters=filters
        )

        print "Creating NGrams-TF"
        # Create the NGrams-TF Sparse Matrix for all...
        # ...HTML attributes requested.

        id2trm = dict(zip(tid_vocabulary.values(), tid_vocabulary.keys()))

        lsi_mdl = gsm.models.LsiModel(num_topics=dims, id2word=id2trm)

        for html_attrib in self.html_attrib_lst:

            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):

                # Creating the pytables Earray for the data, which later will be used for...
                # ...returing the projected corpus
                fq_earray.append(
                    # Creating numpy.array of Frequencies of the respective terms.
                    self.tl2tf.trms2f_narray(
                        # Getting the Character or Word n-grams list.
                        # NOTE: self.__class__.terms_lst is the only way to work correctly when...
                        # this class will be used as Parent class.
                        self.__class__.s2ngl.terms_lst(
                            # Getting the HTML attributes (usually text) as requested at Object...
                            # ...Initialization.
                            self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))
                        ),
                        # Setting some parameters required here.
                        tid_vocabulary, norm_func, d2=True
                        # Parameter dtype has omitted and letting the default value to be applied.
                    )
                )

        # Training/Extending the LSI model squentially.
        lsi_mdl.add_documents(
            gsm.matutils.Dense2Corpus(fq_earray[:, :].T)  # SOS: should this be Traspose?
        )

        # Creating LSI pyTables array of the Corpus Projection in LSI model.
        lsi_array = h5f.create_array(
            '/', 'corpus_LSI_array',
            gsm.matutils.corpus2dense(
                lsi_mdl[gsm.matutils.Dense2Corpus(fq_earray[:, :].T)],
                num_terms=dims
            ).T
        )

        # Returning Corpus LSI and Frequencies per Document.
        return (lsi_array, fq_earray, h5f, tid_vocabulary)

    def from_src(self, xhtml_str, tid_vocabulary=None):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l, dims, h5_fname,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(
            xhtml_file_l, dims, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

    def from_paths(self, basepath, filepath_l, dims, h5_fname,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        lsi_array, fq_earray, h5f, tid_vocabulary = self.from_files(
            xhtml_file_l, dims, h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (lsi_array, fq_earray, h5f, tid_vocabulary, xhtml_file_l)


class Html2GsmVec(BaseHtml2TF):

    # Define the TermsType to be produced from this class.
    s2ngl = String2CNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initializing BaseHtml2TF Class.
        super(Html2GsmVec, self).__init__(*args, **kwrgs)

    def yield_(self,
               xhtml_file_l, dims, min_trm_fq, win_size, algo, alpha, min_alpha, epochs, decay,
               h5_fname, tid_vocabulary, norm_func, encoding, error_handling):

        # Creating the Dictionary from the given corpus if not given form the use
        if tid_vocabulary is None:

            # Creating Terms-Frequnecies Vocabulary.
            tf_vocabulary = self._build_vocabulary(xhtml_file_l, encoding, error_handling)

            # Get the Vocabulary keeping all the terms this 'min_trm_fq' frequency and above.
            resized_tf_vocab = tfdutils.keep_min_fq(tf_vocabulary, min_trm_fq)

            # Create The Terms-Index Vocabulary that is shorted by Frequency descending order.
            # The if statment prevent creating an empty Vocabulary when very small corpus is...
            # ...provided as an input.
            if resized_tf_vocab != {}:

                tid_vocabulary = tfdutils.tf2tidx(resized_tf_vocab)

            else:

                tid_vocabulary = tfdutils.tf2tidx(tf_vocabulary)

                wrn = "The min_trm_fq option has been ignored because" +\
                      " is causing a zero (0) size Vocabulary."
                warnings.warn(wrn)

        # Creating h5file.
        h5f = tb.open_file(h5_fname, 'w')

        # Defining pyTables Filters.
        filters = tb.Filters(complevel=1, complib='lzo', shuffle=True, fletcher32=False)

        # Initializing EArray. NOTE: expected row is critical for very large scale corpora.
        # NOTE: It has to be tb.Float64Atom() in case a limit -> 0 will be used in farther...
        # ...Text Classification or other vector calculations.
        fq_earray = h5f.create_earray(
            '/', 'corpus_array', tb.Float64Atom(), shape=(0, len(tid_vocabulary)),
            expectedrows=len(xhtml_file_l), filters=filters
        )

        # List of TaggedDocuments objects one for each sentence of each document, plus a list of...
        # terms-list one for each document.
        corptgd_sentces_lst = list()
        corp_doctermslist_lst = list()

        print "Creating NGrams-TF and Gensim Doc2Vec List."
        # Create the NGrams-TF Sparse Matrix for all...
        # ...HTML attributes requested.

        for html_attrib in self.html_attrib_lst:

            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):

                # Getting the HTML attributes (usually text) as requested at Object...
                # ...Initialization.
                clean_doc = self._string_case(self.h2attr.__getattribute__(html_attrib)(html_str))

                # Spliting the document in sentences.
                doc_sents_lst = [sentence for sentence in clean_doc.split('. ') if sentence]
                if doc_sents_lst == []:
                    doc_sents_lst = [clean_doc]

                # Document's Full Terms List.
                doc_trms_lst = list()

                for i, sent in enumerate(doc_sents_lst):
                    # Getting the Character or Word n-grams list.
                    # NOTE: self.__class__.terms_lst is the only way to work correctly when...
                    # this class will be used as Parent class.
                    sent_trm_lst = self.__class__.s2ngl.terms_lst(sent)

                    # Getting the Terms are inlcuded in Vocabulary only!
                    sent_trm_lst_in_vocab = [
                        trm for trm in sent_trm_lst if trm in tid_vocabulary.keys()
                    ]

                    # Populating the corpus sentence list.
                    corptgd_sentces_lst.append(
                        gsm.models.doc2vec.TaggedDocument(sent_trm_lst_in_vocab, [i])
                    )

                    # Extending the list of the document's terms list with the terms of this...
                    # ...sentence.
                    doc_trms_lst.extend(sent_trm_lst_in_vocab)

                # Keeping the full list of terms for this document. This list will be used...
                # ...for creating the Doc2Vec projection vector of the full corpus.
                corp_doctermslist_lst.append(doc_trms_lst)

                # Creating the pytables Earray for corpus TF vectors for each Document.
                fq_earray.append(
                    # Creating numpy.array of Frequencies of the respective terms.
                    self.tl2tf.trms2f_narray(
                        sent_trm_lst_in_vocab, tid_vocabulary, norm_func, d2=True
                        # Parameter dtype has omitted and letting the default value to be applied.
                    )
                )

        # Choosing algorithm for Gensim Doc2Vec.
        if algo == 'PV-DBOW':
            dm = 0
        elif algo == 'PV-DM':
            dm = 1
        else:
            raise Exception("Invalid option for 'alog' argument.")

        # When decay is non-zero then  linear learning-rate is triggered. Following the manual..
        # ...instructions of Gensim lib.
        if decay:

            doc2vec_mdl = gsm.models.doc2vec.Doc2Vec(
                size=dims, window=win_size, dm=dm, alpha=alpha, min_alpha=min_alpha
            )

            doc2vec_mdl.build_vocab(corptgd_sentces_lst)

            doc2vec_mdl.train(
                corptgd_sentces_lst,
                total_examples=doc2vec_mdl.corpus_count, epochs=doc2vec_mdl.iter
            )

        else:

            doc2vec_mdl = gsm.models.doc2vec.Doc2Vec(
                size=dims, window=win_size, dm=dm, iter=epochs, alpha=alpha, min_alpha=min_alpha
            )

            doc2vec_mdl.build_vocab(corptgd_sentces_lst)

            for epoch in range(epochs):

                doc2vec_mdl.train(
                    corptgd_sentces_lst,
                    total_examples=doc2vec_mdl.corpus_count, epochs=doc2vec_mdl.iter
                )

                doc2vec_mdl.alpha -= decay  # decreasing the learning rate
                doc2vec_mdl.min_alpha = model.alpha

        # Creating the Gensim Doc2Vec Earray table.
        gsm_d2v_earray = h5f.create_earray(
            '/', 'corpus_GsmDoc2Vec_array', tb.Float64Atom(), shape=(0, dims),
            expectedrows=len(xhtml_file_l), filters=filters
        )

        # Appending the Infered Doc2Vec vectors to the Doc2Vec Earray.
        for doc_trm_lst in corp_doctermslist_lst:
            gsm_d2v_earray.append(doc2vec_mdl.infer_vector(doc_trm_lst).reshape((1, dims)))

        # Returning Corpus LSI and Frequencies per Document.
        return (gsm_d2v_earray, fq_earray, h5f, tid_vocabulary)

    def from_src(self, xhtml_str, tid_vocabulary=None):
        raise Exception("Please use from_files() or from_paths() methods instead")

    def from_files(self, xhtml_file_l,
                   dims, min_trm_fq, win_size, algo, alpha, min_alpha, epochs, decay, h5_fname,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(
            xhtml_file_l, dims, min_trm_fq, win_size, algo, alpha, min_alpha, epochs, decay,
            h5_fname, tid_vocabulary, norm_func, encoding, error_handling
        )

    def from_paths(self, basepath, filepath_l,
                   dims, min_trm_fq, win_size, algo, alpha, min_alpha, epochs, decay, h5_fname,
                   tid_vocabulary=None, norm_func=None, encoding='utf8', error_handling='strict'):

        # Get the filenames located in the paths given
        xhtml_file_l = file_list_frmpaths(basepath, filepath_l)

        # Create the vectors sparse matrix for this files
        gsm_d2v_earray, fq_earray, h5f, tid_vocabulary = self.from_files(
            xhtml_file_l,
            dims, min_trm_fq, win_size, algo, alpha, min_alpha, epochs, decay, h5_fname,
            tid_vocabulary, norm_func, encoding, error_handling
        )

        # Return the matrix, the dictionary created and the xhtml_files_list
        return (gsm_d2v_earray, fq_earray, h5f, tid_vocabulary, xhtml_file_l)
