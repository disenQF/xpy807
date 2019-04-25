"""
实现api接口服务器
安装依赖包：
1） flask
2)  flaks-blueprint
3)  pymysql
4)  redis
pip install flask flask-blueprint pymysql redis==2.6.1
"""

from app import app
from views import ip_api
from views import teacher_api
from views import log_api

if __name__ == '__main__':
    app.register_blueprint(ip_api.blue)
    app.register_blueprint(teacher_api.blue)
    app.register_blueprint(log_api.blue)

    app.run(host='0.0.0.0')