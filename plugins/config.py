import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7830984248:AAFgFOWSSFW9GAP0i38LpkLVNb6pb9DWwcE")
    
    API_ID = int(os.environ.get("API_ID", "26729193"))
    
    API_HASH = os.environ.get("API_HASH", "a94598ef642481e35466292df95f251e")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1608365151231-7dbed3034787%3Ffm%3Djpg%26q%3D60%26w%3D3000%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8M3x8aGFwcHklMjBiYWJ5fGVufDB8fDB8fHww&tbnid=0yhNfCmQL9-ZGM&vet=1&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fhappy-baby&docid=0kxURV9oahKycM&w=3000&h=2000&source=sh%2Fx%2Fim%2Fm1%2F2&kgs=0c2f8657d8575bcc")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Uploaderbot:Uploaderbot@cluster0.mkxbrre.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002607015025"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002607015025")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1012164907"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Uploderbbbb_bot")
                                  
