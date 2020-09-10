

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

"""
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
"""

path = os.getcwd()
if not os.path.exists('Files.2'):
    os.makedirs('Files.2')

