#!C:\Python27\python2.exe
from linkedin import linkedin
import urllib2
import requests
from bs4 import BeautifulSoup
import oauth2 as oauth
import time
import cgi, os
import smtplib
import cgitb; cgitb.enable()



CONSUMER_KEY = '78n8iswagri3t1'
CONSUMER_SECRET = 'FsxPzuk0eySVKCww'
USER_TOKEN = '1ccb1925-b540-46c8-9561-9671a7446b36'
USER_SECRET = '84ece83a-f3d5-40c5-a3da-94fc3f27c86a'


API_KEY = '78n8iswagri3t1'
API_SECRET = 'FsxPzuk0eySVKCww'
RETURN_URL = 'https://localhost:8080'

# get parameters, given Ravi's as default in index.html
form = cgi.FieldStorage()

final_out = ""


''' want to get X's profile '''

base_url = form['username'].value
final_out += base_url + "<br><br>"


#base_url = "http://www.linkedin.com/pub/rashmi-raghunandan/57/85a/97b"
#response = urllib2.urlopen(base_url).read()
response = requests.get(base_url).text

htmldom = BeautifulSoup(response)

bgcontent = htmldom.find("div", {"class":"background-content"})

''' get experience '''

bgexperience = htmldom.find("div", {"id":"background-experience-container"})
if(bgexperience):
    final_out += "Work" + "<br>"

    position_set = list()
    company_set = list()
    time_set = list()
    description_set = list()

    for exp in bgexperience.contents[0].findAll("div", {"class":"editable-item section-item"}):
        main = exp.contents[0]
        if(main.contents[0].find("h4")):
            position_list.append(main.contents[0].find("h4").text)
        resultset = main.contents[0].findAll("h5")
        if(resultset):
            try:
                company_set.append(resultset[-1].find("a").text)
            except Exception as e:
                company_set.append(resultset[-1].find("span").text)
        if(main.find("time")):
            time_set.append(main.find("span", {"class":"experience-date-locale"}).text)
        if(main.find("p")):
            description_set.append(main.find("p").text)

    while(len(position_set) > 0):
        final_out += position_set.pop() + "<br>"
        final_out += company_set.pop() + "<br>"
        final_out += time_set.pop() + "<br>"
        final_out += description_set.pop() + "<br>"
        final_out += "<br><br>"
    final_out += "-"*100 + "<br>"


''' get projects and publications '''

final_out += "Projects" + "<br>"
bgprojects = htmldom.find("div", {"id":"background-projects-container"})
if(bgprojects):
    title_set = list()
    duration_set = list()
    desc_set = list()

    for proj in bgprojects.contents[0].findAll("div", {"class":"editable-item section-item"}):
        title_set.append(proj.find("h4", {"class":"summary fn org"}).text)
        duration_set.append(proj.find("span", {"class":"projects-date"}).text)
        desc_set.append(proj.find("p").text)

    while(len(title_set) > 0):
        final_out += title_set.pop() + "<br>"
        final_out += duration_set.pop() + "<br>"
        final_out += desc_set.pop() + "<br>"
        final_out += "<br><br>"

bgpubs = htmldom.find("div", {"id":"background-publications-container"})
if(bgpubs):
    pub_title_set = list()
    pub_duration_set = list()
    pub_desc_set = list()

    for pub in bgpubs.contents[0].findAll("div"):
        pub_title_set.append(pub.find("span", {"dir":"auto"}).text)
        pub_duration_set.append(pub.find("span", {"class":"publication-date"}).text)
        pub_desc_set.append(pub.find("p").text)

    while(len(pub_title_set) > 0):
        final_out += pub_title_set.pop() + "<br>"
        final_out += pub_duration_set.pop() + "<br>"
        final_out += pub_desc_set.pop() + "<br>"
        final_out += "<br><br>"

    final_out += "-"*100 + "<br>"


''' get non-technical skills '''

final_out += "Non-technical skills" + "<br>"
non_tech_skill_set = list()
bglangs = htmldom.find("div", {"id":"background-languages-container"})
if(bglangs):
    langlist = bglangs.find("ol")
    for i in langlist.contents:
        non_tech_skill_set.append(i.find("span").text)

    final_out += str(non_tech_skill_set) + "<br>"
    final_out += "-"*100 + "<br>"


'''get technical skills '''

final_out += "Skills" + "<br>"
bgskills = htmldom.find("div", {"id":"profile-skills"})
if(bgskills):
    skill_list = bgskills.find("ul")
    skill_set = list()
    for i in skill_list.contents[:len(skill_list.contents)-1]:
        skill_set.append(i.text)

    final_out += str(skill_set) + "<br>"
    final_out += "-"*100 + "<br>"


''' get education '''

bgedu = htmldom.find("div", {"id":"background-education-container"})
if(bgedu):
    school_set = list()
    degree_set = list()
    date_set = list()
    info_set = list()

    for edu in bgedu.contents[0].findAll("div", {"class":"editable-item section-item"}):
        school_set.append(edu.find("h4", {"class":"summary fn org"}).text)
        if(edu.find("span", {"class":"degree"}) and edu.find("span", {"class":"major"})):
            degree_set.append(edu.find("span", {"class":"degree"}).text + edu.find("span", {"class":"major"}).text)
        else:
            degree_set.append("Not mentioned")
        date_set.append(edu.find("span", {"class":"education-date"}).text)
        if(edu.find("p")):
            info_set.append(edu.find("p").text)
        else:
            info_set.append("No info")

    for i in range(len(school_set)):
        final_out += school_set[i] + "<br>"
        final_out += degree_set[i] + "<br>"
        final_out += date_set[i] + "<br>"
        final_out += info_set[i] + "<br>"
        final_out += "<br><br>"


message = final_out.encode("utf-8")

# you can also do a file read and print the file where the file is the html file you want

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)

