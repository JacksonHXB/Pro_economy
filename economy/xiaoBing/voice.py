#===============================================================================
# 语音合成和语音识别
#===============================================================================
import json
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus

class Speech(object):
    PER = 4         # 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
    SPD = 6         # 语速，取值0-15，默认为5中语速
    PIT = 5         # 音调，取值0-15，默认为5中语调
    VOL = 5         # 音量，取值0-9，默认为5中音量
    AUE = 6         # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
    API_KEY = 'jonxo7q0KLYsMVeP8EVzeVI9'                # 百度用户应用的相关配置
    SECRET_KEY = 'gvRjX3EZgmLI6wwYNoGCjPK4ujGQ4ioe'     # 百度用户应用的相关配置

#------------------------------------------------------------------------------ 
### 语音合成  ###
    def syntheticSpeech(self, content): # content表示语音合成的内容，返回一个*.mp3的网址请求
        CUID = "123456PYTHON"
        TTS_URL = 'http://tsn.baidu.com/text2audio'         # 语音合成的接口地址
        
        # 校验token
        token = self.fetch_token()
        tex = quote_plus(content)  # 此处content需要两次urlencode
        params = {'tok': token, 'tex': tex, 'per': Speech.PER, 'spd': Speech.SPD, 'pit': Speech.PIT, 'vol': Speech.VOL, 'aue': Speech.AUE, 'cuid': CUID,
                  'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
        data = urlencode(params)
        # 返回一个网址请求，可以直接在网页播放的*.mp3
        return (TTS_URL + '?' + data)
    
#这里可以返回实体的*.mp3的文件
#         FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
#         FORMAT = FORMATS[Speech.AUE]
#         req = Request(TTS_URL, data.encode('utf-8'))
#     
#         has_error = False
#         try:
#             f = urlopen(req)
#             result_str = f.read()
#     
#             has_error = ('Content-Type' not in f.headers.keys() or f.headers['Content-Type'].find('audio/') < 0)
#         except  URLError as err:
#             print('asr http response http code : ' + str(err.code))
#             result_str = err.read()
#             has_error = True
#     
#         save_file = "error.txt" if has_error else 'result.' + FORMAT
#         with open(save_file, 'wb') as of:
#             of.write(result_str)
#     
#         if has_error:
#             result_str = str(result_str, 'utf-8')
#             print("tts api  error:" + result_str)
#     
#         print("result saved as :" + save_file)
    
#------------------------------------------------------------------------------ 
### 语音识别  ###
    def recognitionSpeech(self):
        print("语音识别")
        
            
#------------------------------------------------------------------------------ 
### 百度文字合成语音身份校验  ###
    def fetch_token(self):
        TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
        SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选
        
        params = {
            'grant_type': 'client_credentials',
            'client_id': Speech.API_KEY,
            'client_secret': Speech.SECRET_KEY
        }
        post_data = urlencode(params)
        post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            print('请求失败！')
#             print('请求失败！' + str(err.code))
#             result_str = err.read()
            result_str = ""
        if result_str != "":
            result_str = result_str.decode()
            
            result = json.loads(result_str)
            # 对请求的结果进行处理如果正确则返回access_token
            if ('access_token' in result.keys() and 'scope' in result.keys()):
                if not SCOPE in result['scope'].split(' '):
                    raise DemoError('scope is not correct')
                # print('成功返回token: %s ; 在这世间之后将会失效: %s' % (result['access_token'], result['expires_in']))
                return result['access_token']
            else:
                raise DemoError("或许 API_KEY 或者 SECRET_KEY 不正确，也可能是在获取token的返回值中没有找到 access_token 或者 scope")


#------------------------------------------------------------------------------ 
# 处理语音合成中请求中的错误
class DemoError(Exception):
    pass




































