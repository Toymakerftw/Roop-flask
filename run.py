from flask import Flask, render_template, request, jsonify, Response, send_from_directory
from werkzeug.utils import secure_filename
import os
from roop import core
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    jpg_file = request.files['jpgFile']
    mp4_file = request.files['mp4File']
    if jpg_file and allowed_file(jpg_file.filename) and mp4_file and allowed_file(mp4_file.filename):
        jpg_filename = secure_filename(jpg_file.filename)
        mp4_filename = secure_filename(mp4_file.filename)
        jpg_file.save(os.path.join(app.config['UPLOAD_FOLDER'], jpg_filename))
        mp4_file.save(os.path.join(app.config['UPLOAD_FOLDER'], mp4_filename))
        core.args.source_img = os.path.join(app.config['UPLOAD_FOLDER'], jpg_filename)
        core.args.target_path = os.path.join(app.config['UPLOAD_FOLDER'], mp4_filename)
        core.args.output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4')
        core.args.keep_fps = True
        core.args.keep_frames = True
        core.start()
        return jsonify({'message': 'Files uploaded and processed successfully'})
    else:
        return jsonify({'message': 'Invalid file type'})

@app.route('/status')
def status_stream():
    def event_stream():
        while True:
            if core.status_message:
                yield f"data: {core.status_message}\n\n"
                core.status_message = None
            time.sleep(0.1)
    return Response(event_stream(), mimetype="text/event-stream")

@app.route('/uploads')
@app.route('/uploads/<path:path>')
def uploaded_files(path=''):
    base_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    if not os.path.exists(base_path):
        return "Not found", 404
    if os.path.isfile(base_path):
        return send_from_directory(os.path.dirname(base_path), os.path.basename(base_path))
    files = os.listdir(base_path)
    file_links = []
    for filename in files:
        file_path = os.path.join(base_path, filename)
        if os.path.isdir(file_path):
            file_links.append(f"<a href='/uploads/{os.path.join(path, filename)}/'>{filename}/</a><br>")
        else:
            file_links.append(f"<a href='/uploads/{os.path.join(path, filename)}'>{filename}</a><br>")
    return "".join(file_links)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'mp4'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, debug=True)
