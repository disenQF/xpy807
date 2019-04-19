import json

from flask import Blueprint, jsonify
from flask import request

from dao_api.tearch_dao import  TeacherDao

blue = Blueprint('TeacherApi', __name__)


@blue.route('/teacher/', methods=('GET', 'POST'))
def teacher():
    dao = TeacherDao()

    if request.method == 'GET':
        all_teachers = dao.query_all()
        dao.close()
        return jsonify(all_teachers)

    if request.method == 'POST':
        # 上传的数据类型是json格式
        # {'tn': '老师的新编号', 'name': '老师的姓名'}
        upload_json = request.get_json()
        if upload_json:
            tn = upload_json.get('tn')
            name = upload_json.get('name')

            if tn and name :
                dao.save(tn=tn, name=name)
                dao.close()
                return jsonify({'code': 200,
                                'msg': '添加数据成功',
                                'data': upload_json})
            else:
                return jsonify({'code': 100,
                                'msg': 'tn和name参数不能为空',
                                'data': upload_json})
        else:
            return jsonify({'code': 9999,
                            'msg': '上传的数据必须是json格式'})