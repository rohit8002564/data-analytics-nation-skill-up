import requests

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
print(response.status_code)  # Should print 200 if the request was successful
print(response.text)  # Print the HTML content of the page
print(response.status_code)  # Print the status code of the response
print(response.headers)  # Print the headers of the response