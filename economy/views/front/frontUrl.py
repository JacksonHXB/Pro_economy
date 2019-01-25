#===============================================================================
# 前端的URL管理
#===============================================================================
from flask import jsonify, request, render_template,flash
from economy.views import viewManager
import json
from economy.service.front.newsService import NewsService


# 工作台
@viewManager.route("/index")
def toWorkspace():
    return render_template("front/index/index.html")

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
    data["topNews"] = NewsService.queryNews(20, 1) # 查询最新5条的新浪新闻
    return render_template("front/info/info_index.html", data=data)

# 跳转后台
@viewManager.route('/toBackIndex')
def toBackIndex():
    return render_template("back/index.html")

# 跳转后台登录 /*登录以后会拦截*/
@viewManager.route('/toBackLogin')
def toBackLogin():
    return render_template("back/login.html")


@viewManager.route('/index/news/topNews')
def getTopNews():
    # 获取最近的热点新闻
    topNews = NewsService.queryHotNews()
    return json_util.dumps(topNews)


@viewManager.route('/index/news/latest', methods=["GET"])
def getLatestNew():
    
    
    
    return json_util.dumps("")































































