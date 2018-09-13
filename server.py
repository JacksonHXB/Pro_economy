from flask import Flask,render_template
from multiprocessing import Process
import webbrowser as browser
import win32con
import win32api

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/toPage')
def toPage():
    return render_template('index2.html')

def test(url):
    # 打开浏览器并输入网址
    browser.open_new(url)
    # 360极速浏览器全屏
    win32api.keybd_event(122, 0, 0, 0)
    win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    test("http://localhost:5000/")
    app.run()























