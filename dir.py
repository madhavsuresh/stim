import os
from jinja2 import Template

SUFFIX_LENGTH = 4

def get_categories(directory):
    cats = {}
    l = os.listdir(directory)
    for vid in l:
        spl = vid.split('__')
        pretty_print = spl[1][:-SUFFIX_LENGTH].replace('_',' ')
        if len(spl) > 1 and spl[0] in cats:
            cats[spl[0]].append((vid,pretty_print))
        else:
            cats[spl[0]] = [(vid,pretty_print),]
    '''
    for key in cats:
        print key
        for els in cats[key]:
            print '\t' , els[0] + ' ' +  els[1]
            '''
    return cats

def template_dis(cats,fname):
    f = open(fname)
    c = f.read()
    template = Template(c)
    return template.render(vids = cats)


f = open('out.html','w')
s = template_dis(get_categories('./vid_bk/'),'./temps/tst.html')
f.write(s)
f.close()
