import smtplib

email = input("SENDER EMALI: ")
receiver_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"{subject} \n\n {message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email,"qygfkimkjkuytmlq")

server.sendmail(email,receiver_email,text)

print("Email has been sent to "+ receiver_email)