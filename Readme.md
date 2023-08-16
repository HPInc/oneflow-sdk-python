# Python SDK for Site Flow

Site Flow API request client including the OneFlow credentials authentication logic.
## Requirements

Python 3

See [requirements.txt](requirements.txt) for Python package dependencies.

## Installation instructions ##

### Git ###
    
    git clone https://github.com/HPInc/oneflow-sdk-python <your-target-directory>
    
### Manually ###

Download the .zip file of this project and unzip it in the desire location. [Download the last zip here](https://github.com/HPInc/oneflow-sdk-python/archive/master.zip)


## Basic usage

```python
import os
from OneflowSDK import OneflowSDK

# Create a OneflowSDK instance
api_url = "https://orders.oneflow.io"
client = OneflowSDK(api_url, os.environ["OFS_TOKEN"], os.environ["OFS_SECRET"])

# Fill in request method, path and data
method = "POST"
path = "/api/order"
data = {
    # ... Order Data
}

# Make the request to the endpoint
result = client.request(method, path, data)
```

## Samples

You can find Site Flow order validation and submission examples in the [samples](samples) folder.
