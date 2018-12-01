from economy.views import viewManager
from flask.globals import current_app  # Flask核心对象
import economy
from bson import json_util


class Service:
       
    # 查询最近几日的热点新闻
    @classmethod
    def queryHotNews(cls):
        query = economy.mongodb.db.tb_news_sina
        res = query.find()
        topNews = []
        for index in range(5):
            item= {} 
            item["title"] = res[index]["data"]["detail"]["title"]
            item["href"] = res[index]["data"]["detail"]["href"]
            item["time"] = res[index]["data"]["detail"]["time"]
            topNews.append(item)
        return topNews






















































