#Mohammed Abdulkadir
#CS491 Adv python
#HW_W12

from __future__ import print_function
from bs4 import BeautifulSoup
import requests

class fact_directory(object):

    def __init__(self, url="",page="",bsoup=""):
        self.url = url
        self.page = page
        self.bsoup = bsoup

    def connect(self):
        self.page = requests.get(self.url)

    def get_staffinfo(self):
      #this function will scrape the link from the faculty directory
        bsoup = BeautifulSoup(self.page.text, 'html.parser')

        #finds all 'div' tags with faculty info
        directory_array = bsoup.find_all('div', class_='people-wrapper')
        directory_array2 = bsoup.find_all('div', class_='department')
        directory_array3 = bsoup.find_all('div', class_='person-contact')
        directory_array4 = bsoup.find_all('div', class_='summary')
        
        #if faculty is found, pull information from website
        for i in directory_array:
            name = i.find('h3').text
            position = i.find('h4').text
            info = i.find('p').text
            web = i.find('a href')
            print("Name:", name)
            print("Position:", position)
            print(info)
            print("Website:", web)
            print("**********************************************************", sep="")

    def null_filler(self, fun_arr):
      #check if all infomations are available if not N/A

        data = []
        for p_row in fun_arr:
            output = p_row.text.encode('utf-8').strip()
            if not output:
                output = "N/A"
                data.append(output)
            else:
                data.append(output)
        return data

if __name__ == "__main__":
    #faculy page from class
    start = fact_directory("http://cs.siu.edu/faculty-staff/continuing_faculty.php")
    #function connect() from class fact_directory
    start.connect()
    #function get_staffinfo() from class fact_directory
    start.get_staffinfo()
