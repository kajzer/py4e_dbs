from twilio.rest import Client

# Enter valid credentails for this code to work.

# Your Account SID from twilio.com/console
account_sid = "enter_acc_sid"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)