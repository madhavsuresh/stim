import web
from threading import Thread
import os

PLAYER = 'omxplayer'
VIDEO_PATH = '/home/pi/stim/static/vids'
TURN_ON_PORT = 'echo "1" > /sys/class/gpio/gpio17/value'
TURN_OFF_PORT = 'echo "0" > /sys/class/gpio/gpio17/value'

urls = ('/', 'play', '/playem',
        'playit')
render = web.template.render('/home/madhav/bme390/stim/templates/')
app = web.application(urls, globals())
class play:
    def GET(self):
        print 'wat?'
        return render.out()

class playit:
    def GET(self):
        i = web.input()
        t = Thread(target=play_em, args=[i['file']])
        t.start()
        return None
       
        
def play_em(fname):
    print fname
    exstr = TURN_OFF_PORT + ' && '  + PLAYER + ' ' + VIDEO_PATH + ' ' + fname + ' && ' + TURN_ON_PORT
    print exstr
    os.system(exstr)

if __name__ == '__main__':
    app.run()
