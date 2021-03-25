import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet"
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                      crossorigin="anonymous">
                       <title>Привет, Яндекс!</title>
                     </head>
                     <body>
                       <h1>Привет, Яндекс!</h1>
                       <img src="static/img/fon.jpg" alt="">
                     </body>
                   </html>'''

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run(host="127.0.0.1", port="5000")