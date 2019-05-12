from flask import Flask, request
import json
import markovify
import os
import requests

app = Flask(__name__)
MAX_OVERLAP_RATIO = 0.4
MAX_OVERLAP_TOTAL=10

@app.route('/', methods=['POST'])
def web_hook():
    message_text = request.get_json()['text']
    if message_text.startswith('[Sim]'):
        person = message_text.split('[Sim]')[1].lower().replace(" ", "")
        if person == 'anthony':
            with open('models/anthony_barnum_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Anthony bot says: " + msg)
        elif person == 'chase' or person == 'eric':
            with open('models/chase_m_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Chase bot says: " + msg)
        elif person == 'chris' or person ==  'christopher':
            with open('models/christopher_densmore_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Chris bot says: " + msg)
        elif person == 'jack':
            with open('models/jack_maher_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Jack bot says: " + msg)
        elif person == 'johnny':
            with open('models/johnny_chiles_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Johnny bot says: " + msg)
        elif person == 'lanier':
            with open('models/lanier_freeman_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Lanier bot says: " + msg)
        elif person == 'ryan':
            with open('models/ryan_yeung_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Ryan bot says: " + msg)
        elif person == 'yash' or person == 'qb1':
            with open('models/yash_punjabi_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Yash bot says: " + msg)
        elif person == 'jacob':
            with open('models/jacob_meyers_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_sentence(tries=1000, max_overlap_ratio=MAX_OVERLAP_RATIO, max_overlap_total=MAX_OVERLAP_TOTAL)
                send_message("Jacob bot says: " + msg)
        else:
            send_message("Sorry! I don't recognize that name.")
    return "ok", 200
    

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        "bot_id" : os.getenv("BOT_ID"),
        "text" : msg
    }

    requests.post(url, data=data)