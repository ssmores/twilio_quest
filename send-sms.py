"""Small program that sent a specific message for Twilio Quest."""


from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']

auth_token = os.environ['TWILIO_AUTH_TOKEN']

my_num = os.environ['TWILIO_PHONE_NUM']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12092104311", 
    from_=my_num,
    body="Greetings! The current time is: 16:17 on Oct 26, 2017 G97EMODD6UNX4YQ")

print(message.sid)