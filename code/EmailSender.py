import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import make_msgid
from os.path import basename

class EmailSender:
    """ Helper class to send email """
    def __init__(self, ownerEmail, ownerPassword):
        self._ownerEmail = ownerEmail
        self._smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        self._smtpObj.ehlo()
        self._smtpObj.starttls()
        self._smtpObj.login(ownerEmail, ownerPassword)
        
    def sendEmail(self, targetEmail, subject, content, filesToAttach):
        self._internalEmailSender(targetEmail, subject, content, filesToAttach)

    def replayEmail(self, targetEmail, subject, content, filesToAttach, messageId):
        self._internalEmailSender(targetEmail, subject, content, filesToAttach, messageId)

    def _internalEmailSender(self, targetEmail, subject, content, filesToAttach, messageId=None):
        msg = MIMEMultipart()
        msg["Subject"] = Header(subject, "utf-8")
        msg["From"] = self._ownerEmail
        msg["To"] = targetEmail

        msg = self._addOrGenerateMessageId(msg, messageId)

        msg = self._addAttachments(msg, filesToAttach)
        
        _attach = MIMEText(content.encode('utf-8'), 'plain', 'UTF-8')        
        msg.attach(_attach)
        
        self._smtpObj.sendmail(self._ownerEmail, 
                               targetEmail,
                               msg.as_string())

    def _addAttachments(self, msg, filesToAttach):
        for f in filesToAttach:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        return msg

    def _addOrGenerateMessageId(self, msg, messageId):
        if messageId == None:
            msg["Message-ID"]  = make_msgid()
        else:
            msg["In-Reply-To"] = messageId
            msg["References"] = messageId
        return msg

        
    def close(self):
        self._smtpObj.quit()
