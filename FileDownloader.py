import requests

url = 'https://ENTER URL HERE/DOWNLOAD FILE'
r = requests.get(url, allow_redirects=True)
open('DOWNLOAD FILE', 'wb').write(r.content)
