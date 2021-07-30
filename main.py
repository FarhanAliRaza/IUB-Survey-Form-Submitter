from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
def main(r, url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver=webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    radios = driver.find_elements_by_xpath(f"//label [contains( text(), '{r}')]")
    print(radios)
    for i in radios:
        i.click()
    txts = driver.find_elements_by_tag_name("textarea")
    for i in txts:
        i.send_keys("No")
    btn = driver.find_element_by_xpath(f"//button [contains( text(), 'Submit')]")
    print(btn.click())
    time.sleep(5)
    driver.quit()
print(sys.argv)
url = sys.argv[1]

main("Very Satisfied", url)
