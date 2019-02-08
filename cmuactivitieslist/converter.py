import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('cmuactivitieslist','cmualca2019')
mail.list()
mail.select('inbox')

result, data = mail.uid('search',None,"ALL")

i = len(data[0].split())
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uit('fetch',latest_email_uid,'(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decdoe('utf-8')
    print(raw_email_string)
