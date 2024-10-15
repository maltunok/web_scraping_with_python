# Import necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# for holding the resultant list
element_list = []

# Set up Chrome WebDriver with Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

for page in range(1, 3, 1):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver.get(page_url)

    # Find elements by class name
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    # Collect information from each item on the page
    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

# Print the collected elements
print(element_list)

# Close the driver
driver.quit()
