from linkedin import linkedin
import urllib2
import oauth2 as oauth
import time
'''
CONSUMER_KEY = '78n8iswagri3t1'
CONSUMER_SECRET = 'FsxPzuk0eySVKCww'
USER_TOKEN = '1ccb1925-b540-46c8-9561-9671a7446b36'
USER_SECRET = '84ece83a-f3d5-40c5-a3da-94fc3f27c86a'
'''

API_KEY = '78n8iswagri3t1'
API_SECRET = 'FsxPzuk0eySVKCww'
RETURN_URL = 'https://localhost:8080'

# step 2.b on authentication page
AUTHORIZATION_CODE = 'AQT_x9OD2BbinsDOZhwGfscH9W7VPCdFPIz6gnpl2Eh0zSC4K5Tg4P8sTJOac0M4e1gPrP7s-awCwD5GmxNMzo3z2qoUDrLk3CjFntSIEzmopRKEoWg'

# Instantiate the developer authentication class

#authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
#print authentication.authorization_url

#authentication.authorization_code = 'AQR32bUdcjnr8-uyHJ1Q2k_5Yeq88uJ_HdW6AB8rdl8l-Q07twtF3DwHxdcvPkUzsmjle6DQ4hZPsAn08Pp2u45mfzduuqyYIwAqrn6zw7uFtWXKtI8'
#print(authentication.get_access_token())

# Pass it in to the app...
ACCESS_TOKEN = 'AQUaEi-eUrMkKjQIQnGswmnGCDkoMdiKSBrSlXic465PAwx57jgJDDAs-C8Z7yhDAVju9x7FTfK-qLKx0oktvVfe_d28FAgozw7QPwa2Vqu1PPp-RwsIrYzDN_ocgTFcMJukDtL-0Ag-bYzpGbkWHKMdaN9rYP2VG5Rrcn1bY19wTv0vAgE'
application = linkedin.LinkedInApplication(token=ACCESS_TOKEN)


''' want to get random people's things from api '''

base_url = "https://www.linkedin.com"
readfile = open("profiles_urls.txt", "r")
profiles = readfile.readlines()
writefile = open("random_profiles.txt", "w")
count = 1

for user in profiles:
    print count
    final_url = base_url + user.strip()
    writefile.write(str(application.get_profile(member_url=final_url, selectors=['id','first-name', 'last-name', 'maiden-name', 'headline', 'location', 'industry', 'distance', 'relation-to-viewer', 'num-connections', 'summary', 'specialties', 'positions', 'public-profile-url'])) + "\n")
    count += 1
    


''' # works to get my connections' profile stuff from api (written to file already, don't run again unless you put your token and find your connections
writefile = open('profiles_api.txt', 'w')

# Use the app....

count = 0 # number of profiles fetched

#testid = application.get_connections()['values'][3]['id']

myprofile = application.get_profile(selectors=['id','first-name', 'last-name', 'maiden-name', 'headline', 'location', 'industry', 'distance', 'relation-to-viewer', 'num-connections', 'summary', 'specialties', 'positions', 'public-profile-url'])

writefile.write(str(myprofile) + "\n")
count += 1

connections = application.get_connections()['values']

while(count < 1000):
    if(count > 1):
        connections = application.get_connections(member_id=connections[0]['id'])
    for profile in connections:
        userprofile = application.get_profile(member_id=profile['id'], selectors=['id','first-name', 'last-name', 'maiden-name', 'headline', 'location', 'industry', 'distance', 'relation-to-viewer', 'num-connections', 'summary', 'specialties', 'positions', 'public-profile-url'])
        count += 1
        writefile.write(str(userprofile) + "\n")
        print count
    

'''




# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# all testing stuff below this line (ignore for now)




                                    
#public_profile_url = application.get_profile(member_id=testid, selectors=['public-profile-url'])['publicProfileUrl']

#print testid
#print public_profile_url


#testurl['url'] is unicode. make it utf-8

#utfurl = testurl['url'].encode('utf8')

#print (type(utfurl))
#print utfurl

#encurl = urllib2.quote(utfurl, safe="")

#print(application.get_profile(member_url='https://in.linkedin.com/pub/rashmi-raghunandan/57/85a/97b', selectors=['first-name', 'public-profile-url', 'last-name', 'educations', 'skills', 'summary', 'num-connections']))

#data['key'] = 'A1JRUc5JqTU1RAykmBeS6w(('


'''
url = "https://api.linkedin.com/v1/people/url='https://in.linkedin.com/pub/rashmi-raghunandan/57/85a/97b'"

consumer = oauth.Consumer(
     key=CONSUMER_KEY,
     secret=CONSUMER_SECRET)
     
token = oauth.Token(
     key=USER_TOKEN,
     secret=USER_SECRET)


client = oauth.Client(consumer, token)

resp, content = client.request(url)
print content
'''

#pub = 'https://in.linkedin.com/pub/rashmi-raghunandan/57/85a/97b'
#encurl = urllib2.quote(pub, safe="")
#print encurl
'''
url = 'https://api.linkedin.com/v1/people/url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fvijaymahantesh:(id,skills,educations,first-name,last-name,industry,num-connections,languages)?oauth2_access_token=AQUaEi-eUrMkKjQIQnGswmnGCDkoMdiKSBrSlXic465PAwx57jgJDDAs-C8Z7yhDAVju9x7FTfK-qLKx0oktvVfe_d28FAgozw7QPwa2Vqu1PPp-RwsIrYzDN_ocgTFcMJukDtL-0Ag-bYzpGbkWHKMdaN9rYP2VG5Rrcn1bY19wTv0vAgE&format=json'

req = urllib2.Request(url, None)
response = urllib2.urlopen(req)
print response.read()
'''
