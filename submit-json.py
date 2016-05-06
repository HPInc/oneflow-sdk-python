__author__ = 'oneflow'

#import required libraries
import requests, json, hmac, hashlib, datetime, base64, os

#credentials and endpoint
token = os.environ['ONEFLOW_TOKEN']
secret = os.environ['ONEFLOW_SECRET']
endpoint = 'http://stage.oneflowcloud.com'

#specific api call
api_path = '/api/order/validate'

#sign the request
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
string_to_sign = 'POST' + ' ' + api_path + ' ' + timestamp
signature = hmac.new(secret, string_to_sign, hashlib.sha1).hexdigest()
oneflow_auth = token + ':' + signature

#set the request headers
headers = { 'content-type': 'application/json',
            'x-oneflow-authorization': oneflow_auth,
            'x-oneflow-date': timestamp }

#read in the orderdata from the file, this could be constructed inside the app
order=open('ordertest.json').read()
data = json.dumps(order)

#make the POST request to the endpoint
r = requests.post(endpoint + api_path, data, headers=headers)

#output the results
print r.content
