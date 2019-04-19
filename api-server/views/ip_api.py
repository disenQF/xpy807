from flask import Blueprint, jsonify
from flask import request

from dao_api.ip_dao import IPDao

blue = Blueprint('IpApi', __name__)


@blue.route('/proxy_ip/', methods=('GET', ))
def proxy_ip():
    client_ip = request.remote_addr
    print('client_ip', client_ip)

    return jsonify({
        'type': 'http',
        'ip': '119.102.29.228',
        'port': 9999
    })


@blue.route('/ip/', methods=('POST', 'PUT'))
def save_ip():
    # 表单参数： type 代理类型, ip 网址, port 端口, source来源
    type_ = request.form.get('type')
    ip = request.form.get('ip')
    port = request.form.get('port')
    source = request.form.get('source')

    dao = IPDao()
    msg = ''
    if request.method == 'POST':
        dao.save(ip, port, type_, source)
        msg = '添加数据成功'
    else:
        dao.update(ip=ip, port=port, type=type_, source=source)
        msg = '更新数据成功'
    return jsonify({'code': 200, 'msg': msg})


@blue.route('/ip/query/', methods=('GET', ))
def query():
    dao = IPDao()
    result = dao.query_all()
    return jsonify(result)


@blue.route('/ip/<string:ip>/', methods=('DELETE', ))
def delete(ip):
    dao = IPDao()
    dao.delete(ip)
    return jsonify({
        'code': 300,
        'msg': '删除成功'
    })
