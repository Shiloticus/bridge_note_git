from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import os
import time
import csv
from selenium.webdriver.support import expected_conditions as EC



def load_csv():
    chrome_path = path + "\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.implicitly_wait(10)
    directory = os.getcwd()
    print(directory)
    csv_path = path + "\\Files\\BridgeNotes.csv"
    spreadsheet = open(csv_path, mode='r')
    return driver, spreadsheet

def test_fun():
    test_y_n = 0
    yes_no = ["Yes", "No"]
    while test_y_n not in yes_no:
        test_y_n = input("Would you like to test this script before running?")
        if test_y_n not in yes_no:
            print("Invalid input")
        else:
            continue
    return test_y_n


def login_bridge(driver):
    driver.get("https://crm.uprightlaw.com/account/login")
    user = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[1]/input")
    user.clear()
    user.send_keys("bbloomer@uprightlaw.com")
    password_field = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[2]/input")
    password_field.send_keys("silverRabbit17$")
    login = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div[3]/button")
    login.click()
    input("Log in and hit Enter to proceed")


def create_table():
    row1_column = ''.join(row)
    column_list = row1_column.split(',')
    return column_list


def search_for_client():
    try:
        client_search = driver.find_element_by_xpath('//*[@id="search-input"]')
        client_search.clear()
        client_search.send_keys(column_list[2])
        search_button = driver.find_element_by_xpath('//*[@id="search-button"]')
        search_button.click()
        name = driver.find_element_by_xpath('//*[@id="intro-step-2"]/div[2]')
        name.click()
    except:
        try:
            client_search = driver.find_element_by_xpath('//*[@id="search-input"]')
            client_search.clear()
            time.sleep(1)
            client_search.clear()
            time.sleep(1)
            client_search.clear()
            client_search.send_keys(column_list[2])
            search_button = driver.find_element_by_xpath('//*[@id="search-button"]')
            search_button.click()
            name = driver.find_element_by_xpath('//*[@id="intro-step-2"]/div[2]')
            name.click()
        except:
            print("Stuck on this CL: " + column_list[1] + "  :  " + column_list[2])
            input("Open next client file and press enter")
    return

def click_add_notes():
    try:
        add_note = driver.find_element_by_xpath('//*[@id="add-note"]')
        add_note.click()
    except:
        time.sleep(2)
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

def exit_for_testing():
    exit_note = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/button')
    exit_note.click()

def contact_made():
    contact_y_n = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[3]/div[3]/label/span[1]')
    contact_y_n.click()

def save_note():
    save_note = driver.find_element_by_xpath('//*[@id="add-note-btn"]')
    save_note.click()

def clients_search():
    client_search = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[2]/ul[1]/li[1]/a')
    client_search.click()

def print_line():
    print("Notated " + str(column_list[1]) + "'s file: " + str(column_list[8]))

path = os.getcwd()
if not os.path.exists('ChromeDriver'):
    os.makedirs('ChromeDriver')
    print("If you do not have Chrome, please download and install Google Chrome.")
    input("Once you have installed Google Chrome, press any key to continue")
    print("Please download ChromeDriver.exe and add to " + path + "\\ChromeDriver")
    print("Mac Download Link: https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_mac64.zip")
    print("Windows Download Link: https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip")
    input("Once Chromedriver.exe is in " + path + "\\ChromeDriver, please press any key to continue")

if not os.path.exists('Files'):
    os.makedirs('Files')
    print("Add Bridge Notes CSV to " + path + "\'Files\'")
    print("Rename the file to \'BridgeNotes\'")
    input("Press enter when file is loaded and renamed")
driver, spreadsheet = load_csv()
line_count = 0
login_bridge(driver)
test_input = test_fun()
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
        try:
            search_for_client()
        except:
            try:
                time.sleep(2)
                search_for_client()
            except:
                input("Search for " + column_list[1] + " manually and press enter")
        try:
            click_add_notes()
        except:
            try:
                time.sleep(2)
                click_add_notes()
            except:
                input("Click add note and press enter")
        communication_type_fun()
        in_or_outbound_fun()
        category_fun()
        try:
            time_billed_fun()
        except:
            try:
                time.sleep(2)
                time_billed_fun()
            except:
                input("Enter time billed and press enter")
        subcategory_fun()
        contact_made()
        note_text_fun()
        if test_input == "Yes":
            exit_for_testing()
        elif test_input == "No":
            save_note()
            #print("TESTED AND CLOSED")
            #exit_for_testing()
        else:
            print(test_input)
            input("Didn't work")

        try:
            clients_search()
        except:
            try:
                time.sleep(2)
                clients_search()
            except:
                input("Click 'Clients' and press enter")
        print_line()
    line_count += 1

driver.close()
spreadsheet.close()
print("Complete. Logged notes in " + str(line_count) + " client files.")


