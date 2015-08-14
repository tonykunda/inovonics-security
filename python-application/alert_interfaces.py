import smtplib

class Email():
	def __init__(self, host, port, username, password):
		self.username = username
		self.password = password
		self.host = host
		self.port = port

	def sendEmail(self, emailAddress, emailSubject, emailBody):
			session = smtplib.SMTP(self.host, self.port)
			session.ehlo()
			session.starttls()
			session.login(self.username, self.password)
			headers = "\r\n".join(["from: " + self.username,
			                       "subject: " + emailSubject,
			                       "to: " + emailAddress,
			                       "mime-version: 1.0",
			                       "content-type: text/html"])

			# body_of_email can be plaintext or html!                    
			content = headers + "\r\n\r\n" + emailBody
			session.sendmail(self.username, emailAddress, content)
			session.quit()

if __name__ == '__main__':
	print "Sending Test Email"
	email_interface = Email('smtp.gmail.com', 587, 'username', 'password')
	email_interface.sendEmail('9204194318@vtext.com', 'Test', 'This is a test email.')


		