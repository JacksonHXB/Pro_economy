#===============================================================================
# 宏观经济数据处理
#===============================================================================
from flask import jsonify, request, render_template,flash
from economy.views import viewManager
from flask.globals import current_app  # Flask核心对象
import economy
from bson import json_util
from economy.utils.common import Common


query = None

# 宏观经济数据
@viewManager.route("/macroData/gdps/countries")
def queryCountries():
    query = economy.mongodb.db.tb_gdp
    res = query.find({},{"title":1})# 查询所有国家
    return render_template("/front/macroData/macroData.html", res=res)


# 根据国家查询GDP数据
@viewManager.route("/macroData/gdps/countries/<countryName>", methods=['GET'])
def queryCountryByName(countryName):
    query = economy.mongodb.db.tb_gdp
    country = query.find_one({"title":countryName})
    country = Common.originDataHandler(country)
    return json_util.dumps(country)  # 序列化对象


# 跳转到宏观经济查询页面
@viewManager.route("/macroData/toGdp")
def toGdp():
    return render_template('/front/macroData/gdp.html')






























































