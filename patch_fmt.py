import re

h = open('index.html').read()
old = 'function fmt(v) { return v > 0 ?'
new = 'function fmt(v) { if(typeof v==="string") return v; return v > 0 ?'
h = h.replace(old, new)
open('index.html', 'w').write(h)
print('patched fmt() to handle strings')
