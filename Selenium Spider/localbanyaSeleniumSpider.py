"""
Author :- Mandar Sawant.
Email :- mandar.sawant95@gmail.com
"""
# Selenium driver to simulate actual user visiting website
from selenium import webdriver
# To deal with urls file
import json
# To write scraped data to excel sheet
import xlsxwriter

# Read Urls to be visited from urls json file.
my_data = json.loads(open("urls.json").read())

# Create Excel Workbook
workbook = xlsxwriter.Workbook('Products.xlsx')

# Add worksheet to the workbook
worksheet = workbook.add_worksheet()

# Initialize row and column
# Iterate over rows and columns to insert data in worksheet
row = 1
col = 0

# Perform following operations for each Url in urls json file.
for link in my_data:
    # Extract url
    url = link['navigation_url']
    # Initialize webdriver from selenium
    driver = webdriver.Firefox()
    # Open url in driver
    driver.get(url)

    # Script to Scroll down the window.
    for z in range(1, 150):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Read all the products using outer div xpath
    data = driver.find_elements_by_xpath('//div[@class = "product-inner"]/a[@class = "pointer"]')

    # Iterate over above read Products and fetch required data and write it to excel sheet row.
    for i in data:
        worksheet.write(row, col, i.find_element_by_xpath('./div[@class="prodNameCntr"]/div[@class="prName"]').text)
        worksheet.write(row, col + 1, i.find_element_by_xpath('./div[@class="skuPrice"]/div[@class="skuSelected"]/span[@class="sku_weight"]').text)
        worksheet.write(row, col + 2, i.find_element_by_xpath('./div[@class="skuPrice"]/div[@class="price"]/div[@class="new-price"]').text)
        worksheet.write(row, col + 3, i.find_element_by_xpath('./div[@class="skuPrice"]/div[@class="price"]/div[@class="old-price"]').text)
        row += 1

    # Close the driver
    driver.quit()
    # End of for

# Close the Workbook
workbook.close()

"""
Note :- Excel workbook is edited in memory . If program is closed while executing , Excel sheet will not be written
        partially. Output in excel sheet will be available only after complete execution of the program.

"""