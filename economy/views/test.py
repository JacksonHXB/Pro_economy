#===============================================================================
# 系统架构测试
#===============================================================================
from flask import jsonify, request, render_template,flash
from . import viewManager


# 测试
@viewManager.route('/test')
def test():
    print("特特特")
    return render_template("test.html")





































































