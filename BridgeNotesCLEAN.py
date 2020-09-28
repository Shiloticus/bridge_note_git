from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import os
import time
import csv
from selenium.webdriver.support import expected_conditions as EC
import PrepareNotes as notes




def csv_to_list(file_path, list_name):
    with open(file_path, newline='') as current_report:
        current_report_csv = csv.reader(current_report, delimiter=',', quotechar='\"')
        row_count = 0
        for row in current_report_csv:
            if row_count > 0:
                list_name.append(row)
            row_count += 1

def add_notes():
    xpaths = notes.xpath_dict()
    test_y_n = input("Do you want to test notes before starting?")
    report_y_n = input("Do you want a running report?")
    driver = notes.load_chrome_driver(path)
    username = "bbloomer@uprightlaw.com"
    password = "silverRabbit17$"
    notes.send_keys_to_element(driver, username, xpaths["user_field"])
    notes.send_keys_to_element(driver, password, xpaths["password_field"])
    notes.click_any_element(driver, xpaths["login_click"])
    row_count = 0
    for cl in bridge_notes_list:
        row_count += 1
        notes.send_keys_to_element(driver, cl[0], xpaths["cl_search_field"])
        notes.click_any_element(driver, xpaths["cl_search_click"])
        notes.click_any_element(driver, xpaths["cl_found_click"])
        notes.click_any_element(driver, xpaths["add_notes_click"])
        notes.send_keys_to_element(driver, cl[1], xpaths["communication_type_field"])
        notes.send_keys_to_element(driver, cl[2], xpaths["in_or_out_field"])
        notes.click_any_element(driver, xpaths["contact_made_click"])
        notes.send_keys_to_element(driver, cl[3], xpaths["category_field"])
        notes.send_keys_to_element(driver, cl[4], xpaths["time_billed_field"])
        if cl[3] == "other":
            notes.send_keys_to_element(driver, cl[5], xpaths["subcategory_field_if_other"])
        else:
            notes.send_keys_to_element(driver, cl[5], xpaths["subcategory_field_not_other"])
        notes.send_keys_to_element(driver, cl[6], xpaths["note_field"])
        if test_y_n.lower() == "yes":
            input("Check to ensure notes are good, then press enter")
            notes.click_any_element(driver, xpaths["exit_note_if_test"])
        else:
            notes.click_any_element(driver, xpaths["save_note_if_not_test"])
        notes.click_any_element(driver, xpaths["search_new_cl_click"])
        if report_y_n.lower() == "yes":
            print("Completed " + str(row_count) + "/" + str(len(bridge_notes_list)) + " clients. " + str(cl[0]) + " completed.")
    print("Completed " + str(row_count) + "/" + str(len(bridge_notes_list)) + " clients.")
    driver.close()

path = os.getcwd()
bridge_notes_list = []
csv_to_list(path + "\\Files\\BridgeNotes.csv", bridge_notes_list)
add_notes()
spreadsheet.close()
print("Complete. Logged notes in " + str(line_count) + " client files.")


