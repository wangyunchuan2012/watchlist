from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/home')
def home_page():
    return 'hello, this is home page!'


@app.route('/user/<name>')
def user_page(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.route('/test')
def test_url_for():
    print(url_for('home_page'))  # 输出：/ # 注意下面两个调用是如何生成包含 URL 变量的 URL 的

    print(url_for('user_page', name='wayne'))  # 输出：/user/wayne

    print(url_for('user_page', name='wangyunchuan'))  # 输出：/user/wangyunchuan

    print(url_for('test_url_for'))  # 输出：/test # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。

    print(url_for('test_url_for', num=2))  # 输出：/test?num=2

    return 'Test page'
