from email import message
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from helper import *
from time import sleep
load_dotenv()




class Gmail:

    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

        while True:

            try:
                self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                self.smtp.login(self.email_address, self.password)
                print("Connected to GMAIL successfully")
                break
            except:
                print("\nFaild to connect to GMAIL")
                for i in range(6):
                    sleep(.5)
                    progressBar(i,5)

    def send_email(self, reciever, sender, subject, txt, file):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = reciever
        msg.add_alternative(f'{txt}', subtype = 'html')
        
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        try:
            self.smtp.send_message(msg)
            print(f"✅ Email sent to {reciever}")
            return True
        except:
            print(f"❌ Failed to send email to {reciever}")
            return False

    def close_gmail(self):
        self.smtp.close()



# amir = Gmail(EMAIL_ADDRESS,EMAIL_PASSWORD)
# prof = 'amir'
# paper = 'control'
# txt = f'''
# <p><span style="font-family: Verdana, Geneva, sans-serif;">Hi professor {prof}</span></p>
# <p><span style="font-family: Verdana, Geneva, sans-serif;">This is amir</span></p>
# <p><span style="font-family: Verdana, Geneva, sans-serif;">I love your paper about {paper}</span></p>
# '''
# from templates import Templates
# mytemp = Templates()
# txt = mytemp.get(1,'Asghar', 'Robotics', 'Agile')
# amir.send_email(EMAIL_ADDRESS,EMAIL_ADDRESS, 'HELLO', txt, 'CV.pdf')
