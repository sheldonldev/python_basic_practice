import smtplib
from config import Config
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# MORE INFO: https://geekflare.com/send-gmail-in-python/


# @outlook.com
class Mail:
    def __init__(self):
        self.account = Config.OFFICE_ACCOUNT
        self.password = Config.OFFICE_APP_PASSWORD

    def smtp_control(self, send):
        def sender(*args):
            server = smtplib.SMTP('outlook.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.account, self.password)
            res = send(server, args[0], args[1])
            server.quit()
            return res
        return sender

    @smtp_control
    def send_email(self, server, receivers, content):
        results = []
        for receiver in receivers:
            result = server.sendmail(self.account, receiver, content)
            results.append(result)
        return results


mail = Mail()
mail.send_mail(['xiadanli0320@gmail.com'], 'Subject: test\nhello world')
