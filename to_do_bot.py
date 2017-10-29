"""Flask, Python, Twilio application to test features using Twilio Quest
as a guide."""

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)

to_do = []

@app.route('/')
def hello_world():
    """Simple route that returns 'Hello World'."""

    return 'Hello World! This works, but does the next route...?'


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming texts with phone number's country."""

    # Get information about incoming message body
    msg_request = request.form.get('Body')
    msg_items = msg_request.split(' ')
    action = msg_items[0].lower()

    #Start the TwiML response 
    resp = MessagingResponse()

    full_list = ''

    if action == 'remove':
        remove = int(msg_items[1]) - 1
        if remove <= len(to_do):
            to_do.pop(remove)
    elif action == 'add':
        to_do.append(msg_request[4:])
    elif action == 'list':
        for num, item in enumerate(to_do):
            full_list += '{}. {} \n'.format(num + 1, item)

        resp.message(full_list)

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')