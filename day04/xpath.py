# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get('http://tieba.baidu.com/f?ie=utf-8&kw=数学&fr=search&red_tag=i0828700459')
#
# ele = driver.find_elements_by_xpath('//*[@id="thread_list"]/li')
#
# # //*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a
# # //*[@id="thread_list"]/li[3]/div/div[2]/div[1]/div[1]/a
# # //*[@id="thread_list"]/li[4]/div/div[2]/div[1]/div/a
# for i in ele:
#
#     try:
#
#         print(i.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').text)
#
#         print(i.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').get_attribute('href'))
#
#     except:
#
#         print('error')
#
# driver.maximize_window()
#
# driver.quit()


#########################################
from selenium import webdriver
url = 'http://tieba.baidu.com/f?ie=utf-8&kw=数学&fr=search&red_tag=i0828700459'
driver = webdriver.Chrome()
num = 1
def op(url):
    global driver
    global num
    driver.get(url)
    ele = driver.find_elements_by_xpath('//*[@id="thread_list"]/li')
    for i in ele:
        try:
            print(i.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').text)
            print(i.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').get_attribute('href'))
        except:
            print('error')
    driver.maximize_window()
    url = driver.find_element_by_xpath('//*[@id="frs_list_pager"]/a').get_attribute('href')
    num += 1
    if num < 5:
        print(url)
    else:
        driver.quit()
op(url)

