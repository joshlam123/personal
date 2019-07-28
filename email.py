import smtplib, ssl

port = 465
smtp_server = "smtp@gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type in your password here: \n")
message = """\

Subject: Hi There

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
