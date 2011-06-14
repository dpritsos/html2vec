""" """

import difflib
from filehandlers import basefilehandlers as bfs
import StringIO

genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] # 
base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
text_path_l = ["/txt_rapidminer_app/", "/txt_html2vectors_mod/"]
diff_txt = "/txt_diffs_rapid-h2v/"

file_hdlr = bfs.BaseFileHandler()
diffsto_html = difflib.HtmlDiff()

for g in genres:
    fn_ftxt_ll = list()
    for text_path in text_path_l:
        fn_ftxt_ll.append( file_hdlr.load_frmpaths(base_filepath, g + text_path, encoding='utf-8', error_handling='replace') )
    for i, fn_ftxt_l in enumerate(fn_ftxt_ll):
        fn_ftxt_ll[i] = [ [fn.split('/')[-1], ftxt] for fn, ftxt in fn_ftxt_l ]
    #for fn_ftxt_l in fn_ftxt_ll:
    #    if  fn_ftxt_l[1] == None or fn_ftxt_l[1] == "":
    #        print fn_ftxt_l[0] 
    #0/0
    #print fn_ftxt_ll[0][0]
    #print fn_ftxt_ll[1][0]
    for i in range( len(fn_ftxt_ll[0]) ):
        #Save Diffs in html file format
        #print fn_ftxt_ll[0][i][0]
        try:
            diffs = diffsto_html.make_file(fn_ftxt_ll[0][i][1], fn_ftxt_ll[1][i][1])
        except:
            print fn_ftxt_ll[0][i][0]
            print fn_ftxt_ll[1][i][0]
        sv_fn_ftxt_l =  [[base_filepath + g + diff_txt + fn_ftxt_ll[0][i][0] + ".diff.html", str(diffs) ]]
        file_hdlr.save_files(None, sv_fn_ftxt_l, encoding='utf-8', error_handling='strict') 
        #Save Diffs in txt format
        try:
            diffs = difflib.context_diff(fn_ftxt_ll[0][i][1], fn_ftxt_ll[1][i][1])
        except:
            print fn_ftxt_ll[0][i][0]
            print fn_ftxt_ll[1][i][0]
        all_diffs = str()
        for diff in diffs:
            all_diffs += diff 
        sv_fn_ftxt_l =  [[base_filepath + g + diff_txt + fn_ftxt_ll[0][i][0] + ".diff", all_diffs ]]
        file_hdlr.save_files(None, sv_fn_ftxt_l, encoding='utf-8', error_handling='strict')
        