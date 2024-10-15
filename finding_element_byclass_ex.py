import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming you're looking for a specific tag/class
    s = soup.find('div', class_='text')  # Replace with actual tag and class

    # Check if s is not None before calling find_all
    if s:
        content = s.find_all('p')

        # Open a file to write the content
        with open('web_content.txt', 'w', encoding='utf-8') as file:
            for p in content:
                text = p.text.strip()  # Get the text and strip any extra whitespace
                print(text)  # Print to console (optional)
                file.write(text + '\n')  # Write each paragraph to the file

    else:
        print("No matching element found.")
else:
    print(f"Failed to retrieve the webpage, status code: {response.status_code}")
