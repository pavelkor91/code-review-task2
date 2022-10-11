from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import traceback
import jsonschema
from jsonschema import validate

import json

PASSWORD = 'test'
HOST = 'smtp.freesmtpservers.com'
PORT = 25 
FROM = 'urcoderev@testing.ru'

dataSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"description": "Email of the user", 
                    "type": "string",
                    "pattern": "^\\S+@\\S+\\.\\S+$",
                    "minLength": 6,
                    "maxLength": 127,
                    "format": "email"
                    },
        "result": {"type": "number"},
    },
}

def validate_json(data: json) -> bool:

    try:
        validate(instance=data, schema=dataSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def send_email(data: json) -> bool:

    if validate_json(data):
        message  = f"Привет, {data['name']},  твой результат: {data['result']}"
        msg = MIMEMultipart()
        msg['From'] = FROM
        msg['To'] = data['email']
        msg['Subject'] = "Testing"
        msg.attach(MIMEText(message, 'plain'))

        try:
            smtpObj = smtplib.SMTP(HOST, PORT)
            smtpObj.sendmail( msg['From'], msg['To'], msg.as_string())
        except Exception as e:
            print(traceback.format_exc())

    else:
        print('JSON данные не валидны!')
    

if __name__ == "__main__":
    jsonData = json.loads('{"name": "jane doe", "email": "25", "result": 72}')
    send_email(jsonData)
    jsonData = json.loads('{"name": "Артем", "email": "test@test.ru", "result": 65.6}')
    send_email(jsonData)
