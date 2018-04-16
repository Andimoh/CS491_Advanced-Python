import re

def contacts():    #read the text file
    file = open("contact.txt", "r")
    numbers_re = "\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}"

    for line in file:    #for every line in the txt file use the regex pattern to search for phone number
        p_numbers = re.findall(numbers_re, line)

        for numbers in p_numbers:
            print(numbers)
            
contacts()
    
