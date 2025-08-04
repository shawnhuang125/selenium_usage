# selenium_usage

### selenium配置與啟用
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 正確建立 Service 並指定 chromedriver 路徑
service = Service(executable_path=r"C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

time.sleep(5)
driver.quit()

```
- **說明**
- 指定webdriver的路徑並啟用webdriver
### 
- **開啟網頁**
```
driver.get("http://192.168.26.134:3484/")
```
- **尋找element1並輸入字串**
```
[自訂變數] = driver.find_element(By.NAME, "談入name元素的名稱")
[自訂變數].send_keys("string")
```
|方法|	說明|	範例值|	實際用法範例|
|--|--|--|--|
|By.ID|	用元素的 id 屬性|	"username"	|driver.find_element(By.ID, "username")|
|By.NAME|	用元素的 name 屬性	|"account"|	driver.find_element(By.NAME, "account")|
|By.CLASS_NAME|	用元素的 class 名稱|	"input-field"|	driver.find_element(By.CLASS_NAME, "input-field")|
|By.TAG_NAME|	用 HTML 標籤名	"input"|	|driver.find_element(By.TAG_NAME, "input")|
|By.LINK_TEXT|	用超連結文字完全比對|	"點我登入"	|driver.find_element(By.LINK_TEXT, "點我登入")|
|By.PARTIAL_LINK_TEXT|	用超連結部分文字比對	"登入"|	|driver.find_element(By.PARTIAL_LINK_TEXT, "登入")|
|By.CSS_SELECTOR|	用 CSS 選擇器|	"input[name='account']"	|driver.find_element(By.CSS_SELECTOR, "input[name='account']")|
|By.XPATH|	用 XPath 語法|	"//input[@name='account']"	|driver.find_element(By.XPATH, "//input[@name='account']")|
