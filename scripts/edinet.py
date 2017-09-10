from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from pathlib import Path
cd = Path.cwd()

# options = Options()
# Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
# options.binary_location = '/Applications/Google Chrome Canary.app/Contents/Windows/Google Chrome Canary'
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
#options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。

path = str(Path.cwd() / Path('chromedriver.exe'))
# path =
#  'C:\\Users\\takam\\Dropbox\\GitHub\\data-wrangling-master\\data-wrangling-master\\code\\chromedriver.exe'
options = Options()
options.
browser = webdriver.Chrome(executable_path=path)
webdriver.Chrome()

# %%
url = 'https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.verb=W1E63031Search&uji.bean=ee.bean.W1E63030.EEW1E63031Bean&PID=W1E63030&TID=W1E63031&SESSIONKEY=1504939429098&stype=0&dcdSelect=12001&hcdSelect=01001&ycdSelect=03001400&tsbSdt=B_010102&kbn=1&lgKbn=2&pkbn=0&skbn=1&dskb=&askb=&dflg=0&iflg=0&preId=1&chr=%E6%B2%BF%E9%9D%A9&hbn=true&spf5=2&otd=12001&hcd=01001&ycd=03001400&sec=&scc=&snm=&spf1=1&spf2=1&iec=&icc=&inm=&spf3=1&fdc=&fnm=&spf4=1&cal=1&era=H&yer=&mon=&psr=1&pid=4'

# %%
browser.get(url)
assert 'EDINET' in browser.title

# %%
links = browser.find_elements_by_css_selector('.table_border_1 > a')
company_name = links[1].text
links[0].click()
window_after = browser.window_handles[1]
browser.switch_to_window(window_after)
# %%
sleep(3)
# wait = WebDriverWait(browser,10)
# wait.until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME,".indent-1"),"第一部"))
browser.save_screenshot('image1.png')
browser.switch_to_frame("viewFrame")
browser.switch_to_frame("menuFrame2")
browser.find_elements_by_css_selector('a')[1].click()
browser.switch_to.default_content()
browser.switch_to_frame("viewFrame")
browser.switch_to_frame("mainFrame")
enkaku = browser.find_elements_by_css_selector('.style_pb_after')[2]
assert '沿革' in enkaku.find_element_by_css_selector('h3').text
enkaku_html = enkaku.get_attribute("innerHTML")

# %%
enkaku_dict = {}
enkaku_dict[company_name] = enkaku_html
# %%
import requests
from bs4 import BeautifulSoup
url = "https://news.yahoo.co.jp/topics"
response = requests.get(url)
bs = BeautifulSoup(enkaku_html,"lxml")

# %%
ull = 'https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.verb=W00Z1010initialize&uji.bean=ek.bean.EKW00Z1010Bean&PID=W1E63031&TID=W00Z1010&SESSIONKEY=1505008899533&stype=0&dcdSelect=12001&hcdSelect=01001&ycdSelect=03001400&tsbSdt=&syoruiKanriNo=S100B9FQ&keyword1=%E6%B2%BF%E9%9D%A9&keyword2=&keyword3=&keyword4=&keyword5=&lgKbn=2&pkbn=0&skbn=1&dskb=&askb=&dflg=0&iflg=0&preId=1&chr=%E6%B2%BF%E9%9D%A9&hbn=true&spf5=2&otd=12001&hcd=01001&ycd=03001400&sec=&scc=&snm=&spf1=1&spf2=1&iec=&icc=&inm=&spf3=1&fdc=&fnm=&spf4=1&cal=1&era=H&yer=&mon=&psr=1&pid=4&row=100&idx=0&str=&kbn=1&flg='
import requests
import certifi
s = requests.Session()
s.headers.update({'user-agent':'takamiura12@gmail.com'})
s.get(ull,verify=True)
cert = requests.certs.where()
cert
response = requests.get(ull,verify=cert)
bs = BeautifulSoup(enkaku_html,"lxml")
# %%

ent.append(j.text)

# %%
browser.maximize_window()
browser.find_elements_by_css_selector('.indent-1')

# %%
browser.switch_to_window(window_before)
assert 'EDINET' in browser.title
browser.find_elements_by_css_selector('a')[10].text
browser.find_elements_by_css_selector('*')[20].text

# %%
window_after
window_before
browser.find_elements_by_css_selector('p[class="indent-1"]')


# %%
browser.get('http://disclosure.edinet-fsa.go.jp/')

# %%
kensaku_button = browser.find_element_by_css_selector('.kensaku')
kensaku_button.click()

# %%
menu = browser.find_elements_by_css_selector('.menuItem a')
assert '全文検索' in menu[2].text
menu[2].click()

# %%
search_bar = browser.find_element_by_css_selector('input[name=chr]')
search_bar.clear()
search_bar.send_keys('沿革')

# %%
browser.find_element_by_css_selector('#spf5_2').click()
browser.find_element_by_css_selector('#otd1').click()
browser.find_element_by_css_selector('.panel_silver2nd .panel-title-blue').click()

# %%
select_large = Select(browser.find_element_by_css_selector('#P10'))
select_large.select_by_index(1)
select_small = Select(browser.find_element_by_css_selector('select[name="ycd"]'))
select_small.select_by_index(1)

 # %%
browser.find_element_by_css_selector('#sbm2').click()
browser.find_element_by_css_selector('#ui-dynatree-Cb3-B_010102 > .ui-dynatree-checkbox').click()
browser.find_element_by_css_selector('input[type="button"]').click()


# %%
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
