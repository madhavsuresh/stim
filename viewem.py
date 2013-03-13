import web
from threading import Thread
import os
from constants import *
import dir

PLAYER = 'omxplayer'
VIDEO_PATH = '/home/pi/stim/static/vids'
TURN_ON_PORT = 'echo "1" > /sys/class/gpio/gpio17/value'
TURN_OFF_PORT = 'echo "0" > /sys/class/gpio/gpio17/value'

urls = ('/', 'play', '/playem',
        'playit')
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
       
        
def play_em(fname):
    print fname
    #exstr = TURN_OFF_PORT + ' && '  + PLAYER + ' ' + VIDEO_PATH + ' ' + fname + ' && ' + TURN_ON_PORT
    exstr = PLAYER + ' ' + VIDEO_PATH + ' ' + fname
    #print exstr
    os.system(exstr)

if __name__ == '__main__':
    dir.makeit()
    app.run()
