""" """

import os
from filehandlers import basefilehandlers as bfs

bfile_hdlr = bfs.BasePathFileHandler()

   
#genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#htmls_path = "/html/"
#text_path = "/txt_Htmlremover_app/"

genres = [ "" ] 
htmls_path = "/html/"
base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"

#base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Santini_corpus_html2txt\\"
#htmls_path_w = "\\html\\"
#text_path_w = "\\txt_Htmlremover_app\\"

base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Golden_Standared_from_Santinis_corpus\\"
htmls_path_w = "\\html\\"
text_path_w = "\\htmldetagger_console_ver_text\\"

for g in genres:
    file_lst = bfile_hdlr.file_list_frmpaths(base_filepath, g + htmls_path)
    file_lst = [ fname.split('/')[-1] for fname in file_lst ]
    for html_f in file_lst:
        os.spawnlp(os.P_WAIT, '/usr/bin/wine', '/usr/bin/wine',\
                   '/home/dimitrios/.wine/drive_c/Program Files/JafSoft/Detagger/h2acons.exe',\
                   base_filepath_w + g + htmls_path_w + html_f,\
                   '/out=' + base_filepath_w + g + text_path_w + html_f + ".txt" )





