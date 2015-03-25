from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import random
from time import sleep

debug = True
showdown = 'http://play.pokemonshowdown.com/'
driver = webdriver.Firefox() if debug else webdriver.PhantomJS()
wait = WebDriverWait(driver, 120)
shortwait = WebDriverWait(driver, 15)
username = 'zarly'
password = 'phantom'
log = open('log', 'w')

def login():
    wait.until(EC.element_to_be_clickable((By.NAME,'login')))
    driver.find_element_by_name('login').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_css_selector('button[type=submit]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button[type=submit]').click()
    print("Logged in.")

def join_battle():
    driver.implicitly_wait(1)
    wait.until(EC.element_to_be_clickable((By.NAME,'search')))
    driver.implicitly_wait(2)
    driver.find_element_by_name('search').click()
    print("Battle Started")

def main():
    driver.set_window_size(1200, 800)
    driver.get(showdown)
    print(driver.current_url)
    login()
    join_battle()
    
    timer = False

    while True:  #len(driver.find_elements_by_name('closeAndMainMenu')) > 0:
        # It's possible we can: 
        # - only switch (fainted)
        # - only move (arena trap, outrage, etc)
        # - both
        # TODO need to account for u-turn and volt-switch too, in which
        # a move consists of both 
        switches = []
        moves = []
        while len(switches) == 0 or len(moves) == 0:
            moves = driver.find_elements_by_name('chooseMove')
            switches = driver.find_elements_by_name('chooseSwitch')
        print('moves: ' + str([m.get_attribute('data-move') for m in moves]), file=log)
        print('switches: ' + str([s.text for s in switches]), file=log)

        import pdb; pdb.set_trace()
        if len(moves) == 0:
            switches[1].click()
            continue
        moves[0].click()
        if not timer and len(driver.find_elements_by_name('setTimer')) > 0:
            driver.find_element_by_name('setTimer').click()
            timer = True
    #driver.quit()


if __name__=='__main__':
    try:
        main()
    finally:
        log.close()
        driver.quit()
