#===============================================================================
# 项目初始化
#===============================================================================
from flask import Flask
from economy.views import viewManager 
from flask_pymongo import PyMongo

# 初始化PyMongo
mongodb = PyMongo()

# 初始化系统
def initSystem():
    global mongodb
    
    # 初始化Flask对象
    sys = Flask(__name__)
    # 注册配置文件
    sys.config.from_object('economy.secure')    
    sys.config.from_object('economy.setting') 
    
    # 注册蓝图管理路由系统
    sys.register_blueprint(viewManager) 
    
    # 注册MongoDB
    sys.config["MONGO_URI"] = 'mongodb://192.168.0.180:27017/db_finance'
    
    mongodb.init_app(sys)
    
    # 使用进程打开窗口，向用户展示
    return sys














































































