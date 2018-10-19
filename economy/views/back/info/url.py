#===============================================================================
# 系统架构测试
#===============================================================================
from flask import jsonify, request, render_template,flash
from . import viewManager


# 主页
@viewManager.route('/')
def index():
    return render_template("index.html")

# 跳转后台
@viewManager.route('/toBackIndex')
def toBackIndex():
    return render_template("back/back_index.html")






































































