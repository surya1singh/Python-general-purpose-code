import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

api_docs = 'https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets'

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('* Calling Twitter...')
url = twurl.augment(TWITTER_URL,
              {'q':'suryapratapsingh','count':100 })
print(url)
connection = urllib.request.urlopen(url)
data = json.loads(connection.read().decode())
statuses = data['statuses']
search_metadata = data['search_metadata']
a=0
for status in statuses:
    print(status)
    print(a)
    a+=1
print(search_metadata)
headers = dict(connection.getheaders())
print(headers)
print(type(headers))
print('Remaining', headers['x-rate-limit-remaining'])
