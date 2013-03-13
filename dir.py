import os
from jinja2 import Template
from constants import *


def get_categories(directory):
    cats = {}
    l = os.listdir(directory)
    for vid in l:
        spl = vid.split('__')
        pretty_print = spl[1][:-SUFFIX_LENGTH].replace('_',' ')
        htmlid = vid.replace('.','no_pants_mode')
        if len(spl) > 1 and spl[0] in cats:
            cats[spl[0]].append((vid,pretty_print,htmlid))
        else:
            cats[spl[0]] = [(vid,pretty_print,htmlid,)]
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


f = open(BASE_DIR + TEMPLATE_DIR + TEMPLATE_NAME,'w')
s = template_dis(get_categories(BASE_DIR + VID_DIR),BASE_DIR+TEMPLATE_DIR+MAKER_NAME)
f.write(s)
f.close()
