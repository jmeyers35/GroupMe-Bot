# GroupMe Markov Chain Bot

A simple Flask app defined in app.py that uses [markovify](https://github.com/jsvine/markovify) to 
generate sentences meant to imitate a particular person in a GroupMe group chat.

When a message is sent in the GroupMe chat, the message is sent to this service. If 
the message is of the form "\[Bot\] \<name>", the service parses out the name, finds the appropriate model,
and sends the message back to the chat.

The JSON serialized Markovify models are read from a MongoDB database.

The corpi were generated using a [custom GroupMe API wrapper](https://github.com/jmeyers35/GroupMe-Utils) I wrote.