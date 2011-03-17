import os
import sys

import Image
from flask import Flask, request, flash, render_template
from werkzeug import secure_filename
from tesseract import image_to_string
from settings import *
from forms import UploadForm

def ocr(filename):
    f = open(os.path.join(UPLOAD_FOLDER, filename))
    return image_to_string(Image.open(f))

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if request.method == "POST":
        form = UploadForm(request.form)
        if form.validate():
            filename = secure_filename(form.img.file.filename)
            filename.save(os.path.join(UPLOAD_FOLDER, filename))
            flash(ocr(filename))
        else:
            flash("Invalid filename. Please choose another.")

    return render_template("base.html", form=form) 


if __name__ == "__main__":
    app.run(debug=True)