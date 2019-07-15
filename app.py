from flask import Flask, request
from flask_pymongo import PyMongo
import json
import markovify
import os
import requests

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv()
mongo = PyMongo(app)
MAX_OVERLAP_RATIO = 0.4
MAX_OVERLAP_TOTAL=10

@app.route('/', methods=['POST'])
def web_hook():
    message_text = request.get_json()['text']
    if message_text.startswith('[Bot]'):
        person = message_text.split('[Bot]')[1].lower().replace(' ', '')
        if person == 'anthony':
            text_model = get_model('anthony')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Anthony bot says: ' + msg)
        elif person == 'chase' or person == 'eric':
            text_model = get_model('chase')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Chase bot says: ' + msg)
        elif person == 'chris' or person ==  'christopher':
            text_model = get_model('chris')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Chris bot says: ' + msg)
        elif person == 'jack':
            text_model = get_model('jack')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Jack bot says: ' + msg)
        elif person == 'johnny':
            text_model = get_model('johnny')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Johnny bot says: ' + msg)
        elif person == 'lanier':
            text_model = get_model('lanier')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Lanier bot says: ' + msg)
        elif person == 'ryan':
            text_model = get_model('ryan')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Ryan bot says: ' + msg)
        elif person == 'yash' or person == 'qb1':
            text_model = get_model('yash')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Yash bot says: ' + msg)
        elif person == 'jacob':
            text_model = get_model('jacob')
            msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
            send_message('Jacob bot says: ' + msg)
        else:
            send_message("Sorry! I don't recognize that name.")
    return 'ok', 200
    

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        "bot_id" : os.getenv("BOT_ID"),
        "text" : msg
    }
    requests.post(url, data=data)

def get_model(name):
    model = mongo.db.models.find_one({'name': name})
    return markovify.NewlineText.from_json(model['model'])