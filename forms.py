from flask import flash, Flask, request, render_template
from flaskext.wtf import Form, FileField, TextAreaField
from wtforms import ValidationError
from settings import app, ACCEPTED_TYPES


class UploadForm(Form):
    img = FileField(u"Select image file:")
    
    def validate_file(form, field):
        f = form.img.file.filename
        if '.' in f and f.rsplit('.', 1)[1] in ACCEPTED_TYPES:
            pass
        else:
            raise ValidationError()
