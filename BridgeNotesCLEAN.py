from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import os
import time
import csv
from selenium.webdriver.support import expected_conditions as EC



def load_csv():
    driver = webdriver.Chrome('C:\\Users\\bensb\\MyPythonScripts\\chromedriver_win32\\chromedriver')
    driver.implicitly_wait(10)
    directory = os.getcwd()
    print(directory)
    spreadsheet = open('C:\\Users\\bensb\\PycharmProjects\\Selenium_Test\\Files\\PythonTest.csv', mode='r')
    return driver, spreadsheet

def login_bridge(driver):
    driver.get("https://crm.uprightlaw.com/account/login")
    input("Log in and hit Enter to proceed")

    """
    user = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[1]/input")
    user.clear()
    user.send_keys("bbloomer@uprightlaw.com")
    password_field = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[2]/input")
    password_field.send_keys(password)
    login = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[3]/button")
    login.click()
    """

def create_table():
    row1_column = ''.join(row)
    column_list = row1_column.split(',')
    return column_list


def search_for_client():
    client_search = driver.find_element_by_xpath('//*[@id="search-input"]')
    client_search.clear()
    client_search.send_keys(column_list[2])
    search_button = driver.find_element_by_xpath('//*[@id="search-button"]')
    search_button.click()
    name = driver.find_element_by_xpath('//*[@id="intro-step-2"]/div[2]')
    name.click()
    return

def click_add_notes():
    add_note = driver.find_element_by_xpath('//*[@id="add-note"]')
    add_note.click()

def communication_type_fun():
    communication_type_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/div/select')
    communication_type_entry.click()
    communication_type_entry.send_keys(communication_type)

def in_or_outbound_fun():
    in_or_outbound_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[2]/div/select')
    in_or_outbound_entry.click()
    in_or_outbound_entry.send_keys(in_or_outbound)

def category_fun():
    category_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[1]/div/select')
    category_entry.click()
    category_entry.send_keys(category)

def time_billed_fun():
    time_billed_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[2]/div/input')
    time_billed_entry.clear() #multiple clears needed for some reason
    time_billed_entry.clear() #multiple clears needed for some reason
    time_billed_entry.clear() #multiple clears needed for some reason
    time_billed_entry.click()
    time_billed_entry.send_keys(time_billed)

def subcategory_fun():
    if category == "Other":
        subcategory_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[4]/input')
    else:
        subcategory_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[4]/select')
    subcategory_entry.click()
    subcategory_entry.send_keys(subcategory)

def note_text_fun():
    note_text_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[5]/textarea')
    note_text_entry.clear()
    note_text_entry.click()
    note_text_entry.send_keys(note_text)

def save_note():
    #replace with save button
    exit_note = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/button/i')
    exit_note.click()

def clients_search():
    client_search = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[2]/ul[1]/li[1]/a')
    client_search.click()

def print_line():
    print("Notated " + str(column_list[1]) + "'s file: " + str(column_list[8]))


driver, spreadsheet= load_csv()
line_count = 0
login_bridge(driver)
for row in spreadsheet:
    if line_count > 0:
        column_list = create_table()
        communication_type = column_list[3]
        in_or_outbound = column_list[4]
        category = column_list[5]
        time_billed = column_list[6]
        subcategory = column_list[7]
        note_text = column_list[8]
        if column_list[3] == "NA":
            print("Skipped " + str(column_list[1]))
            continue
        search_for_client()
        click_add_notes()
        communication_type_fun()
        in_or_outbound_fun()
        category_fun()
        time_billed_fun()
        subcategory_fun()
        note_text_fun()
        save_note()
        clients_search()
        print_line()
    line_count += 1

driver.close()
spreadsheet.close()
print("Complete. Logged notes in " + str(line_count) + " client files.")


