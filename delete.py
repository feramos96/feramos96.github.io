
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = """
for item in data:
	model = item.contents[1].find_all("a",{"class":"js-vehicle-name"})[0].text.strip() #.strip() to get rid of any annoying whitespace
	print(model)
"""
print(highlight(code, PythonLexer(), HtmlFormatter()))
print(HtmlFormatter().get_style_defs('.highlighter'))
