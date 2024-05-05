"""
pip install flask
pip install flask-login
pip install flask-sqlalchemy
"""
from flask import Flask, render_template

from user_blueprint import login_required_with_level
import config
from flask_sqlalchemy import SQLAlchemy

user = Flask(__name__)
user.config.from_object(config)

db =SQLAlchemy(user)



# 显示所有用户列表
@user.route('/dispalluser/')
@login_required_with_level([1, 2, 3, 4])
def dispalluser():
    return render_template('dispalluser.html', users=selectAll())


# 新增用户
@user.route('/newuser/', methods=['GET', 'POST'])
@login_required_with_level([1])
def newuser():
    ...


# 修改用户
@user.route('/modifyuser/<userid>/', methods=['GET', 'POST'])
@login_required_with_level([1])
def modifyuser(userid):
    ...


# 删除用户
@user.route('/deleteuser/<userid>', methods=['GET', 'POST'])
@login_required_with_level([1])
def deleteuser(userid):
    ...
