import requests

b = "https://www.reddit.com/"

data = {'grant_type': 'password',
               'username': 'matthiasVinco',
               'password': 'Matthias@28908'
}

r = requests.get(b + '/r/programming/about.json', data=data, 
headers = {'User-Agent': 'Api-advanced by matthiasVinco'}, allow_redirects=False)

d = r.json()
print(d, type(d), r.status_code)
