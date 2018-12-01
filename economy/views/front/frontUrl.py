#===============================================================================
# 前端的URL管理
#===============================================================================
from flask import jsonify, request, render_template,flash
from economy.views import viewManager
import json

# 宏观经济数据
@viewManager.route("/macroData")
def toMacroData():
#     xiaoBing = speech.syntheticSpeech("宏观经济数据正在加载中.....")
#     data = {"xiaoBing":xiaoBing}
    data = {}
    return render_template("front/macroData/macroData.html", data=data)

# 资讯数据
@viewManager.route("/info")
def toInfo():
    data = {}
    return render_template("front/info/info.html", data=data)

# 跳转后台
@viewManager.route('/toBackIndex')
def toBackIndex():
    return render_template("back/index.html")

# 跳转后台登录 /*登录以后会拦截*/
@viewManager.route('/toBackLogin')
def toBackLogin():
    return render_template("back/login.html")
































































