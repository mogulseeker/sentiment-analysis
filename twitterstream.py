
import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = 'DbelX6FFDjnI3jiwn9zRAHgIl' 
api_secret = 'upNw7PQCXj4hojTc3CfznMlCU5MwHz3jDDlNWDCjtRZxELAUwl'
access_token_key = '2525883858-b0J3woxzMsGvKVYb3Q5zNBueHRxczJRF6E3xvZ5'
access_token_secret = 'V5JB3p8KWEOMZ6WFAXls4EERkUDNHs3LyS0k31HzbHY5J'

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('baseline1.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
