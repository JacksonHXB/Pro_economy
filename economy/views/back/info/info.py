#===============================================================================
# info模块的URL管理
#===============================================================================
from flask import jsonify, request, render_template,flash
from economy.views import viewManager
from bson import json_util
import economy
# 
# 
# # 主页
# @viewManager.route('/')
# def index():
#     return render_template("index.html")
# 
# # 跳转后台
# @viewManager.route('/toBackIndex')
# def toBackIndex():
#     return render_template("back/back_index.html")
# 
# 
# # 跳转后台登录
# @viewManager.route('/toBackLogin')
# def toBackLogin():
#     return render_template("back/back_login.html")

# 热点资讯
@viewManager.route('/back/info/hotNews')
def toHotNews():
    return render_template("back/info/hotNews.html")


# 管理新浪热点新闻
@viewManager.route('/back/info/hotNews/<keyword>', methods=['POST'])
def querySinaHotNews(keyword):
    db = economy.mongodb.db
    
    arr = []
    if keyword == "sina": # 当关键字为新浪时搜索新浪热点资讯
        hotNews = db.tb_news_sina.find({"title":"hotNews_sina"})
        for hotNew in hotNews:
            item = {}
            data = hotNew["data"]["detail"]
            item["title"] = data["title"]
            item["time"] = data["time"]
            item["href"] = data["href"]
            item["type"] = hotNew["data"]["title"]
            arr.append(item)    
    return json_util.dumps(arr)



# @viewManager.route("/macroData/gdps/countries")
# def queryCountries():
#     query = economy.mongodb.db.tb_gdp
#     res = query.find({},{"title":1})# 查询所有国家
#     return render_template("/front/macroData/macroData.html", res=res)
# 
# 
# # 根据国家查询GDP数据
# @viewManager.route("/macroData/gdps/countries/<countryName>", methods=['GET'])
# def queryCountryByName(countryName):
#     query = economy.mongodb.db.tb_gdp
#     country = query.find_one({"title":countryName})
#     country = Common.originDataHandler(country)
#     return json_util.dumps(country)  # 序列化对象


























































