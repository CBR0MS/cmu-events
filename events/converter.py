# import imaplib
# import email
# import string
# import re
# #from parserOne import *
# from .parserOne import *

# def normalizer(line):
#     while(re.search("Subject:",line) != None):
#          index = re.search("Subject:",line).span()[0]
#          line = line[index+8:-1]
#     x = re.split("To:",line)
#     c = x[1]
#     c = c.replace('\r\n',' ')
#     c = c.replace(r'\r\n',' ')
#     return c

# def extractor(line):
#     x = re.search("(Subject:).+\n*(To:)",line)
#     if x == None:
#         return None
#     xp = x.group()
#     length = len(xp)-3
#     return (xp[8:length])

# def retrieve():
#     mail = imaplib.IMAP4_SSL('imap.gmail.com')
#     mail.login('cmuactivitieslist','cmualca2019')
#     mail.list()
#     mail.select('inbox')

#     result, data = mail.uid('search',None,"ALL")

#     objects = []

#     i = len(data[0].split())
#     for x in range(i):
#         latest_email_uid = data[0].split()[x]
#         result, email_data = mail.uid('fetch',latest_email_uid,'(RFC822)')
#         raw_email = email_data[0][1]
#         raw_email_string = raw_email.decode('utf-8')
#         email_message = email.message_from_string(raw_email_string)
#         obj = Email()
#         for part in email_message.walk():
#             if part.get_content_type() == "text/plain":
#                 body = part.get_payload(decode=True)
#                 save_string = str("Dumpgmailemail_" + str(x) + ".eml")
#                 #myfile = open(save_string, 'w+')
#                 try:
#                     line = body.decode('utf-8')
#                 except UnicodeEncodeError as e:
#                     break
#                 subject = extractor(line)
#                 if subject != None:
#                     obj.activity = [subject]
#                     #print(save_string)
#                     try:
#                         obj = driver(normalizer(line),obj)
#                         if obj != None:
#                             objects.append(obj)
#                     except IndexError as e:
#                         break
#             else:
#                 continue
#     return objects
