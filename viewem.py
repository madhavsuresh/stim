import web
from time import strptime, strftime
from threading import Thread
from subprocess import Popen
import os


urls = ('/(\w*)', 'play', '/playem/(\w*)',
        'playit')
render = web.template.render('/home/pi/stim2/templates/')
app = web.application(urls, globals())
class play:
    def GET(self,arg):
        return render.resp('')

class playit:
    def GET(self,arg):
        t = Thread(target=play_em)
        t.start()
        return render.resp('hello world')
        

class addTodo:
    def POST(self, school):
        i = web.input()
        with open('./todo', 'a') as tdo:
                tdo.write(i['todo1'] + '\n')


def play_em():
 os.system('sleep 1 && omxplayer /home/pi/out.mp4')

if __name__ == '__main__':
    app.run()
