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
