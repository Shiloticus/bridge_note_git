from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import os
import time
import csv
import pyperclip
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


            #assigning CSV contents to variables
def create_table():
    row1_column = ''.join(row)
    column_list = row1_column.split(',')
    return column_list

def assign_csv_vars(column_list):

    communication_type = column_list[3]
    in_or_outbound = column_list[4]
    category = column_list[5]
    time_billed = column_list[6]
    subcategory = column_list[7]
    note_text = column_list[8]

def click_entry(xpaths_dict_key):
    clicked_entry = driver.find_element_by_xpath(xpaths_dict_key)
    clicked_entry.click()
    clicked_entry.clear()
    #entry.clear()
    #entry.clear()
    return clicked_entry



    #Searching for CL
    client_search = driver.find_element_by_xpath('//*[@id="search-input"]')
    client_search.clear()
    client_search.send_keys(column_list[2])
    search_button = driver.find_element_by_xpath('//*[@id="search-button"]')
    search_button.click()
    name = driver.find_element_by_xpath('//*[@id="intro-step-2"]/div[2]')
    name.click()
    #Adding Note
    add_note = driver.find_element_by_xpath('//*[@id="add-note"]')
    add_note.click()
    #Adding fields in Note
    communication_type_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/div/select')
    communication_type_entry.click()
    communication_type_entry.send_keys(communication_type)
    in_or_outbound_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[2]/div/select')
    in_or_outbound_entry.click()
    in_or_outbound_entry.send_keys(in_or_outbound)
    category_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[1]/div/select')
    category_entry.click()
    category_entry.send_keys(category)
    time_billed_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[2]/div/input')
    time_billed_entry.clear()
    time_billed_entry.clear()
    time_billed_entry.clear()
    time_billed_entry.click()
    time_billed_entry.send_keys(time_billed)
    if category == "Other":
        subcategory_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[4]/input')
    else:
        subcategory_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[4]/select')
    subcategory_entry.click()
    subcategory_entry.send_keys(subcategory)
    note_text_entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[5]/textarea')
    note_text_entry.clear()
    note_text_entry.click()
    note_text_entry.send_keys(note_text)
    #replace with save button
    exit_note = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/button/i')
    exit_note.click()
    clients_search = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[2]/ul[1]/li[1]/a')
    clients_search.click()
    print("Notated " + str(column_list[1]) + "'s file: " + str(column_list[8]))

driver, spreadsheet= load_csv()
line_count = 0
login_bridge(driver)
for row in spreadsheet:
    if line_count > 0:
        column_list = create_table()
        if column_list[3] == "NA":
            print("Skipped " + str(column_list[1]))
            continue
        active_entry = assign_csv_vars(column_list)
        search_for_client()
        open_note_filed()
        update_comm_type()
        update_in_outbound()
        update_category()
        update_time_billed()
        update_subcategory()
        update_note()
        save_note()

        steps = [
            "1. Send Client",
            "2. Click Search",
            "3. Click Client",
            "4. Click Add Note",
            "5. Select Communication Type",
            "6. Select Inbound or Outbound",
            "7. Select Category",
            "8. Send Time Billed",
            "9. Select or Send Subcategory",
            "10. Send Note",
            "11. Click Save",
            "12. Click Clients",
            ]

        for step in steps:
            if step == "1. Send Client":
                xpaths_dict_key = "cl_srch"
                value = column_list[2]
            entry = click_entry(xpaths_dict_key)
            entry.send_keys(value)





        xpaths={
            "cl_srch": '//*[@id="search-input"]',
            "srch_but": '//*[@id="search-button"]',
            "cl_name": '//*[@id="intro-step-2"]/div[2]',
            "note_but": '//*[@id="add-note"]',
            "com_type": '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/div/select',
            "in_out": '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[2]/div/select',
            "category": '/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[1]/div/select',
            "time_billed": '/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[2]/div/input',
            "other_sub": '/html/body/div[4]/div[2]/div/div/div[2]/div[4]/input',
            "sub": '/html/body/div[4]/div[2]/div/div/div[2]/div[4]/select',
            "note_text": '/html/body/div[4]/div[2]/div/div/div[2]/div[5]/textarea',
            #replace with save note button:
            "exit_note": '/html/body/div[4]/div[2]/div/div/div[1]/button/i',
            "restart": '//*[@id="root"]/div/div/div[1]/div/div[2]/ul[1]/li[1]/a',
        }
    line_count += 1

driver.close()
spreadsheet.close()
print("Complete. Logged notes in " + str(line_count) + " client files.")

TEST TEST TEST