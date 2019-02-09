# import spacy
# from spacy.pipeline import EntityRecognizer

# class Email:
#     def __init__(self):
#         self.clubname = []
#         self.date = []
#         self.time = []
#         self.activity = []
#         self.urlimage = []
#         self.topic = []
#         self.loc = []


# def abs(x):
#     if x > 0:
#         return x
#     return (-x)

# def pair(email):
#     dateloc = email.date[0][1]
#     minPair = [0,0,9999999999]
#     minIndex = 0
#     minDif = 99999999999
#     for j in range(len(email.date)):
#         for i in range(len(email.time)):
#             loc = email.time[i][1]
#             if(abs(loc-dateloc) < minDif):
#                 minIndex = i
#                 minDif = abs(loc-dateloc)
#             if(minDif < minPair[2]):
#                 minPair[2] = minDif
#                 minPair[1] = minIndex
#                 minPair[0] = j
#     email.time = [email.time[minPair[1]][0]]
#     email.date = [email.date[minPair[0]][0]]
#     email.urlimage = ['']
#     if(len(email.loc) < 1):
#         email.loc.append(["CMU"])
#     else:
#         minIndex = 0
#         minDif = 99999999999
#         for i in range(len(email.loc)):
#             loc = email.loc[i][1]
#             if(abs(loc-dateloc) < minDif):
#                 minIndex = i
#                 minDif = abs(loc-dateloc)
#         email.loc = [email.loc[minIndex]]
#     return email


# def clean(email):
#     email.time = [email.time[0].replace(r'\r\n','')]
#     email.date = [email.date[0].replace(r'\r\n','')]
#     email.clubname = [email.clubname[0][0].replace(r'\r\n','')]
#     email.activity = [email.activity[0].replace(r'\r\n','')]
#     email.loc = [email.loc[0][0].replace(r'\r\n','')]
#     return email

# def driver(input,temp):

#     nlp = spacy.load('en',disable=['parser'])
#     #file = open(file,'r')
#     #input = file.read()
#     #file.close()
#     doc = nlp(input)
#     #temp = Email()
#     for ent in doc.ents:
#         words = ent.text
#         type = ent.label_
#         start = ent.start_char
#         #print(ent.text, ent.label_)
#         if(ent.label_ == "DATE"):
#             temp.date.append((ent.text,ent.start_char))
#         elif(ent.label_ == "TIME"):
#             temp.time.append((ent.text,ent.start_char))
#         elif(ent.label_ == "ORG"):
#             temp.clubname.append((ent.text,ent.start_char))
#         elif(ent.label_ == "LOC"):
#             temp.loc.append((ent.text,ent.start_char))


#     #If multiple dates, discard email
#     #Or multiple orgs, activites, write some cleaning function
#     #Might be useful to include context of email for "this" localizations
#     #Add ability to parse multiple events later
#     #if(len(temp.date) == 1):
#     temp = pair(temp)
#     temp = clean(temp)
#     try:
#         if(len(temp.clubname) > 0 and len(temp.date)>0 and len(temp.time)>0 and len(temp.loc)>0):
#             return temp
#         else:
#             return None
#     except UnicodeEncodeError as e:
#         return None

# """for token in doc:
#     print(token.text)"""
