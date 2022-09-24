import selenium
from selenium import webdriver
from settings import config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized");
driver = webdriver.Chrome(options=chrome_options)
print(driver)




def start():
    print(f"selenium {selenium.__version__}")
    print(config.client_url)
    driver.get(config.client_url)
    for attempt in range(10):
        driver.switch_to.new_window()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

