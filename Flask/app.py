import os
from os.path import join,exists,isfile
from os import makedirs,listdir

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from recognize_diesease import recognize_diesease
from flask import jsonify

from constants import *

app = Flask(__name__)
app.secret_key = "super secret key"

path = os.getcwd()

# file Upload
UPLOAD_FOLDER = join(join(path, 'static'),'input_images')

# Make directory if "uploads" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# allow files of a specific type
ALLOWED_EXTENSIONS_IMAGE = set(['jpg','png'])


# function to check the file extension of image
def allowed_file_image(filename):
    '''
    Input:Image name with extension
    Output:True if extension in allowed image extension
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_IMAGE


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/recognisediesease', methods=['GET', 'POST'])
def recognise_diesease():
	"""
	Input:File
	Output:diesease name
	"""
	if request.method == 'POST':
		if 'file' not in request.files:
			return jsonify(
				response="file not found",
				status=404,
				mimetype='application/json'
				)

		file = request.files['file']
		if file.filename == '':
			return jsonify(
				response="file not found",
				status=404,
				mimetype='application/json'
				)
		print(file.filename)

		for images in os.scandir(UPLOAD_FOLDER):
			os.remove(images.path)


		if file and allowed_file_image(file.filename):
				filename = secure_filename(file.filename)
				file.save(join(app.config['UPLOAD_FOLDER'], 
					'leaf_image.jpg'))
				diesease_name = recognize_diesease()
				Treatment = diesease_treatment[diesease_name]
				return render_template('display.html', 
					text = str(diesease_name),
					file_name = str('leaf_image.jpg'),
					Treatment_disease = str(Treatment))

		else:
			return jsonify(
			            response="allowed format of file is jpg,png",
				        status=400,
				        mimetype='application/json'
			        )

		


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True,threaded=True)
