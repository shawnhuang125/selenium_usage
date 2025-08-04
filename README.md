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
- **尋找element1並執行**
```
[自訂變數] = driver.find_element(By.NAME, "談入name元素的名稱")
```
|方法|	說明|	範例值|	實際用法範例|
|--|--|--|--|
|By.ID|	用元素的 id 屬性|	"username"	|driver.find_element(By.ID, "username")|
|By.NAME|	用元素的 name 屬性	|"account"|	driver.find_element(By.NAME, "account")|
|By.CLASS_NAME|	用元素的 class 名稱|	"input-field"|	driver.find_element(By.CLASS_NAME, "input-field")|
|By.TAG_NAME|	用 HTML 標籤名	|	"input"|driver.find_element(By.TAG_NAME, "input")|
|By.LINK_TEXT|	用超連結文字完全比對|	"點我登入"	|driver.find_element(By.LINK_TEXT, "點我登入")|
|By.PARTIAL_LINK_TEXT|	用超連結部分文字比對	|"登入"	|driver.find_element(By.PARTIAL_LINK_TEXT, "登入")|
|By.CSS_SELECTOR|	用 CSS 選擇器|	"input[name='account']"	|driver.find_element(By.CSS_SELECTOR, "input[name='account']")|
|By.XPATH|	用 XPath 語法|	"//input[@name='account']"	|driver.find_element(By.XPATH, "//input[@name='account']")|
- **element可以執行的動作**
```
[自訂變數].send_keys("string")
```
|方法|	功能|	範例|
|--|--|--|
|send_keys(text)	|輸入文字|	element.send_keys("admin")|
|click()	|點擊按鈕、連結、核取框等|	element.click()|
|clear()	|清除輸入框內容|	element.clear()|
|get_attribute(name)	|取得元素的屬性值|	element.get_attribute("value")|
|text	|取得元素的內文字串|	element.text|
|is_displayed()	|判斷元素是否可見|	element.is_displayed()|
|is_enabled()	|判斷元素是否可用|	element.is_enabled()|
|is_selected()	|判斷核取框或選項是否被選取|	element.is_selected()|
|submit()	|提交 <form> 表單|	element.submit()|
