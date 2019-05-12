# GroupMe Markov Chain Bot

A simple Flask app defined in app.py that uses [markovify](https://github.com/jsvine/markovify) to 
generate sentences meant to imitate a particular person in a GroupMe group chat.

The serialized markovify models are in the models directory. These models were created with
`create_models.py`. `create_models.py` expects a directory containing .txt files of the form
person_name_messages.txt. The particular models I used are shown, but you can use create_models to
create models based on your own corpi. The Flask app expects the models to be in a directory called 'models'.