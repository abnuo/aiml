import sys
import json
from bs4 import BeautifulSoup
from xml.sax.saxutils import escape

def tab(n):
  return " "*n

list = ["Hello World!", "Goodbye World!"]
name = "origin"
out = """<category>
  <pattern>X"""+name.upper()+"""</pattern>
  <template>
    <random>
"""
for i in list:
  if not i == list[-1]:
    out=out+f"{tab(6)}<li>{escape(i)}</li>\n"
  else:
    out=out+f"{tab(6)}<li>{escape(i)}</li>"
out=out+"""
    </random>
  </template>
</category>"""
print(out)
