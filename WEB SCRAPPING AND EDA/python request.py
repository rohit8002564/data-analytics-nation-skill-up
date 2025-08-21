'''To install request library via pip, use the following command: pip install requests'''
# Syntax: requests.get(url, params={key: value}, **kwargs)

# Making a Simple GET Request
import requests
response = requests.get("https://www.geeksforgeeks.org/")
print(response.status_code)

'''Explanation:

requests.get() sends a GET request to the specified URL.
response.status_code returns the HTTP status code (200 means success).'''

# Sending GET Requests with Parameters
params = {'q': 'geeksforgeeks'}
response = requests.get("https://www.google.com/search", params=params)
print(response.url)

# Response Object
response = requests.get("https://www.geeksforgeeks.org/")
print(response.url)
print(response.status_code)

'''Explanation:

response.url returns the final URL after redirections.
response.status_code shows the HTTP status of the request.
Status code 200 indicates that request was made successfully.'''

# POST Request
payload = {'username': 'test','password': 'test123'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)
print(response.json())

'''Explanation:

Sends form data to the server.
data=payload sends the data in the request body.
The server echoes back the data for testing.'''

# Authentication using Python Requests
from requests.auth import HTTPBasicAuth
response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)
print(response.json())

'''Explanation:

HTTPBasicAuth is used to provide basic authentication.
The server responds with a 200 status code if authentication is successful.'''

# SSL Certification Verification
response = requests.get('https://expired.badssl.com/', verify=False)
print(response.status_code)

'''Explanation:

This request checks the SSL certificate of the server.
A valid SSL certificate is required for secure connections.'''

# Providing a custom certificate:
response = requests.get('https://example.com', verify='/path/to/certfile.pem')  

#Using Session Objects
import requests

# Create a session object
session = requests.Session()

# Set a cookie
session.get('https://httpbin.org/cookies')

# Access the cookie in the next request
response = session.get('https://httpbin.org/cookies')
print(response.text)

# Error Handling with Requests
import requests

try:
    response = requests.get("https://www.example.com/", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something Else:", err)