# Using 'twilio'. They providing API for communications to connect you with customers.

# 1: Create TWILIO account

# 2: pip install twilio

# class Client() - represents client in twilio REST API
from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

# Took this data in twilio account


# Create instance based on the Clien class with two required arguments
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# This objects has a few useful artibutes with useful methods
call = client.messages.create(
    to='Number',
    from_='Twilio Number',
    body='Message Text'
)

# This "call" obj has a lots of atributes
# call.date_created ...
