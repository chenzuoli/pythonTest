# -*- coding: utf8 -*-

from functools import wraps

from flask import redirect, url_for, flash
from flask_login import current_user, login_required


def login_required_with_level(levels):
    """登录等级描述符"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                if int(current_user.level) in levels:
                    return func(*args, **kwargs)

            flash("您无权访问此页面。")
            return redirect(url_for("user.index"))

        return login_required(wrapper)

    return decorator
