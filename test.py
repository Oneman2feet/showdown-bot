from selenium import webdriver

debug = False
showdown = 'http://play.pokemonshowdown.com/'

driver = webdriver.Firefox() if debug else webdriver.PhantomJS()
def main():
    driver.set_window_size(1120, 550)
    driver.get(showdown)
    print driver.current_url
    login()
    driver.quit()


username = 'zarly'
password = 'phantom'
def login():
    driver.find_element_by_name('login').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_css_selector('button[type=submit]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button[type=submit]').click()
    print "Logged in."

main()
