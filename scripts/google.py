from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pathlib import Path
cd = Path.cwd()

options = Options()
# Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
# options.binary_location = '/Applications/Google Chrome Canary.app/Contents/Windows/Google Chrome Canary'
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
#options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。

path = str(Path.cwd() / Path('chromedriver.exe'))
# path =
#  'C:\\Users\\takam\\Dropbox\\GitHub\\data-wrangling-master\\data-wrangling-master\\code\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=options)
browser.get('http://google.com')
assert 'Google' in browser.title
inputs = browser.find_elements_by_css_selector('form input')
for i in inputs:
    if i.is_displayed():
        search_bar = i
        break

search_bar.send_keys('web scraping with python')

search_button = browser.find_element_by_xpath('//input[@name="btnK"][@type="submit"]')
search_button.click()

browser.implicitly_wait(10)
results = browser.find_elements_by_css_selector('div h3 a')

for r in results:
    action = webdriver.ActionChains(browser)
    action.move_to_element(r)
    action.perform()
    sleep(2)

browser.quit()
