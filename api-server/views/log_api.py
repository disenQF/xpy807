from flask import Blueprint, jsonify
from flask import request

blue = Blueprint('LogApi', __name__)


@blue.route('/log/', methods=('POST', ))
def upload_log():

    print(request.form)

    return jsonify({
        'status': 'ok',
        'msg': '日志上传成功'
    })