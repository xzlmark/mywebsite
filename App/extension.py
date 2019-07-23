from flask_bootstrap import Bootstrap


def init_ext(app):

    # 初始化bootstrap对象，不需要在其他地方设置
    Bootstrap(app)

