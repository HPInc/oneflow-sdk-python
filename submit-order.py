#!/usr/bin/python

__author__ = 'oneflow'

import requests, json, hmac, hashlib, datetime, base64, string, random, os

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_headers(method, path, timestamp):
	string_to_sign = method + ' ' + path + ' ' + timestamp
	signature = hmac.new(secret, string_to_sign, hashlib.sha1).hexdigest()
	oneflow_auth = token + ':' + signature
	return {'content-type': 'application/json',
		'x-oneflow-authorization': oneflow_auth,
		'x-oneflow-date': timestamp}

def oneflow_request(method, path, data):
	timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	url = endpoint + path
	headers = create_headers(method, path, timestamp)
	result = requests.post(url, data, headers=headers)
	return result.content

def validate_order(order):
	print "Validating Order"
	return oneflow_request("POST", '/api/order/validate', order)

def submit_order(order):
	print "Submitting Order"
	return oneflow_request("POST", '/api/order', order)


#oneflow acccess credentials
token = os.environ['ONEFLOW_TOKEN']
secret = os.environ['ONEFLOW_SECRET']
endpoint = 'http://stage.oneflowcloud.com'

#Here are the variables required for a single item order
#this is not a full set of fields available
destination = "oneflow"
orderId = id_generator()
itemId = id_generator()
sku = "card"
quantity = 1
fetchPath = "https://oneflow-public.s3.amazonaws.com/CardSample.pdf"
componentCode = "card"
shipTo = {
	"name":           "Nigel Watson",
	"address1":       "1 Primrose Street",
	"town":           "London",
	"postcode":       "12345",
	"isoCountry":     "GB",
	"email":          "info@oneflowsystems.com",
	"phone":          "01234567890"
}
carrier = {
	"code":       "royalmail",
	"service":    "firstclass"
}

#nothing to change below here

#create an item - this goes into the order below
item = {
	"sourceItemId":         itemId,
	"sku":                  sku,
	"quantity":             quantity,
	"components": [{
		"code":               componentCode,
		"path":               fetchPath,
		"fetch":			  "true"
	}]
}

#create a shipment - this goes into the order below
shipment = {
	"shipTo":  shipTo,
	"carrier": carrier
}

#put together the complete order
order = {
  "destination": {
    "name":       destination
  },
  "orderData": {
    "sourceOrderId":        orderId,
    "items": [ item ],
    "shipments": [ shipment ]
  }
}

#validate the order
print validate_order(json.dumps(order))

#finally, submit the order
print submit_order(json.dumps(order))
