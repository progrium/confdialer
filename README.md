# confdailer

## Step 1: Get a Twilio account

Write down your AccountSID and AuthToken.

## Step 2: Make sure you have a number on Twilio

I think they give you one for free.

## Step 3: Dial people into a conference

	curl -u "<account_sid>:<auth_token>" https://confdialer.herokuapp.com/<number_to_dial>