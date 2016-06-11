import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
from msvcrt import getche
import sys

print("Connecting to GMail...")
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
except Exception:
    print("Couldn't connect to server.")
    quit()
print("Connected.")

server.ehlo()
server.starttls()
server.ehlo()
auth = False
while(auth == False):
    fromaddr = input("Address: ")
    pwd = getpass.getpass('Password: ')
    print("Logging in... ("+fromaddr+")")
    try:
        server.login(fromaddr, pwd)
        auth = True
    except smtplib.SMTPAuthenticationError:
        print("Error: Invalid username or password.")
        auth = False


print("Login successful.")
toaddr = input("To: ")
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input("Subject: ")
message = ""
swb = False
swi = False
print("Message (Press Ctrl+Enter to send:\n>> ")
while(True):
    bf = ord(getche())
    if(bf == 13):
        message += "<br>"
        print("")
    else:
        message += chr(bf)
    if(bf == 10):
        break
    if(bf == 8):
        message = message[:-1]
        sys.stdout.write("\b")
        sys.stdout.write(" ")
        sys.stdout.write("\b")
    """if(bf == 13):
        message += "<br>"
        print("\n")
    if(bf == 2 and swb == False):
        message += "<b>"
        sw = True
    elif(bf == 2 and swb == True):
        message += "</b>"
        sw = False
    if(bf == 9 and swi == False):
        message += "<i>"
        swi = True
    elif(bf == 9 and swi == True):
        message += "</i>"
        swi = False
    if(bf == 10):
        break
    else:
        message += chr(bf)
"""

msg.attach(MIMEText(message, 'html'))

text = msg.as_string()

try:
    server.sendmail(fromaddr, toaddr, text)
    print("E-mail sent to "+toaddr+".")
except Exception:
    print("Couldn't send e-mail.")

