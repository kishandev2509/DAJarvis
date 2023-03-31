import smtplib
import os

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.environ['UMAIL'],  os.environ['NTMP'])
    server.sendmail(os.environ['UMAIL'], to, content)
    server.close()

if __name__ == "__main__":
    sendEmail('kishandevprajapati4@gmail.com', 'how are you')