import requests
from flask import Blueprint,render_template

blue = Blueprint('first_blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    url = 'https://www.anyknew.com/api/v1/sites/zhihu'
    response = requests.get(url)
    infos = response.json()
    # datas=[]
    # for info in infos['data']['site']['subs']:
    #     for i in info['items']:
    #
    # for info in infos['data']['site']['subs']:
    #     datas = info
    return render_template('index.html', infos=infos)


@blue.route('/test/')
def test():

    return render_template('test.html')