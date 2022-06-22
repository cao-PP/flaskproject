import datetime
import os
# from re import template
from string import Template
from flask import Flask, send_file, request, jsonify
# from werkzeug.utils import secure_filename
from flask_cors import CORS
import time
import zipfile


app = Flask(__name__)
absolute = os.path.dirname(__file__)
CORS(app)
app.debug = True


# 定义文件的保存路径和文件名尾缀
FOLDER = os.path.join(absolute, 'save_file')
HOST = "111.62.111.13"
PORT = 22
UPLOAD = 'upload'
app.config['UPLOAD'] = UPLOAD
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['zip'])


# 进行文件类型判断的函数
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 默认访问
# @app.route('/')
# def index():
#   html = Template(
#       """
#   <!DOCTYPE html>
#   <html>
#       <body style='padding-left:30px;'>
#         <a href='http://localhost:8080/download'>下载</a>
#         <br>
#         <a href='http://localhost:8080/upload'>上传</a>
#       </body>
#   </html>
#   """
#   )
#   html = html.substitute()
#   return html


# 上传
@app.route('/upload', methods=['post'])
def upload_file():
    # file_dir = os.path.join(basedir, app.config['UPLOAD'])
    #
    # if not os.path.exists(file_dir):
    #     os.makedirs(file_dir)

    file = request.files['test_file']
    fileName = file.filename

    if str(fileName).split('.')[1] != 'zip':
        return jsonify({"state": 200, "data": "上传失败"})

    try:
        startNow = datetime.datetime.now()

        zip_file = zipfile.ZipFile(file)
        for names in zip_file.namelist():       # 解压
            zip_file.extract(names, names)
        zip_file.close()

        endNow = datetime.datetime.now()
        print(endNow - startNow)

        return jsonify({"state": 500, "errmsg": "上传成功"})

    except Exception as e:
        pass


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

