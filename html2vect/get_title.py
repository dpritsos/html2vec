
import re

get_url_anchor = re.compile(r'<a.*href=(["\'].+?["\']).*[>](.+)(?=</a>)', re.UNICODE | re.IGNORECASE)

print get_url.findall('<a href="/eee/ee//e" style="fdfasdfsa" >CLICK WORLD!</a>')
