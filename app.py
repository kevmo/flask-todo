from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/.htaccess')
def htaccess():
    return app.send_static_file('.htaccess')



if __name__ == '__main__':
    app.run()