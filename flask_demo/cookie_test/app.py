from flask import Flask, Response

import admin

app = Flask(__name__)

# 配置`SERVER_NAME`，设置主域名
app.config['SERVER_NAME'] = 'example.com:5000'
# 注册蓝图，指定了subdomain
app.register_blueprint(admin.bp)


# @app.route('/index')
# def index():
#     return '通过域名访问！'

@app.route('/')
def set_cookie():
    resp = Response("设置Cookie！")
    # domain设置为 .example.com 是允许 example.com 域名下的各子域名使用该cookie
    resp.set_cookie("username", "zhangsan", domain='.example.com')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
