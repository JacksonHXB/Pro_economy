

class Common():
    
    # 处理GDP中原始数据
    @classmethod
    def originDataHandler(cls, country):
        res = {}
        res["title"] = country["title"]
        data = {}
        for (key,value) in country["data"].items():
            val = value.replace(",","")
            LeftIndex = val.find("(")
            RightIndex = val.find(")")
            if value.find("(") != -1:
                value = val[LeftIndex+1 : RightIndex]
            data[key[0:-1]] = value  
        res["data"] = data
        return res










































