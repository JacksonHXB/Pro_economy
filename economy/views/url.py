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


    data = {}
    return render_template("front/index.html",data=data)


# 语音小冰
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




































































