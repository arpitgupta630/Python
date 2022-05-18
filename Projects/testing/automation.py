from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver.exe")

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert "Selenium Easy Demo" in chrome_browser.title