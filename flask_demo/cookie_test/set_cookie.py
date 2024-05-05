from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/")
def set_cookie():
    """
    实例化Response对象时可以传递三个参数：
    1. data：需要响应的数据
    2. status：响应的状态码
        平时我们请求接口的时候，如果成功状态码是200，Flask中这个状态码可以修改，在反爬虫中用处很大，
        如我将成功响应的状态码设置为401，那么其他人爬虫的时候就不会爬虫401返回状态码的数据了。
    3. headers：设置的请求头
    :return:
    """
    resp = Response("设置Cookies")

    resp.status = 401

    # 前两个参数默认传递给key value
    resp.set_cookie("username", "zhangsan", path="/static")
    resp.set_cookie("passwd", "123456", expires="2024-01-01 12:12:12+08:00")

    return resp


@app.route("/get_cookies")
def get_cookies():
    """
    查看cookie
    因为我们设置的key valued的cookie工作子目录为/static，所以在当前目录下的程序，无法获取此cookie，返回None
    :return:
    """
    username = request.cookies.get("username")
    passwd = request.cookies.get("passwd")
    print(username)
    print(passwd)
    return str(username) + ", " + str(passwd)


@app.route("/delete_cookies")
def delete_cookies():
    resp = Response("删除cookie")
    resp.delete_cookie("username", path="/static")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
