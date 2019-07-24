from selenium import webdriver
from datetime import *


def attendance():
    d = date.today()
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScLIDMWlP-erAuxjRvduaqbU1OlrVIKBxMKQqDj2M9WoEErTQ/viewform')
    xpath_id = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
    student_id = driver.find_element_by_xpath(xpath_id)
    first_name = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
    surname = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
    office_no = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
    date_ = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
    time_in_h = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
    time_in_m = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
    #time_in_ap = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[4]/div[1]/div[1]/div[1]/content')
    time_out_h = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
    time_out_m = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
    #time_out_ap = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[1]')
    #note = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/div[1]/input')
    form = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span')

    student_id.send_keys('')
    first_name.send_keys('')
    surname.send_keys('')
    office_no.send_keys('')
    date_.send_keys('{}/{}/{}'.format(d.day, d.month, d.year))
    date_.send_keys('dd/mm/yyyy')
    time_in_m.send_keys('30')
    time_in_h.send_keys('11:00')
    time_out_h.send_keys('18:00')
    time_out_m.send_keys('30')
    #note.send_keys("Tim's attendance")
    form.click()


attendance()
