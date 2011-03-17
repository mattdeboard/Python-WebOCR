from flask import flash, Flask, request, render_template
from flaskext.wtf import Form, FileField, file_allowed, file_required, TextField
from flaskext.uploads import UploadSet, IMAGES
from wtforms import ValidationError
from wtforms.widgets import FileInput
from settings import app, ACCEPTED_TYPES

images = UploadSet("images", IMAGES)

class UploadForm(Form):
    img = FileField(u"Select image file:",
                    validators=[file_required(),
                                file_allowed(images, "Images only!")], 
                    widget=FileInput())
    
