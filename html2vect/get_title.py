
import re

get_url_anchor = re.compile(r'<a.*href=(["\'].+?["\']).*[>](.+)(?=</a>)', re.UNICODE | re.IGNORECASE)

print get_url_anchor.findall('<a href="/eee/ee//e" style="fdfasdfsa" >CLICK WORLD!</a>')


class TestClass(object):

    def __init__(self):
        # Do Nothing.
        self.case = 'join'

    def testMethod(self, print_str):
        print print_str.__getattribute__(self.case)()


tc = TestClass()

if set(['testMethod', '__init__']) < set(dir(tc)):
    tc.__getattribute__('testMethod')("Hello World!")
