# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not Found'})

# @app.errorhandler(404)
# def not_found(error):
#     # return render_template('404.html'), 404
#     flash('404')

@main.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'status': 500})
    