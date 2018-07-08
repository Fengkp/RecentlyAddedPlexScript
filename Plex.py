import smtplib
import getpass
import re
from plexapi.myplex import MyPlexAccount

def formatSearchStr(toFormat):
    firstFormat = re.sub(r'.*:', '', toFormat)
    secondFormat = re.sub(r'>.', '', firstFormat)
    print (secondFormat)
    return secondFormat

def sendEmail():
    emailServer = smtplib.SMTP('smtp.gmail.com', 587)       # If smptlib.SMTP() is unsuccessful then try
    print(type(emailServer))                                # "= smtplib.SMTP_SSL('smtp.gmail.com', 465)"
    print(emailServer.ehlo())                  # ALWAYS CALL FIRST AFTER CREATING OBJ (250 = success)
                                        #:Sends a "hello" to the server, making sure you get a response
    emailServer.starttls()                  # Enables encryption for your connection
    email = input("Email: ")
    password = getpass.getpass()        # Masks password
    receipientEmail = input("Receipient: ")
    subject = input("Subject: ")
    message = input("Message: ")
    try:
        print(emailServer.login(email, password))
    except Exception:
        print("Can't login")
        return
    password = None
    print(password)
    emailServer.sendmail(email, receipientEmail, 'Subject: ' + subject + '\n' + message)
    emailServer.quit()

account = MyPlexAccount('****', '****')
plex = account.resource('MediaServer').connect()
new = formatSearchStr(str(plex.library.section('Movies').recentlyAdded(1)))
print(plex.library.section('Movies').search(new))
#print(plex.library.section('Movies').search('Rush Hour'))
#plex.library.section

#sendEmail()
