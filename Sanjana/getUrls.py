import urllib2
from bs4 import BeautifulSoup
from random import randint

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
base_url = "https://www.linkedin.com/directory/people-"

writefile = open("profile_urls.txt", "w")

profiles_list = []

while(len(profiles_list) < 50): # increase to as many as you want
    for letter in letters:
        # this bit gets us to the page with only links to profiles (the page we want)
        directory_url = base_url + letter
        for i in range(0, 3):
            response = urllib2.urlopen(directory_url).read()
            htmldom = BeautifulSoup(response)
            ul = htmldom.find("ul", { "class" : "directory" })
            urllist = ul.find_all('a')
            rand_index = randint(1,len(urllist)-1)
            directory_url = urllist[rand_index].get("href")

        # print directory_url
        
        # now we get the actual profile links excluding those which make us search more (gets the profile urls we want)
        final_response = urllib2.urlopen(directory_url).read()
        final_htmldom = BeautifulSoup(final_response)
        ul = final_htmldom.find("ul", { "class" : "directory" })
        proflinks = ul.find_all('a')

        for link in proflinks:
            if(link.get("href")[0] == "/"):
                profiles_list.append(link.get("href"))

        # print len(profiles_list)

        # just testing. remove this to run
        if(len(profiles_list) > 50):
            break
        

print profiles_list

''' FOR some strange reason, this is not working in my laptop tonight. please modify code appropriately to write to file. I obtained file by redirecting output
for i in profiles_list:
    writefile.write(i + "\n")
'''
