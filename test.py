from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

debug = True
showdown = 'http://play.pokemonshowdown.com/'

driver = webdriver.Firefox() if debug else webdriver.PhantomJS()
wait = WebDriverWait(driver, 120)
def main():
    driver.set_window_size(1200, 800)
    driver.get(showdown)
    print driver.current_url
    driver.implicitly_wait(3)
    login()
    driver.implicitly_wait(3)
    driver.find_element_by_name('search').click()
    print "Battle Started"
    timer = False
    while True: #len(driver.find_elements_by_name('closeAndMainMenu')) > 0:
        wait.until(EC.element_to_be_clickable((By.NAME,'chooseMove')))
        driver.find_element_by_name('chooseMove').click()
        if not timer and len(driver.find_elements_by_name('setTimer')) > 0:
            driver.find_element_by_name('setTimer').click()
            timer = True

    #driver.quit()


username = 'zarly'
password = 'phantom'
def login():
    wait.until(EC.element_to_be_clickable((By.NAME,'login')))
    driver.find_element_by_name('login').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_css_selector('button[type=submit]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button[type=submit]').click()
    print "Logged in."

main()
