import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='deepasomu28@gmail.com',
    to_emails='sowmiyasivakalpana@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)