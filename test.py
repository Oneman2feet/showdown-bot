from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

debug = True
showdown = 'http://play.pokemonshowdown.com/'
driver = webdriver.Firefox() if debug else webdriver.PhantomJS()
wait = WebDriverWait(driver, 120)
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
    while True: #len(driver.find_elements_by_name('closeAndMainMenu')) > 0:
        # Conditional waits ('or') don't seem to be supported...
        # It's possible we can: 
        # - only switch (fainted)
        # - only move (arena trap, outrage, etc)
        # - both
        # TODO need to account for u-turn and volt-switch too, in which
        # a move consists of both 

        #try:
        #    wait.until(EC.element_to_be_clickable((By.NAME,'chooseMove')))
        #    moves = driver.find_elements_by_name('chooseMove')
        #except:
        #    print('no valid moves available... :(')
        #    moves = []
        #try:
        #    wait.until(EC.element_to_be_clickable((By.NAME, 'chooseSwitch')))
        #    switches = driver.find_elements_by_name('chooseSwitch')
        #except:
        #    print('no valid switches available... :(')
        #    switches = []
        wait.until(EC.presence_of_element_located((By.CLASS, 'battle-controls')))
        moves = driver.find_elements_by_name('chooseMove')
        switches = driver.find_elements_by_name('chooseSwitch')
        print('moves: ' + str(moves))
        print('switches: ' + str(switches))
        if len(moves) == 0:
            switches[0].click()
            continue
        driver.find_element_by_name('chooseMove').click()
        if not timer and len(driver.find_elements_by_name('setTimer')) > 0:
            driver.find_element_by_name('setTimer').click()
            timer = True
    #driver.quit()


if __name__=='__main__':
    main()

(mu*I1*I2*ln((((L^2)/4) + h^2)/(h^2))/(4*pi))
