#===============================================================================
# 项目初始化
#===============================================================================
from flask import Flask
from economy.views import viewManager 
# 初始化系统
def initSystem():
    # 初始化Flask对象
    sys = Flask(__name__)
    # 注册配置文件
    sys.config.from_object('economy.secure')    
    sys.config.from_object('economy.setting')    
    # 注册蓝图管理路由系统
    sys.register_blueprint(viewManager)
    # 使用进程打开窗口，向用户展示
    return sys
    















































































