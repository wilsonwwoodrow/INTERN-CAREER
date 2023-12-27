import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Set up the webdriver (downloads the appropriate driver for your browser)
chrome_options = Options()

# Set up the webdriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get("https://www.oanda.com/currency-converter/live-exchange-rates/")

# Wait for the content to load (adjust the time based on your needs)
driver.implicitly_wait(5)

# Now you can access the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser
driver.quit()

# Find all <td> elements and append them to listt
x = soup.find_all("td")
listt = [i.text for i in x]

# Separate the lists
list1 = listt[0::3]
list2 = listt[1::3]
list3 = listt[2::3]

# Create a DataFrame
df = pd.DataFrame({
    'Currency': list1,
    'buying': list2,
    'selling': list3
})

# Convert columns to appropriate data types
df['buying'] = df['buying'].astype(float)
df['selling'] = df['selling'].astype(float)

# Save DataFrame to a CSV file
df.to_csv('OANDA.csv', index=False)
