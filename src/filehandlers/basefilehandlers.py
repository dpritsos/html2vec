""" """

import codecs
import os

class BasePathFileHandler(object):
    
    def __init__(self):
        pass
    
    def file_list_frmpaths(self, basepath, filepath_l):
        if basepath is None:
            basepath = '' 
        if isinstance(filepath_l, str):
            flist = [ files_n_paths[2] for files_n_paths in os.walk( basepath + filepath_l ) ]
            flist = flist[0]
            fname_lst = [ basepath + filepath_l + fname for fname in flist ]
        elif isinstance(filepath_l, list):
            fname_lst = list()
            for filepath in filepath_l:
                flist = [ files_n_paths[2] for files_n_paths in os.walk( basepath + filepath ) ]
                flist = flist[0]
                fname_lst.extend( [ basepath + filepath + fname for fname in flist ] )
        else:
            raise Exception("A String or a list of Strings was Expected as input - Stings should be file-paths")
        #For ease of usage the filename list should be returned sorted
        fname_lst.sort()
        return fname_lst
    
    @staticmethod
    def copyfile(source, dest):
        """ copyfile(): Copy a file from source to dest path. """
        source_f = open(source, 'rb')
        dest_f = open(dest, 'wb')
        while True:
            copy_buffer = source_f.read(1024*1024)
            if copy_buffer:
                dest_f.write(copy_buffer)
            else:
                break
        source_f.close()
        dest_f.close()
        
    @staticmethod
    def movefile(source, dest):
        """ movefile(): A UNIX compatible function for moving file from Source path
            to Destination path. The Source path Hard Link is deleted  """
        os.link(source, dest)
        os.unlink(source)
        

class BaseFileHandler(BasePathFileHandler):

    def __load_file(self, filename, encoding='utf-8', error_handling='strict'):
        """ """
        try:
            fenc = codecs.open( filename, 'rb',  encoding, error_handling) 
        except Exception as e:
            print("BaseFileHandler.__load_file() FILE %s ERROR: %s" % (filename, e))
            return None
        try:
            fstr = fenc.read()
        except Exception as e:
            print("BaseFileHandler.load_file() FILE %s ERROR: %s" % (filename, e))
            return None
        finally:
            fenc.close()    
        return fstr  
    
    def load_files(self, filename_l, encoding='utf-8', error_handling='strict'):
        """ """
        if isinstance(filename_l, str):
            return self.__load_file(filename_l, encoding, error_handling)
        elif isinstance(filename_l, list):
            fstr_lst = list()
            for filename in filename_l:
                fstr_lst.append( self.__load_file(filename, encoding, error_handling) )
            return fstr_lst
        else:
            raise Exception("A String or a list of Strings was Expected as input")
    
    def load_frmpaths(self, basepath, filepath_l, encoding='utf-8', error_handling='strict'):
        """ """
        fname_lst = self.file_list_frmpaths(basepath, filepath_l)
        return  [ [fname, fstr] for fname, fstr in zip(fname_lst, self.load_files(fname_lst, encoding, error_handling)) ]
    
    def save_files(self, basepath, fname_fstr_l, encoding='utf-8', error_handling='strict'):
        if not basepath:
            basepath = ""
        for filename, fstr in fname_fstr_l:
            with codecs.open( (basepath + filename), 'w', encoding, error_handling) as fobj:
                fobj.write(fstr)
        

        
            
            
    
    
    
    
        
    
