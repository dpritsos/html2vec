#
#    Module: TF Dictionary-Files Handler
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.io.tfdfileshadlers: submodule of `html2vect` module defines the class TFdictFilesHandler """


""" This module seams not be need anymore, however, let it be for GreenThreading paradigm and future usage. """


import eventlet
import codecs
basefillers import file_list_frmpaths


class TFdictFilesHandler(object):

    def __init__(self):
        pass


    def __load_tf_dict(self, filename, encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ __load_tf_dict(): do not use this function prefer the TFdictFilesHandler.load_tf_dict().
            This function is getting a filename and a lower case force option and returns a
            Term-Frequency dictionary loaded from the file given as argument. """
        try:
            fenc = codecs.open( filename, 'rb', encoding, error_handling)
        except IOError as e:
            print("TFdictFilesHandler.load_dict() FILE %s ERROR: %s" % (filename,e))
            return None

        #The following for loop is an alternative approach to reading lines instead of using f.readline() or f.readlines()
        tf_d = dict()
        try:
            for fileline in fenc:
                line = fileline.rstrip()
                line = fileline.rstrip()

                if len(line.split(" ~~> ")) != 2:
                    print line

                Term, Freq = tuple( line.split(" ~~> ") )

                if force_lower_case:
                    tf_d[ Term.lower() ] = float( Freq )
                else:
                    tf_d[ Term ] = float( Freq )

        except Exception as e:
            print("TFdictFilesHandler.__load_tf_dict() Error: %s" % e)
            return None

        finally:
            fenc.close()

        return tf_d


    def load_tf_dict(self, filename_l, encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ load_tf_dict(): is getting a filename or a (filename list) and lower case force option
            as arguments. It returns a Term-Frequency Dictionary which is a merged dictionary of all
            TF dictionaries given a argument """
        if isinstance(filename_l, str):
            return self.__load_tf_dict(filename_l, encoding, error_handling, force_lower_case)

        elif isinstance(filename_l, list):
            mrgd_tf_d = dict()

            for filename in filename_l:
                tf_d = self.__load_tf_dict(filename, encoding, error_handling, force_lower_case)
                for Term, Freq in tf_d.items():
                    if Term in mrgd_tf_d:
                        mrgd_tf_d[ Term ] += Freq
                    else:
                        mrgd_tf_d[ Term ] = Freq

            return mrgd_tf_d

        else:
            raise Exception("A String or a list of Strings was Expected as input")


    def load_tfd_frmpaths(self, basepath, filepath_l, encoding, error_handling, force_lower_case=False):
        """ laod_tf_frmpaths: is getting a list of paths as argument and a base path as optional argument.
            Returns a merge of all Term-Frequency Dictionaries found in the file paths list. """
        fname_lfile_list_frmpaths(basepath, filepath_l)
        return self.load_tf_dict(fname_lst, encoding, error_handling, force_lower_case)


    def __load_tf_dict_l(self, filename, line_lim=0 , encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ __load_tf_dict_l(): is getting a filename as argument and force lower_case as optional argument.
            It returns an a list for TF dictionaries and a list of the web-pages where the TF Dictionaries are
            related to. If line_lim is set above 0 then If a file contains more than one line (i.e. web page vectors) keep
            only the amount of pages requested in this argument  """
        try:
            fenc = codecs.open( str(filename), 'rb', encoding, error_handling )

        except IOError, e:
            print("TFdictFilesHandler.__load_dict_l() FILE %s ERROR: %s" % (filename,e))
            return None

        #The following for loop is an alternative approach to reading lines instead of using f.readline() or f.readlines()
        wps_l = list()
        vect_l = list()
        try:
            lines_cnt = 0
            wholetxt = fenc.read()

            for fileline in wholetxt.split("\n~\n~\n"):
                line = fileline.rstrip()
                wp_name, wp_tf_d = tuple( line.split(" ~~> ") ) #BE CAREFULL with SPACES
                wps_l.append( wp_name )
                composed_terms = wp_tf_d.split('\t~,~\t')
                vect_dict = dict()

                for comp_term in composed_terms:
                    Term, Freq = tuple( comp_term.split(' ~:~ ') )
                    if force_lower_case:
                        vect_dict[ Term.lower() ] = float( Freq )
                    else:
                        vect_dict[ Term ] = float( Freq )

                vect_l.append( vect_dict )
                #If a file contains more than one line (i.e. web page vectors) keep
                #only the amount of pages requested in the line_lim argument
                lines_cnt += 1

                if lines_cnt == line_lim:
                    break

        except Exception as e:
            print("TFdictFilesHandler.__load_dict_l() FILE %s ERROR: %s" % (filename,e))
            return None

        finally:
            fenc.close()

        return (wps_l, vect_l)


    def load_tf_dict_l(self, filename_l, page_lim=0, encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ loadtf_dict_l(): is getting a filename or a filename list as first arguments and
            a lower case force option. If page_lim is set above 0 then If a file contains more than one line (i.e. web page vectors)
            or a folder contains more than one files then keeps only the amount of pages requested in this argument either
            because the amount of lines in a file have reached the argument or because the amount of file have been loaded have. """
        if isinstance(filename_l, str):
            return self.__load_tf_dict_l(filename_l, page_lim, encoding, error_handling, force_lower_case)

        elif isinstance(filename_l, list):
            mrgd_wps_l = list()
            mrgd_vect_l = list()

            for filename in filename_l:
                wps_l, vect_l = self.__load_tf_dict_l(filename, page_lim, encoding, error_handling, force_lower_case)
                mrgd_wps_l.extend( wps_l )
                mrgd_vect_l.extend( vect_l )

                #If a the merged list of web pages reached the the amount of pages requested
                #in the page_lim argument the loop stops
                if len(mrgd_wps_l) == page_lim:
                    break

            return (mrgd_wps_l, mrgd_vect_l)

        else:
            raise Exception("A String or a list of Strings was Expected as input")


    def load_tfd_l_frmpaths(self, basepath, filepath_l, page_lim=0, encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ load_tfd_l(): is getting a list of file-paths, a base-path, and a lower case force option
            as arguments. In addition it has the page_lim argument for constraining the amount of web page vectors to be
            loaded if requested using this argument. It returns a list of TF-Dictionaries and a list of the Web-pages related to
            the TF-Dictionaries, of all the files found in the file-paths lists."""
        fname_lst = file_list_frmpaths(basepath, filepath_l)
        return self.load_tf_dict_l(fname_lst, page_lim, encoding, error_handling, force_lower_case)


    def save_tf_dct(self, filename, tfd, encoding='utf-8', error_handling='strict'):
        """ save_tf_dct(): is getting a filename string and a TF-Dictionary saves
            the dictionary to a file with utf-8 Encoding. """
        try:
            #Codecs module is needed to assure the proper saving of string in UTF-8 encoding.
            fenc = codecs.open( filename, 'wb', encoding, error_handling)
        except IOError:
            return None

        try:
            for term, feq in tfd.items():
                fenc.write( term + " ~:~ "  + str(feq) + "\n" ) # Write a string to a file

        except Exception as e:
            print("ERROR WRITTING FILE: %s -- %s ~~> %s" % (e, filename, term))

        finally:
            fenc.close()

        return True


    def save_tf_dct_lst(self, filename, fname_tf_l, encoding='utf-8', error_handling='strict'):
        """ save_tf_dct_lst(): is getting a filename string a list of TF-Dictionaries and a List of Web-Pages
            related to the TF-Dictionaries and saves them to a file in the form <webpage-filename> ~~> <TF-Dictionary> """
        try:
            #Codecs module is needed to assure the proper saving of string in UTF-8 encoding.
            fenc = codecs.open( filename, 'wb', encoding, error_handling)
        except IOError as e:
            print "save_dct_lst Error: ", e
            return None

        try:

            for fn, tfd in fname_tf_l:
                fenc.write(fn + " ~~> ")
                tfd_len = len(tfd)

                for i, (term, freq) in enumerate(tfd.items()):
                    fenc.write( term + " ~:~ "  + str(freq) )

                    if i != tfd_len - 1:
                        fenc.write("\t~,~\t")

                fenc.write("\n~\n~\n")

        except Exception as e:
            print("ERROR WRITTING FILE: %s -- %s ~~> %s" % (e, fn, term))

        finally:
            fenc.close()

        return True




class GreenTFdictFilesHandler(TFdictFilesHandler):
    """ GreenTFdictFilesHandler Class is a GreenLet/Eventlet version of TFdictFilesHandler Class.
        Actually it just overrides the load_tf_dict() and load_tf_dict_l() with an Eventlet-Based
        version of them """

    def __init__(self):
        super(GreenTFdictFilesHandler, self).__init__()


    def load_tf_dict(self, filename_l, encoding='utf-8', error_handling='strict', force_lower_case=False):
        """ """
        if isinstance(filename_l, str):
            return self.__load_dict_l(filename_l, encoding, error_handling, force_lower_case)

        elif isinstance(filename_l, list):
            mrgd_wps_l = list()
            mrgd_vect_l = list()
            gpool = eventlet.GreenPool(1000)
            force_lower= map( lambda x: force_lower_case, range(len(filename_l)) )
            enc  = map( lambda x:  encoding, range(len(filename_l)) )
            err_handling = map( lambda x: error_handling, range(len(filename_l)) )

            for wps_l, vect_l in gpool.imap(self.__load_dict_l, filename_l, enc,  err_handling, force_lower):
                mrgd_wps_l.extend( wps_l )
                mrgd_vect_l.extend( vect_l )
            return (mrgd_wps_l, mrgd_vect_l)

        else:
            raise Exception("A String or a list of Strings was Expected as input")


    def load_tf_dict_l(self, filename_l, encoding='utf-8', error_handling='strict', force_lower_case=False):
        if isinstance(filename_l, str):
            return self.__load_tf_dict(filename_l, encoding, error_handling, force_lower_case)

        elif isinstance(filename_l, list):
            gpool = eventlet.GreenPool(1000)
            force_lower= map( lambda x: force_lower_case, range(len(filename_l)) )
            enc  = map( lambda x:  encoding, range(len(filename_l)) )
            err_handling = map( lambda x: error_handling, range(len(filename_l)) )
            mrgd_tf_d = self.__load_tf_dict(filename_l[0], encoding, error_handling, force_lower_case)

            for tf_d in gpool.imap(self.__load_tf_dict, filename_l[1:], enc,  err_handling, force_lower):

                for Term, Freq in tf_d.items():
                    if Term in mrgd_tf_d:
                        mrgd_tf_d[ Term ] += Freq
                    else:
                        mrgd_tf_d[ Term ] = Freq

            return mrgd_tf_d

        else:
            raise Exception("A String or a list of Strings was Expected as input")
