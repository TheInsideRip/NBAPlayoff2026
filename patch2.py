h = open('index.html').read()
old = 'if(data.overview)renderOverview(data);'
new = 'try{if(data.overview)renderOverview(data);}catch(e){console.log("overview error",e);}'
if old in h:
    h = h.replace(old, new)
    open('index.html', 'w').write(h)
    print('patched')
else:
    print('ERROR: string not found in index.html')
