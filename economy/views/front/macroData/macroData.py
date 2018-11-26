#===============================================================================
# 宏观经济数据处理
#===============================================================================
from flask import jsonify, request, render_template,flash
from economy.views import viewManager
from flask.globals import current_app  # Flask核心对象
import economy

# 宏观经济数据
@viewManager.route("/macroData/gdps/countries")
def queryCountries():
    print(type(economy.mongodb.db.tb_gdp.find_one()))
    
    
    
    return ""

































































