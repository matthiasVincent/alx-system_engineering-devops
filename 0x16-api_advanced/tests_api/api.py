import requests

b = "https://www.reddit.com/"

data = {'grant_type': 'password',
               'username': 'matthiasVinco',
               'password': 'Matthias@28908'
}

auth = requests.auth.HTTPBasicAuth('Fgi1a55HCgqzqQkwRE3BFg', 'iMsPBk9mQavNkuXuqu4dHw1i9MqwDg')

r = requests.post(b +'api/v1/access_token',
data=data,
headers = {'User-Agent': 'Api-advanced by matthiasVinco'},
auth=auth)

d = r.json()
print(d)

