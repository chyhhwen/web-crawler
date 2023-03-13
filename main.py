import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    path = "C:/Users/User/Desktop/web-crawler/lib/chromedriver.exe"
    driver = webdriver.Chrome(path, options = option)
    print("今日股價")
    #台積電
    url = "https://tw.search.yahoo.com/search?p=2330&fr=finance&fr2=p%3Afinvsrp%2Cm%3Asb"
    driver.get(url)
    elem = "fin_quotePrice"
    title = driver.find_elements(By.CLASS_NAME, elem)
    for i in title:
        print("台積電:" + i.text)
    #聯發科
    url = "https://tw.search.yahoo.com/search;_ylt=Awrt4BvBBw9keQ0U425r1gt.;_ylc=X1MDMjExNDcwNTAwMwRfcgMyBGZyA2ZpbmFuY2UEZnIyA3NiLXRvcARncHJpZANkdjJ5dExDZ1EzS0lRME05YXRscGxBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DdHcuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNARxdWVyeQMyNDU0BHRfc3RtcAMxNjc4NzA2Njc5?p=2454&fr2=sb-top&fr=finance"
    driver.get(url)
    elem = "fin_quotePrice"
    title = driver.find_elements(By.CLASS_NAME, elem)
    for i in title:
        print("聯發科:" + i.text)
    # 鴻海
    url = "https://tw.search.yahoo.com/search;_ylt=AwrtgxItCA9kvy4UTDRr1gt.;_ylc=X1MDMjExNDcwNTAwMwRfcgMyBGZyA2ZpbmFuY2UEZnIyA3NiLXRvcARncHJpZANaU0g1anBUNVRTYTFUV0NTNTYwZk9BBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DdHcuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNARxdWVyeQMyMzE3BHRfc3RtcAMxNjc4NzA2NzM0?p=2317&fr2=sb-top&fr=finance"
    driver.get(url)
    elem = "fin_quotePrice"
    title = driver.find_elements(By.CLASS_NAME, elem)
    for i in title:
        print("鴻海:" + i.text)

    driver.quit()

if __name__ == '__main__':
    login()

