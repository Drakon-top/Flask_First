from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    _list = [
        "Человечество вырастает из детства.", "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"
    ]
    return '</br>'.join(_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css"/>
                      </head>
                      <body>
                        <h1 class="im_mar">Привет, Марс!</h1>
                        <div>
                          <img src="{url_for('static', filename='img/mars_image.png')}" width='136' height='136'>
                          <p>Жди нас, Марс!</p>
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')