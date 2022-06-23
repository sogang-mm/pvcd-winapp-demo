FILE_DIALOG_ROOT = '.\\samples'

VIDEO_EXTENSIONS = ('.3g2', '.3gp', '.3gp2', '.3gpp', '.asf', '.avchd', '.avi', '.flv', '.m1v', '.m4v', '.mkv', '.mov',
                    '.mp2', '.mp4', '.mpe', '.mpeg', '.mpg', '.mpv', '.qt', '.rm', '.swf', '.webm', '.wmv')
IMAGE_EXTENSIONS = ('.jpg', '.png')

VIDEO_EXTENSION_FILTER = 'All Video Files |' + ';'.join([f'*{i}' for i in VIDEO_EXTENSIONS])
IMAGE_EXTENSION_FILTER = 'All Image Files |' + ';'.join([f'*{i}' for i in IMAGE_EXTENSIONS])

DEFAULT_PIP_BACKGROUND = '.\\resource\\images\\pip\\background.jpg'
DEFAULT_LOGO = '.\\resource\\images\\logo\\Sogang_University_emblem.png'

DEFAULT_FONT = 'Segoe UI'
DEFAULT_FONT_SIZE = 24
DEFAULT_FONT_COLOR = '#000000'
DEFAULT_TRANSFORM_OUTPUT = 'outputs.mp4'

DEFAULT_QUERY_TOPK = 2
DEFAULT_QUERY_WND = 10
DEFAULT_QUERY_SCORE = 12
DEFAULT_QUERY_MATCH = 3

PVCD_QUERY_POST_URL = ''  #########
PVCD_QUERY_TIME_OUT = 10
DETECT_MAX_ROW = 30
POT_PLAYER_PATH = "C:\\Program Files (x86)\\DAUM\\PotPlayer\\PotPlayer.exe"
