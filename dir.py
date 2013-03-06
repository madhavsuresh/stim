import os

SUFFIX_LENGTH = 4

def get_categories(directory):
    cats = {}
    l = os.listdir(directory)
    for vid in l:
        spl = vid.split('#')
        print spl
        pretty_print = spl[1][:-SUFFIX_LENGTH].replace('_',' ')
        print pretty_print
        
        if len(spl) > 1 and spl[0] in cats:
            cats[spl[0]].append((vid,pretty_print))
        else:
            cats[spl[0]] = [(vid,pretty_print),]
    for key in cats:
        print key
        for els in cats[key]:
            print '\t' , els[0] + ' ' +  els[1]
    return cats
        

get_categories('./vids/')
