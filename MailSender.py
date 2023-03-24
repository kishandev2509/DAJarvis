import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('datinderjeets@gmail.com', 'Jarvis@07')
    server.sendmail('datinderjeets@gmail.com', to, content)
    server.close()