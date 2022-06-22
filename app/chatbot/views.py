# coding = utf-8
"""
@author: zhou
@time:2019/6/25 20:09
"""
import os

from chatterbot import ChatBot
from flask import render_template, request, jsonify
from . import chatbot
from .. import config

config_name = os.getenv("FLASK_CONFIG") or "default"
bot = ChatBot("my-chat", database_uri=config[config_name].SQLALCHEMY_DATABASE_URI)


@chatbot.route("/")
def home():
    return render_template("index.html")


@chatbot.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(bot.get_response(userText))


@chatbot.route("/api/chat/<text>")
def get_bot_api(text):
    res = str(bot.get_response(text))
    return jsonify(res), 200


def get_bot_text(text):
    res = str(bot.get_response(text))
    return res
