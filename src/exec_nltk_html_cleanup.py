
""" """
import nltk
import filehandlers.basefilehandlers

bfh = filehandlers.basefilehandlers.BaseFileHandler() 
   
#genres = [ "blog/html/", "eshop/html/", "faq/html/", "frontpage/html/", "listing/html/", "php/html/", "spage/html/"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#text_path = "/txt_html2vectors_mod/"

genres = [ "html/" ] 
base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
text_path = "/nltk-clean_html_text/"

for g in genres:
    fn_fhtml_l = bfh.load_frmpaths(base_filepath, g, encoding='utf-8', error_handling='replace')
    fn_fhtml_l = [ [fn.replace('/html/', text_path), nltk.clean_html(fhtml)] for fn, fhtml in fn_fhtml_l ]
    fn_ftxt_l = [ [fn.replace('.html', '.html.txt'), ftxt] for fn, ftxt in fn_fhtml_l ]
    bfh.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
   
