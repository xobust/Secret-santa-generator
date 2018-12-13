import smtplib
import sys
from random import shuffle
server = smtplib.SMTP('smtp.gmail.com:587') #Mailserver
server.starttls()

#Next, log in to the server
server.login("name@gmail.com", "password/app-password")


Personer = [ 
        ("Name", "email@gmail.com"), 
        ("John Smith", "john@smith.com")
]

shuffle(Personer)

to_send = []

#Send the mail
for (fran, email),(to, _) in zip(Personer, Personer[1:]+Personer[:1]):
    msg = """Subject: Tomtemail!

    Hej {namn}!
    Du är hemlig tomte för {mottagare}.  

    MVH Tomten""".format(namn = fran,
                         mottagare = to).encode("utf-8")

    #print(email)
    #print(msg)
    to_send.append((email, msg))


input("Press Enter to send mails...")

for email, msg in to_send:
    m = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8')
    m['Subject'] = Header("Tomtemail", 'utf-8')
    server.sendmail("tomten@gmail.com", email, m)

