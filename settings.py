from flask import Flask
from secret import secret_key

UPLOAD_FILES_DEST = "uploads/"

ACCEPTED_TYPES = set(["jpg", "gif", "png", "jpeg", 
                      "tif", "tiff", "bmp"])

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = secret_key
