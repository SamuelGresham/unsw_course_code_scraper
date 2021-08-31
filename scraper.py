import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json

url = 'http://timetable.unsw.edu.au/2021/subjectSearch.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

codes = []

for a in soup.findAll('a'):
    if len(a.text) == 4:
        codes.append(a.text)

courses = []

for code in codes: 
    #get the website
    url1 = "http://timetable.unsw.edu.au/2021/" + code + "KENS.html"
    print("Now getting data for code " + code + " using the URL " + url1)
    response = requests.get(url1)
    soup = BeautifulSoup(response.text, "html.parser")
    for a in soup.findAll('a'):
        if (len(a.text) == 8 and a.text[-1].isnumeric()):
            courses.append(a.text)

json_formatted_string = json.dumps(courses)

print("Overwriting old file now. Bye bye data!")

f = open("data.txt", "w")
f.write(json_formatted_string)
f.close()

print("done")
