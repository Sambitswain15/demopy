from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Chromedriver.exe")
driver.maximize_window()
driver.get("https://google.com")
driver.implicitly_wait(5)
driver.quit()
print("hello world")

