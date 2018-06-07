#coding:utf-8

"""
app.py
应用入口文件
"""

import urllib
from rmon.app import create_app
from rmon.models import db

app = create_app()

@app.cli.command()
def init_db():
    """
    数据库初始化
    """
    print("sqlite3 database file is %s"%app.config['SQLALCHEMY_DATABASE_UI'])
    db.create_all()
