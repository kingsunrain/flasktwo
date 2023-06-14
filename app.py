#!/usb/bin/env python3
# -*- coding=utf-8 -*-
#fdsdfffcds


from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#    return render_template(index.html)

@app.route("/")  # 使用Flask的 app.route 装饰器将URL路由映射到该函数：
def index():
    # render_template("index.html")      # "Hello, Flask!"
    return "Hello, 5555444215Flask!"


@app.route("/about")
def about():
    return "Hello, Flask!"         # render_template("about.html")


if __name__ == '__main__':
    # app.run
    app.run(host='0.0.0.0',port='8090')
# dfaf
