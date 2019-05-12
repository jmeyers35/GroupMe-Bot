from flask import Flask, request
import json
import markovify
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def web_hook():
    message_text = request.get_json()['text']
    if message_text.startswith('[Sim]'):
        person = message_text.split('[Sim]')[0].lower()
        if person == 'anthony':
            with open('models/anthony_barnum_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'chase' or 'eric':
            with open('models/chase_m_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'chris' or 'christopher':
            with open('models/christopher_densmore_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'jack':
            with open('models/jack_maher_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'johnny':
            with open('models/johnny_chiles_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'lanier':
            with open('models/lanier_freeman_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'ryan':
            with open('models/ryan_yeung_model.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        elif person == 'yash':
            with open('models/yash_punjabi.json') as f:
                model_json = json.load(f)
                text_model = markovify.NewlineText.from_json(model_json)
                msg = text_model.make_short_sentence(140, tries=1000, max_overlap_ratio=0.5, max_overlap_total=10)
                send_message(msg)
        else:
            send_message("Sorry! I don't recognize that name.")
    return "ok", 200
    

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/pos'

    data = {
        "bot_id" : os.getenv("BOT_ID"),
        "text" : msg
    }

    requests.post(url, data=data)