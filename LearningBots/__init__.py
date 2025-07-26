# Powered By Team LearningBots
from LearningBots.core.bot import Anony
from LearningBots.core.dir import dirr
from LearningBots.core.git import git
from LearningBots.core.userbot import Userbot
from LearningBots.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
