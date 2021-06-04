#  Lines of code for sending email automation
# import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('ericscorpio1@gmail.com', '')
# server.sendmail('ericscorpio1@gmail.com', 'E.Fonseca19@outlook.com',
#                 'This is a test of a email script on python')

# -------------------- New Code
# Slow bot but can be worked on to assist in email dictation & expedite work flow
# First email project
# Install pip speech recognition
# Install pyAudio
# Install pyttsx3

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
# initialize the pyttsx3 feature
engine = pyttsx3.init()


def talk(text):
    """ Function controls the pyttsx3 talking conversion"""
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('ericscorpio1@gmail.com', 'Sender_Email_Password')
    # Connects the email message imported

    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'cale': 'cale.anderson@sunrun.com',
    'eric': 'E.Fonseca19@outlook.com',
    'rudy': 'rudy.gaytan@sunrun.com',
    'Lourdes': 'Lourdesk.14@gmail.com',

}


def get_email_info():
    """Initiates and controls the flow of input & output between Bot and yourself"""
    talk('Who are we sending an email to?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('I am ready to dictate your email proceed slowly')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. I sent your email haha')
    talk('Are we sending more?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        print('Goodbye')


get_email_info()
