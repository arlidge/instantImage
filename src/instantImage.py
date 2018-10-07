import time, urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class instantImage:

    def Scrape_Instagram(self, tag, limit=20, browser='chrome'):

        print("Finding Images")
        keyword = tag

        # Opening Instagram in browser
        if 'chrome' in browser.lower():
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.get("https://www.instagram.com/" + "explore/tags/" + tag)

        print("Loading Posts")
        time.sleep(10)
        print("Loading Data")

        # Clicking on load more once to load more images. Afterwards we will just
        # tap space to scroll to the page end to load more images
        actions = ActionChains(driver)
        actions.send_keys(Keys.SPACE).perform()
        actions.send_keys(Keys.SPACE).perform()
        actions.send_keys(Keys.SPACE).perform()

        time.sleep(5)

        # Just tap space to scroll to the page end to load more images
        clear = lambda: os.system('cls')
        msg = "Loading Images"
        class_div_img = ["_si7dy"]
        for div in class_div_img:
            if len(driver.find_elements_by_class_name(div)) > 1:
                while (len(driver.find_elements_by_class_name(div)) ) <= limit :
                    actions.send_keys(Keys.SPACE).perform()
                    msg = msg + "."
                    print(msg)
                    print(len(driver.find_elements_by_class_name(div)))
                    time.sleep(2.5)
                    if len(msg) > 18:
                        msg = "Loading Images"
        print(str(limit) + " Images loaded")


        print("Closing Instagram in two minutes")
        time.sleep(120)
        driver.quit()
