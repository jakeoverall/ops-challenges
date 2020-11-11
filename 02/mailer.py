import mailer_config
import smtplib
from email.mime.text import MIMEText

def connect():
    try:
        print(f"LOGGING IN WITH {mailer_config.SENDER_EMAIL}")
        server = smtplib.SMTP(mailer_config.MAIL_SERVER, mailer_config.PORT_NUMBER)
        server.connect(mailer_config.MAIL_SERVER, mailer_config.PORT_NUMBER)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(mailer_config.SENDER_EMAIL, mailer_config.SENDER_PASSWORD)
        return server
    except Exception as err:
        print(str(err))
        raise err


def send(to, message):
    try:
        server = connect()
        msg = MIMEText(message.encode("UTF-8"), 'plain', "UTF-8")
        server.sendmail(mailer_config.SENDER_EMAIL, to, msg.as_string())
        server.close()
        print("Message Successfully Sent")
    except Exception as err:
        print(str(err))
        print('Something went wrong...')