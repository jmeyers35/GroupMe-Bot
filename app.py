from flask import Flask, request
from flask_pymongo import PyMongo
import json
import markovify
import os
import random
import requests

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
MAX_OVERLAP_RATIO = 0.4
MAX_OVERLAP_TOTAL=10

BLOOMBERG_QUOTES = [
    "Mike will get it done.", 
    "Mike Bloomberg started as a middle class kid who worked his way through college.",
    "Today, Bloomberg LP employs some 20,000 talented and creative people who share Mike’s passion for innovation and customer service.",
    "In 2001, just weeks after the terrorist attacks of 9/11, Mike Bloomberg was elected mayor of New York City in his first run for public office.",
    "Mike gave $1.8 billion to his alma mater Johns Hopkins to forever guarantee need-blind admissions for all students.",
    "Talk is cheap. As an entrepreneur, mayor, and problem-solving philanthropist, Mike has taken on the toughest challenges and gotten big things done.",
    "As president, Mike will continue putting progress ahead of partisanship – and he will unite the country around a bold and achievable agenda."
]

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
        elif person == 'maddie':
            msg = BLOOMBERG_QUOTES[random.randrange(0, len(BLOOMBERG_QUOTES))]
            send_message('Maddie bot says: ' + msg)
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