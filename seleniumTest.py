from selenium import webdriver
import urllib,time

port = "5000"
ip = "192.168.99.101"
url = "http://" + ip + ":" + port
driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")
driver.get(url)
text_element = driver.find_element_by_xpath('/html/body')
print(text_element.text)
time.sleep(5)
driver.close()
# print(docker_ip+":"+port)
