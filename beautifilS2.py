import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


class

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#count = input('Enter count:')
#position = input('Enter position')

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = 4
position = 3

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all anchor tags
tags = soup('span') #<a....>...</a>
for tag in tags:
    s+=int(tag.contents[0])
    c+=1
print('Count ', c)
print('Sum ', s)