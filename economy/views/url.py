#===============================================================================
# 系统架构测试
#===============================================================================
from flask import jsonify, request, render_template,flash
from . import viewManager
import json
from economy.xiaoBing.voice import Speech


speech = Speech()
def speak(str):
    xiaoBing = speech.syntheticSpeech(str) 
    return xiaoBing


# 主页
@viewManager.route('/')
def index():
#     xiaoBing = speech.syntheticSpeech("主人，你终于来到经济系统了！这里有有关经济的一切，您有什么需要尽管跟我说。") 
    xiaoBing = None
    data = {"xiaoBing":xiaoBing}
    return render_template("front/index.html", data=data)

# 宏观经济数据
@viewManager.route("/macroData")
def toMacroData():
#     xiaoBing = speech.syntheticSpeech("宏观经济数据正在加载中.....")
#     data = {"xiaoBing":xiaoBing}
    data = {}
    return render_template("front/macroData/macroData.html", data=data)


@viewManager.route("/toXiaoBing", methods=['POST'])
def toXiaoBing():
    if request.method == 'POST':
        data = json.loads(request.get_data().decode("UTF-8"))
        res = None
        if data["flag"] == "macroData":
#             xiaoBing =speak("今年国家的数据比较良好，目前市场趋于稳定，建议购买一点国债！")
            res = {}
#             res = {"data": xiaoBing}
    return json.dumps(res)


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



































































