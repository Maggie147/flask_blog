# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment  # 本地化日期和时间(Flask-Moment 把moment.js[浏览器中渲染日期和时间] 集成到 Jinja2 模板中)
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
pagedown = PageDown()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # session_protection: None , 'basic', 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    # 创建项目对象
    app = Flask(__name__)

    # 加载配置文件内容
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # from .models import User
    # from .models import Role

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
