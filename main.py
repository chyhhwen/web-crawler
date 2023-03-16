import pymysql
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def insert(sid,name,price):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stonk', charset='utf8')
    cursor = db.cursor()
    quary = "INSERT into `data`(`sid`,`name`,`price`,`time`) VALUES " \
            "('" + sid + "'," + "'" + name + "'," + "'" + price + "'," + "'" + time + "')"
    print(quary)
    try:
        cursor.execute(quary)
        db.commit()
        print('success')
    except Exception as ex:
        db.rollback()
        print(ex)
    db.close()
def login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    path = "C:/Users/User/Desktop/web-crawler/lib/chromedriver.exe"
    driver = webdriver.Chrome(path, options=option)
    url = "https://www.google.com/"
    datalist = ["2330","2317"]
    dataname = ["台積電","鴻海"]
    size = 2
    driver.implicitly_wait(1)
    driver.get(url)
    print("今日股價")
    for i in range(size):
        try:
            search = driver.find_element(By.NAME, 'q')
            search.send_keys(datalist[i])
            search.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print('無法定位')
        elem = "IsqQVc"
        title = driver.find_elements(By.CLASS_NAME, elem)
        print(dataname[i] + ":" + title[0].text)
        insert(datalist[i],dataname[i],title[0].text)
        driver.back()
    driver.quit()


if __name__ == '__main__':
    login()

