import urllib
git_classes={1:"Education",2:"Technical",3:"Projects",4:"Work",5:"Socialy",6:"Popularity",7:"Non_technical skills",8:"Tech_Interests",9:"Non_Tech_Interests"};
print " Select number for display"
for i in range(1,10):
      print str(i)+":"+git_classes[i];
selection=raw_input();
print(git_classes[int(selection)]);
f=open("data.txt","r");
contents=f.read();
contents=contents.split("\n");
#print contents;
content_dict={};
details=[];
for i in contents:
    j=i.strip("'");
    j=j.split(":");
    if(j[0]==git_classes[int(selection)]):
        j[1]=j[1].split("_")[0];
        j[1]=j[1].strip();
        details.append(j[1]);
print details;
url="https://api.github.com/users/rashrag/";
for i in range(0,len(details)):
    url="https://api.github.com/users/rashrag/";
    url=url+details[i]
    url=url.strip();
    print url
    f1=urllib.urlopen(url);
    s=f1.read()
    print s
