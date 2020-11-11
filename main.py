import smtplib
import time
from urllib.request import Request, urlopen

#Setup
ADDRESS  = "shamustch@gmail.com"
PWD    = "viyqxenrwxudsbgb"
#Send mail
def send_email(to, message):
    #Login
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(ADDRESS, PWD)
    sent_from = ADDRESS
    to = ["shamustch@gmail.com"]
    message = """\
Subject: Server Status

This message is sent from Python."""
    server.sendmail(sent_from, to, message)
    server.close()
while True:

    time.sleep(10)