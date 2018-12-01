#===============================================================================
# 蓝图初始化
#===============================================================================
from flask import Blueprint, render_template

# 蓝图blueprint:用于解决视图函数与app的绑定问题,用一个蓝图管理多个不同的视图函数
viewManager = Blueprint('viewManager', __name__)
# web = Blueprint('web', __name__, template_folder='templates')# 这里的蓝图也可以注册静态文件static_folder='', static_url_path=''

#-- 分别导入蓝图管理的所有视图函数文件 ---------------------------------------------------------------------------- 
from economy.views import url


# 导入macroData的路由
from economy.views.front import frontUrl
from economy.views.front.macroData import macroData
from economy.views.front.info import info



#----- 后台URL管理 ------------------------------------------------------------------------- 
from economy.views.back import backUrl
from economy.views.back.info import info













































































































