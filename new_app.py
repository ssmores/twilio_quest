"""Flask, Python, Twilio application to test features using Twilio Quest
as a guide."""

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Simple route that returns 'Hello World'."""

    return 'Hello World! This works, but does the next route...?'


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming texts with phone number's country."""

    # Get information about incoming phone number.
    number = request.form.get("FromCountry")

    #Start the TwiML response 
    resp = MessagingResponse()

    #Add a message
    resp.message('Hi! It looks like your phone number was born in {}'.format(number))

    print number
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')