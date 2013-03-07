import web
from threading import Thread
import os
from constants import *

BASE_DIR = '/home/madhav/bme390/stim'
VID_DIR = '/static/vids/'
TEMPLATE_DIR = '/templates/'
TEMPLATE_NAME = 'out.html'
MAKER_NAME = 'maker.html'
VIDEO_PATH = BASE_DIR + VID_DIR
PLAYER = 'omxplayer'
TURN_ON_PORT = 'echo "1" > /sys/class/gpio/gpio17/value'
TURN_OFF_PORT = 'echo "0" > /sys/class/gpio/gpio17/value'
SUFFIX_LENGTH = 4



urls = ('/', 'play', '/playem',
        'playit','/vids/(.*)','vids')
render = web.template.render(BASE_DIR+TEMPLATE_DIR)
app = web.application(urls, globals())
class play:
    def GET(self):
        return render.out()

class playit:
    def GET(self):
        i = web.input()
        t = Thread(target=play_em, args=[i['file']])
        t.start()
        return None

class vids:
    def GET(self,args):
        return args
        
def play_em(fname):
    print fname
    #exstr = TURN_OFF_PORT + ' && '  + PLAYER + ' ' + VIDEO_PATH + ' ' + fname + ' && ' + TURN_ON_PORT
    exstr = PLAYER + ' ' + VIDEO_PATH + ' ' + fname
    #print exstr
    os.system(exstr)

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

def makeit():
    f = open(BASE_DIR + TEMPLATE_DIR + TEMPLATE_NAME,'w')
    s = template_dis(get_categories(VIDEO_PATH),BASE_DIR+TEMPLATE_DIR+MAKER_NAME)
    f.write(s)
    f.close()




if __name__ == '__main__':
    dir.makeit()
    app.run()
