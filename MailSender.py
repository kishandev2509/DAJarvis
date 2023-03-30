import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testingemail2593@gmail.com',  os.environ['TMP'])
    server.sendmail('testingemail2593@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    sendEmail('kishandevprajapati4@gmail.com', 'test')