import spacy
from spacy.pipeline import EntityRecognizer

class Email:
    def __init__(self):
        self.clubname = []
        self.date = []
        self.time = []
        self.activity = []
        self.urlimage = []
        self.topic = []

def abs(x):
    if x > 0:
        return x
    return (-x)

def pair(email):
    dateloc = email.date[0][1]
    minPair = [0,0,9999999999]
    minIndex = 0
    minDif = 99999999999
    for j in range(len(email.date)):
        for i in range(len(email.time)):
            loc = email.time[i][1]
            if(abs(loc-dateloc) < minDif):
                minIndex = i
                minDif = abs(loc-dateloc)
            if(minDif < minPair[2]):
                minPair[2] = minDif
                minPair[1] = minIndex
                minPair[0] = j
    email.time = [email.time[minPair[1]][0]]
    email.date = [email.date[minPair[0]][0]]

def clean(email):
    return email

def driver(input,temp):

    nlp = spacy.load('en',disable=['parser'])
    #file = open(file,'r')
    #input = file.read()
    #file.close()
    doc = nlp(input)
    #temp = Email()
    for ent in doc.ents:
        words = ent.text
        type = ent.label_
        start = ent.start_char
        #print(ent.text, ent.label_)
        if(ent.label_ == "DATE"):
            temp.date.append((ent.text,ent.start_char))
        elif(ent.label_ == "TIME"):
            temp.time.append((ent.text,ent.start_char))
        elif(ent.label_ == "ORG"):
            temp.clubname.append(ent.text)


    #If multiple dates, discard email
    #Or multiple orgs, activites, write some cleaning function
    #Might be useful to include context of email for "this" localizations
    #Add ability to parse multiple events later
    #if(len(temp.date) == 1):
    pair(temp)
    clean(temp)
    try:
        if(len(temp.clubname) > 0):
            print(temp.clubname)
            print(temp.activity)
            print(temp.date)
            print(temp.time)
    except UnicodeEncodeError as e:
        return
    print('\n')

"""for token in doc:
    print(token.text)"""
