from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + '/files' # 저장 경로
# print(UPLOAD_DIRECTORY)                               # 저장 경로 확인

if not os.path.exists(UPLOAD_DIRECTORY): # 존재하면 실행, 없다면 makedirs를 실행해서 만든다 (flask_upload 내부 files 폴더 생성)
    os.makedirs(UPLOAD_DIRECTORY)        # flask_upload 폴더 내부에 files 폴더 생성한다

app = Flask(__name__)

# 업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html') # /upload 요청 들어왔을 때 upload.html 문서 서비스(실행)

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식일 때 아래 작업 실행
        f = request.files['file'] # ['file'] -> file 개체
        # 저장할 경로 + 파일명
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(dirname)
        f.save(dirname)
    return redirect('/files')

@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY): # 리스트 안에 목록을 뽑아주는 것 (listdir)
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):    # file인지 물어본다. file이라면 아래 실행(.append 추가)
            files.append(filename)
    # return jsonify(files)         # json 문법 형식으로 변경
    ''' jsonify(files)의 결과값 
    ["\ub2e4\uc6b4\ub85c\ub4dc (2).jpeg", 
     "\ub2e4\uc6b4\ub85c\ub4dc (1).jpeg"
    ]
    '''
    return render_template('list.html', files = files)

@app.route("/files/<path:path>") # data 타입 path --> accepts slashes 
def get_file(path): # <path:path>의 :뒤의 path와 함수의 인자값과 동일
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8890)