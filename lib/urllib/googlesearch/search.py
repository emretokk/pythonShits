import urllib.request
import urllib.parse

values = {"q": "test searching"}

data = urllib.parse.urlencode(values)
#data = data.encode("UTF-8")
base_url = "https://www.google.com/search?"+data

# self, *args, **kwargs

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(base_url, headers=headers)
resp = urllib.request.urlopen(req)

resp_data = resp.read()
print(resp_data)