# import requests,re
# url  = "http://www.baidu.com"
# response = requests.get(url)
# response.encoding = 'utf-8'  ##防止乱码，编码格式一致
# #print(response.status_code)###状态码  200是正确
# if response.status_code == 200:
#     print(response.text)
#     text = response.text.replace(">",">\n")
#     with open(r"index.txt",'w') as f:
#         f.write(text)
#     print("源代码报存完毕")
##########################################
# response1 = requests.get(url)
# response1.encoding = 'utf-8'
# url2 = 'D://aa'
# reg  = re.compile('src=//(.+\.png)')
# if response1.status_code == 200:
#     text1 = response1.text
#     list0 = reg.findall(text1)
#     num = 1
#     for i in list0:
#         url3 = url2 + 'bd'+str(num) + '.png'
#         response3 = requests.get('http://'+i)
#         with open(url3,'wb') as f1:
#             f1.write(response3.content)
#             print('bd' + str(num) + '.png下载完成')
#             num += 1
#################################
##使用代码操作浏览器
##打开谷歌
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='bin\chromedriver.exe')
##打开火狐
#driver = webdriver.Firefox(executable_path='bin\geckodriver.exe')  ##用火狐报错，没有火狐
driver.get('http://baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('大白马')
driver.find_element_by_xpath('//*[@id="su"]').click()
#窗口最大化
driver.maximize_window()
time.sleep(3)
#截屏，之前需睡几秒
driver.save_screenshot('dabaima.png')
driver.quit()
#########################################
from selenium import webdriver
driver = webdriver.Chrome(executable_path='')
driver.get()





#################################
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='bin\chromedriver.exe')
driver.get('http://baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('大白马')
driver.find_element_by_xpath('//*[@id="su"]').click()
driver.maximize_window()
driver.save_screenshot('haha.png')
time.sleep(5)
driver.quit()

####################################
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='')
driver.get()
driver.find_element_by_xpath().send_keys()
driver.find_element_by_xpath().click()
driver.maximize_window()
driver.save_screenshot()
time.sleep(10)
driver.quit()



