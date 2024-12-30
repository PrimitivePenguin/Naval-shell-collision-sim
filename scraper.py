
from bs4 import BeautifulSoup
import matplotlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def crawler():

    # Creating a webdriver instance
    driver = webdriver.Firefox()
    # This instance will be used to log into LinkedIn
    
    # Opening page
    driver.get("http://www.navweaps.com/index_nathan/Penetration_United_States.php")
    
    # waiting for the page to load
    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    table_element = soup.find_all('table', class_='prettytable')
    # prettytable_tbody_elements = soup.find_all(By.CLASS_NAME, 'prettytable')
    # tbody_size = len(prettytable_tbody_elements)
    print(table_element)
    table_header = []
    table_content = []

    for index, table in enumerate(table_element):
        if index == 0:
            table_header.append(table)
        else:
            table_content.append(table)
    
    print(len(table_content))
    print(len(table_header))
    print(table_header[0], table_content[0])
    
def main():
    # empty\
    crawler()

if __name__ == "__main__":
    main()