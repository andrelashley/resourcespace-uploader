import requests
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get("USER") or "your_username"
PRIVATE_KEY = os.environ.get("PRIVATE_KEY") or 'placeholder'
# RS_RESOURCE_ID = 123
# FILE_NAME = "my_upload_file.jpg"