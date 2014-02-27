import os
import twilio.rest
from flask import Flask, request

app = Flask(__name__)

@app.route('/<dial_number>')
def dial(dial_number):
    client = twilio.rest.TwilioRestClient(request.authorization.username, request.authorization.password)
    numbers = client.phone_numbers.list()
    if not numbers:
        return "no number to call from"
    c = client.calls.create(
        to=dial_number, 
        from_=numbers[0].phone_number, 
        url="http://twimlets.com/conference?Name=confdial&Message=.", if_machine="Hangup")
    return c.status