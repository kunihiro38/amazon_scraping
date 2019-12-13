from selenium import webdriver
from selenium.webdriver.support.select import Select
import chromedriver_binary
import time

# chromeを使用します
driver = webdriver.Chrome()

def amazon_login(email,password,login_url):
    # メールアドレス入力
    driver.get(login_url)
    search_box = driver.find_element_by_id("ap_email")
    search_box.send_keys(email)
    search_box.submit()
    time.sleep(2)
    # パスワード入力
    search_box = driver.find_element_by_id("ap_password")
    search_box.send_keys(password)
    search_box.submit()
    time.sleep(2)
    # amazonホーム画面からの操作
    driver.get("https://www.amazon.co.jp/ref=gno_logo")
    selectbox_element = driver.find_element_by_id("searchDropdownBox")
    selectbox = Select(selectbox_element)
    # カテゴリーの選択
    selectbox.select_by_value("search-alias=videogames")
    input_keyword = driver.find_element_by_id("twotabsearchtextbox")
    # ポケモンを選択
    input_keyword.send_keys("ポケモン")
    submit = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
    submit.submit()

email = "input_your_email"
password = "input_your_passwd"
login_url = "https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_signin&switch_account="

amazon_login(email, password, login_url)
