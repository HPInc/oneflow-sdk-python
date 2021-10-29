__author__ = 'oneflow'

import json
from OneflowSDK import OneflowSDK

#credentials and endpoint
#OneflowSDK instance
client = OneflowSDK(endpoint, token, secret)

#specific api call
api_path = '/api/order/validate'

#read in the orderdata from the file, this could be constructed inside the app
order=open('ordertest.json').read()
data = json.dumps(order)

#make the POST request to the endpoint
r = client.request('POST', api_path, data)

#output the results
print(r)
