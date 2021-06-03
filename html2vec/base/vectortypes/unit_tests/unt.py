





d1 =  {'a unit test': 1, 'html2tfd.charngrams.BaseString2TF class for': 1, 'test for html2tfd.charngrams.BaseString2TF': 1,\
 'for html2tfd.charngrams.BaseString2TF class': 1, 'is a unit': 1, 'for html2vectors package/module': 1, 'This is a': 1,\
 'unit test for': 1} 

d2 = {'is a unit': 1, 'test for html2tfd.charngrams.BaseString2TF': 1, 'a unit test': 1, 'This is a': 1,\
 'html2tfd.charngrams.BaseString2TF class for': 1, 'for html2tfd.charngrams.BaseString2TF class': 1, 'unit test for': 1,\
 'class for html2vectors package/module': 1, 'for html2vectors package/module': 1}




print [t1 for t1 in d2.keys() if t1 not in d1.keys()]
print len([t1 for t1 in d2.keys() if t1 in d1.keys()]), len(d1), len(d2)
