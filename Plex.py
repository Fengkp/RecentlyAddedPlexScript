import smtplib
import getpass
import re
import datetime
from plexapi.myplex import MyPlexAccount

def initiatePlex():
    global plexInstance
    plexLogin = input("User: ")
    plexPassword = getpass.getpass()
    plexAccount = MyPlexAccount(plexLogin, plexPassword)
    plexInstance = plexAccount.resource('MediaServer').connect()

def formatTitle(toFormat):
    formatFront = re.sub(r'.*:', '', toFormat)
    formatBack = re.sub(r'>', '', formatFront)
    formatted = hyphenStrCheck(formatBack)
    return formatted

def hyphenStrCheck(toCheck):
    regHyphen = re.compile(r'-')
    if regHyphen.search(toCheck):
        return re.sub(regHyphen, " ", toCheck)
    return toCheck

def sendEmail():
    emailServer = smtplib.SMTP('smtp.gmail.com', 587)       # If smptlib.SMTP() is unsuccessful then try
    print(type(emailServer))                                # "= smtplib.SMTP_SSL('smtp.gmail.com', 465)"
    print(emailServer.ehlo())                  # ALWAYS CALL FIRST AFTER CREATING OBJ (250 = success)
                                        #:Sends a "hello" to the server, making sure you get a response
    emailServer.starttls()                  # Enables encryption for your connection
    emailLogin = input("Email: ")
    emailPassword = getpass.getpass()        # Masks password
    receipientEmail = input("Receipient: ")
    emailSubject = input("Subject: ")
    emailMessage = input("Message: ")
    try:
        print(emailServer.login(emailLogin, emailPassword))
    except Exception:
        print("Can't login")
        return
    emailPassword = None
    emailServer.sendmail(emailLogin, receipientEmail, 'Subject: ' + emailSubject + '\n' + emailMessage)
    emailServer.quit()

initiatePlex()
movies = plexInstance.library.section('Movies')
television = plexInstance.library.section('Television')
recentMovies = []

for movie in movies.recentlyAdded(10):
    recentMovies.append(formatTitle(str(movie)))
for movie in recentMovies:
    print(movies.get(movie).addedAt)
#sendEmail()
