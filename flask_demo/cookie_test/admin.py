from flask import Blueprint, request

bp = Blueprint('admin', __name__, subdomain='admin')


# @bp.route('/ad')
# def admin():
#     return 'Admin Page'

@bp.route('/')
def get_cookie():
    username = request.cookies.get('username')
    # 如果前一个对象为None，则将后一个对象作为响应
    return username or '没有获取到name值'
