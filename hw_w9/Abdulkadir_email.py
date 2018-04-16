import re

def emails():  #read the text file
    file = open("emails.txt", "r")
    email_re = "[a-zA-Z]+[a-zA-Z0-9]+?@[a-zA-Z]+\.[com|COM|edu|EDU|org|ORG|net|NET]+"

    for line in file:  #for every line in the txt file use the regex pattern to search for email
        emails = re.findall(email_re, line)

        for email in emails:
            print(email)
            
emails()
