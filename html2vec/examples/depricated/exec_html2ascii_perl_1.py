""" """

import subprocess
from filehandlers import basefilehandlers as bfs

bpfh = bfs.BasePathFileHandler()
#bfh = bfs.BaseFileHandler()

   
genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] 
#genres = [ "blog_pgs", "news_pgs", "product_pgs", "forum_pgs", "wiki_pgs" ]
base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#base_filepath = "/home/dimitrios/Synergy-Crawler/Manually_Selected_Crawled_corpus_75/"
#base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_500/"

htmls_path = "/html/"
#genres = [ "" ] 
#htmls_path = "html/"
#base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
text_path = "/html2ascii_perl_text/"

for g in genres:
    file_lst = bpfh.file_list_frmpaths(base_filepath, g + htmls_path)
    file_lst = [ fname.split('/')[-1] for fname in file_lst ]
    for html_f in file_lst:
        print base_filepath + g + htmls_path + html_f 
        p1 = subprocess.Popen(['/home/dimitrios/Development_Workspace/html2ascii_scripts/html2ascii.perl', base_filepath + g + htmls_path + html_f],\
                              stdout=subprocess.PIPE) 
        #, stderr=subprocess.PIPE) using this parameter it will prevent print error to std-outputand it will be placed in p1.communicate()[1]
        txt = p1.communicate()[0]
        with open(base_filepath + g + text_path + html_f.replace('.htm', '.html.txt'), 'w') as f:
            f.write(txt)
        #bfh.save_files(None, [[base_filepath + g + text_path + html_f + '.txt', txt]], encoding='utf8' )
        ###I am not using bfh.save_files because the output has Incompatible to UTF8 encoding





