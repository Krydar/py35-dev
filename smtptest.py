import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
from msvcrt import getche
import sys
from Crypto.Cipher import AES
from Crypto import Random
from io import BytesIO
import base64
import os

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
padding = '{'
pad = lambda s: s + (16 - len(s) % 16) * padding

def DecodeAES(c, e):
    cipher = c
    encoded_string = e
    enc_str = base64.urlsafe_b64decode(encoded_string)
    decrypted_string = cipher.decrypt(enc_str)
    return decrypted_string.decode('utf8').rstrip(padding)

while(auth == False):
    fromaddr = input("Address: ")
    pwd = getpass.getpass('Password: ')
    sav = input("Do you wish to save your password? (1. Yes / 2. No)\n>> ")
    if(sav == '1'):
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        key = os.urandom(16)
        cipher = AES.new(key)
        spwd = EncodeAES(cipher, pwd)
        fpwd = open("data00.pwd", "w").write(str(spwd))
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
print("Message (Press Ctrl+Enter to send):\n>> ")
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

if(sav == 1):
    key = "AESKeyTest"
    getpwd = open("data00.pwd", "r").read()
    print("Password: "+DecodeAES(cipher, spwd))
