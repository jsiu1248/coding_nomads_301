# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.

import requests
from decouple import config
auth = requests.auth.HTTPBasicAuth(config('CLIENT_ID'), config('SECRET_TOKEN'))


# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': '<USERNAME>',
        'password': '<PASSWORD>'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

print(res.json())

# convert response to JSON and pull access_token value
# TOKEN = res.json()['access_token']

# # add authorization to our headers dictionary
# headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# # while the token is valid (~2 hours) we just add headers=headers to our requests
# requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)