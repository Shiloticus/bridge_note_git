from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


"""This module allows the user to leave notes in bridge by using a dictionary."""


def xpath_dict():
# defines the xpaths used for leaving notes in bridge (dict_name = xpath_dict())
    xpath_dictionary = {
        "user_field": "//*[@id='root']/div/div/div/div/div[2]/div[1]/input",
        "password_field": '//*[@id="root"]/div/div/div/div/div[2]/div[2]/input',
        "login_click": "//*[@id='root']/div/div/div/div/div[2]/div[3]/button",
        "cl_search_field": '//*[@id="search-input"]',
        "cl_search_click": '//*[@id="search-button"]',
        "cl_found_click": '//*[@id="intro-step-2"]/div[2]',
        "add_notes_click": '//*[@id="add-note"]',
        "communication_type_field": '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/div/select',
        "in_or_out_field": '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[2]/div/select',
        "contact_made_click": '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[3]/div[3]/label/span[1]',
        "category_field": '/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[1]/div/select',
        "time_billed_field": '/html/body/div[4]/div[2]/div/div/div[2]/div[3]/div[2]/div/input',
        "subcategory_field_if_other": '/html/body/div[4]/div[2]/div/div/div[2]/div[4]/input',
        "subcategory_field_not_other": '/html/body/div[4]/div[2]/div/div/div[2]/div[4]/select',
        "note_field": '/html/body/div[4]/div[2]/div/div/div[2]/div[5]/textarea',
        "exit_note_if_test": '/html/body/div[4]/div[2]/div/div/div[1]/button',
        "save_note_if_not_test": '//*[@id="add-note-btn"]',
        "search_new_cl_click": '//*[@id="root"]/div/div/div[1]/div/div[2]/ul[1]/li[1]/a'
    }
    return xpath_dictionary


def load_chrome_driver(path):
# Loads chrome driver which is needed to use selenium
    if not os.path.exists('ChromeDriver\\chromedriver.exe'):
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
    chrome_driver_path = path + "\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(10)
    driver.get("https://crm.uprightlaw.com/account/login")
    time.sleep(3)
    return driver



def click_any_element(driver, xpath):
# Clicks element as defined by xpath as dictionary key ("dict_name['field_name'])
    try:
        element = driver.find_element_by_xpath(xpath)
        element.click()
    except:
        time.sleep(2)
        element = driver.find_element_by_xpath(xpath)
        element.click()

def send_keys_to_element(driver, field_text, xpath):
# Clicks element as defined by xpath as dictionary key and then types field_text ("dict_name['field_name'].
# Should define field_text in dictionary
    try:
        element = driver.find_element_by_xpath(xpath)
        element.click()
        try:
            element.clear()  # multiple clears needed for some reason
            element.clear()  # multiple clears needed for some reason
        except:
            element.click()
        element.send_keys(field_text)
    except:
        time.sleep(2)
        element.click()
        try:
            element.clear()  # multiple clears needed for some reason
            element.clear()  # multiple clears needed for some reason
        except:
            element.click()
        element.send_keys(field_text)

