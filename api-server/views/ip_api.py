from flask import Blueprint, jsonify
from flask import request

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