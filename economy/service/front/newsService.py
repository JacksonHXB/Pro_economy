from economy.views import viewManager
from flask.globals import current_app  # Flask核心对象
import economy
from bson import json_util


class NewsService:
       
    # 查询最近几日的热点新闻
    @classmethod
    def queryHotNews(cls):
        try:
            query = economy.mongodb.db.tb_news_sina
            res = query.find()
            topNews = []
            for index in range(5):
                item= {} 
                title = res[index]["data"]["detail"]["title"]
                if len(title) > 12 :
                    x = title[:12]+"..."
                item["title"] = x
                item["href"] = res[index]["data"]["detail"]["href"]
                item["time"] = res[index]["data"]["detail"]["time"]
                topNews.append(item)
            return topNews
        except Exception as e:
            return []
        return topNews
       
    # 查询最新的新闻资讯
    @classmethod
    def queryLatestNew(cls):
        try:
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
        except Exception as e:
            return []
        return topNews






















































