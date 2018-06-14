# -*- coding: utf-8 -*-
from . import main
from flask import jsonify

@main.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not FOund'})

# @app.errorhandler(404)
# def not_found(error):
#     # return render_template('404.html'), 404
#     flash('404')

@main.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'status': 500})