from decouple import AutoConfig
config = AutoConfig(search_path='./')

MAIL_SERVER = "smtp.gmail.com"
PORT_NUMBER =  587
SENDER_EMAIL = config("email")
SENDER_PASSWORD = config("password")