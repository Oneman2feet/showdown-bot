from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import random

global debug_flag
global username
global password
global showdown
global driver
global wait

debug_flag = True
username = 'zarly'
password = 'phantom'
showdown = 'http://play.pokemonshowdown.com'

def debug(s):
    if debug_flag:
        print s

def main():
    global driver
    global wait
    driver = webdriver.Firefox() if debug_flag else webdriver.PhantomJS()
    wait = WebDriverWait(driver, 120)
    driver.implicitly_wait(2)
    driver.set_window_size(1200, 800)
    driver.get(showdown)
    login()
    join_battle()
    

    if debug_flag:
        sleep(10)
        #driver.quit()

def battle():
    debug("Entering battle phase")
    timer = False
    while True:
        #if len(driver.find_elements_by_name('closeAndMainMenu')) > 0:
        #    break
        wait.until(EC.element_to_be_clickable((By.NAME,'chooseMove')))
        #ls = driver.find_elements_by_name('chooseMove')
        #debug("List of moves available: %s" % ls)
        #ls[int(random()*len(ls))].click()
        driver.find_element_by_name('chooseMove').click()

        if not timer and len(driver.find_elements_by_name('setTimer')) > 0:
            driver.find_element_by_name('setTimer').click()
            timer = True
    debug("Battle over")

def login():
    wait.until(EC.element_to_be_clickable((By.NAME,'login')))
    driver.find_element_by_name('login').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_css_selector('button[type=submit]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button[type=submit]').click()
    if driver.find_element_by_class_name('username').text == username:
        debug("Logged in.")

def join_battle():
    #driver.implicitly_wait(1)
    wait.until(EC.element_to_be_clickable((By.NAME,'search')))
    #driver.implicitly_wait(5)
    driver.find_element_by_name('search').click()
    #driver.find_element_by_name('search').click()
    debug("Battle Started")

if __name__ == '__main__':
    main()
