import requests

response = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Print the response object (not very informative)
print(response)

# Check the status code of the response
if response.status_code == 200:
    print('Success')
else:
    print(f'Failed with status code: {response.status_code}')

# Print the content of the response
print(response.text)  # Use response.content for raw bytes
