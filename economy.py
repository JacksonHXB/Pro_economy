#===============================================================================
# Flask服务器
#===============================================================================
from economy import initSystem
import threading
import webbrowser as browser
import win32con
import win32api
import threading
import time
from urllib import request

__author__ = '黄小兵'


# 初始化系统
economy = initSystem()
   
def open_browser():
    print('服务器正在启动')
    while True:
        try:
            request.urlopen(url=economy.config['URL'])
            break
        except Exception as e:
            print(e)
            time.sleep(0.5)
    print('服务器启动成功！')
    isOpen = browser.open(economy.config['URL'], autoraise=False)
    if isOpen:
        # 360极速浏览器全屏
        win32api.keybd_event(122, 0, 0, 0)
        win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)
        

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    economy.run(host=economy.config['HOST'], port=economy.config['PORT'], debug=economy.config['DEBUG'], threaded=True)
    























