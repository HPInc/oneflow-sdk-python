#!/usr/bin/python

__author__ = "HPInc."

#
# DELETE ME!
# Import parent directory to the sys.path to be able to load OneflowSDK
#

import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

#
# Order submission logic
#

import json, os
from OneflowSDK import OneflowSDK

# credentials and endpoint
token = os.environ["ONEFLOW_TOKEN"]
secret = os.environ["ONEFLOW_SECRET"]
endpoint = "https://orders.oneflow.io"

# OneflowSDK instance
client = OneflowSDK(endpoint, token, secret)

# specific api call
api_path = "/api/order"

# read in the order data from the file, this could be constructed inside the app
currentDir = os.path.dirname(os.path.realpath(__file__))
order = open(os.path.join(currentDir, "ordertest.json")).read()

# make the POST request to the endpoint
r = client.request("POST", api_path, order)

# output the results
print(r)
