from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time as t
from datetime import datetime, time

def scrape_timetable():
    # open the website
    url = 'https://www.scotrail.co.uk/plan-your-journey/stations-and-facilities/chc'
    driver = webdriver.Chrome()
    driver.get(url)

    # click cookie button
    try:
        cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]")))
        cookie_button.click()
    except:
        print('Failed to click the cookie button.')

    # click collapse button
    try:
        collapse_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "act-boards")))
        collapse_button.click()
    except:
        print("Failed to click the collapse button.")

    # click updated button but it does not work
    # try:
    #     button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nre-ldb-stations-off")))
    #     button.click()
    # except:
    #     print("Failed to click the update button.")

    # Get the timetable by xpath
    try:
        table = driver.find_element(By.XPATH, '//*[@id="nre-ldb-stations"]') # May need to update xpath.
                                    #"//div[@class='table-responsive']//table[@class='table table-bordered table-restriped bt_table ']"
        table_html = table.get_attribute('outerHTML')
        df = pd.read_html(table_html)[0]
        df = df[df.iloc[:, 0] != 'Loading...'].reset_index(drop=True)
        df['date'] = datetime.now().strftime("%Y-%m-%d")
        df = df.astype(str)
    except:
        print('No timetable available.')


    # csv_file = '/Users/qiaosili/Pycharm/web_scraping/data/timetable.csv'
    csv_file = 'E:\\QL_2022\\pycharm_project\\web_timetable\\data\\timetable.csv' # Specify path to save csv file.

    # Save the df to csv if it hasn't been saved before.
    if os.path.exists(csv_file) is False:
        df.to_csv(csv_file, index=False)
        print('Save timetable.')
    # If you have a save a timetable before, append the new record to old timetable.
    # To find the new records, locating the index of last train in the old timetable in the current timetable
    else:
        df_old = pd.read_csv(csv_file).astype(str).reset_index(drop=True)
        df_old_last_train = df_old.iloc[-1,0:3].astype(str)
        matching_row_index = None

        try:
            for index, row in df.iloc[:,0:3].iterrows():
                if row.equals(df_old_last_train):
                    matching_row_index = index
                    break
            if matching_row_index is not None:
                new_train = df.iloc[matching_row_index+1:]
                if new_train.empty:
                    print('Trains have not come yet.')
                else:
                    df_new = pd.concat([df_old,new_train], ignore_index=True)
                    df_new.to_csv(csv_file, index=False)
                    print('Update timetable.')
            else:
                df_new = pd.concat([df_old, df], ignore_index=True)
                df_new.to_csv(csv_file, index=False)
                print('Cannot find the record matching the last train.Append the current timetable to csv')
        except:
            print('error')
    driver.quit()


if __name__ == '__main__':

    # Train service usually operates from 5am to 0030am. Scarping timetable very 5min during the service time.
    # start_time = datetime.now().replace(hour=5, minute=10, second=0, microsecond=0)
    # end_time = start_time.replace(hour=23, minute=50)
    # print(start_time)

    start_time = time(5, 10)  # 5:10 AM
    end_time = time(23, 50)  # 11:50 P


    while True:
        current_time = datetime.now().time()
        if start_time <= current_time < end_time:
            scrape_timetable()
            print('current time:', datetime.now(), ', timetable scarped.')
        else:
            print('no operation')
        t.sleep(600)  # Sleep for 10 minutes

