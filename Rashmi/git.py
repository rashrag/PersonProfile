import urllib
def readData(url):
    f=urllib.urlopen(url);
    s=f.read()
    s=[x.strip() for x in s.split(',')]
    for k in s:
        #print k
        t=[x for x in k.split(':')]
       # print t
        for l in t:
                print l
                if(l.startswith("https")):
                    print "yo"
   

readData("https://api.github.com/users/rashrag");
