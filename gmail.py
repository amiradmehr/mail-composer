from email import message
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from helper import *
from time import sleep
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')



class Gmail:

    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

        while True:

            try:
                self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                self.smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                print("Connected successfully")
                break
            except:
                print("\nFaild to connect")
                for i in range(6):
                    sleep(.3)
                    progressBar(i,5)

    def send_email(self, reciever, sender, subject, txt, file):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = reciever
        msg.add_alternative(f""" {txt} """, subtype = 'html')
        
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        try:
            self.smtp.send_message(msg)
            print(f"✅Email sent to {reciever}")
            return True
        except:
            print(f"❌ Failed to send email to {reciever}")
            return False

    def close_gmail(self):
        self.smtp.close()



if __name__ == '__main__':

    amir = Gmail(EMAIL_ADDRESS,EMAIL_PASSWORD)
    txt = "<p>This is in HTML <strong>message</strong></p> <p>also this is next line</p>"
    amir.send_email(EMAIL_ADDRESS,EMAIL_ADDRESS, 'HELLO', txt, 'CV.pdf')
