#===============================================================================
# 系统架构测试
#===============================================================================
from flask import jsonify, request, render_template,flash
from . import viewManager

# 主页
@viewManager.route('/')
def index():
    return render_template("front/index.html")

# 跳转后台
@viewManager.route('/toBackIndex')
def toBackIndex():
    return render_template("back/index.html")

# 跳转资讯系统
@viewManager.route('/toBackInfo')
def toBackInfo():
    return render_template("back/info/info_index.html")

# 跳转后台登录
@viewManager.route('/toBackLogin')
def toBackLogin():
    return render_template("back/login.html")



































































