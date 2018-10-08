# 登录 51job ，
# # http://www.51job.com
# #
# # 输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉），
# # 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
# #
# # Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
# # Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
# # 高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
from selenium import webdriver
driver=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('http://www.51job.com')
ele_key=driver.find_element_by_id('kwdselectid')
ele_key.send_keys('python')
driver.find_element_by_id('work_position_click').click()
driver.implicitly_wait('10')
eles_position_multiple_selected=driver.find_elements_by_css_selector('.tin span')
for ele in eles_position_multiple_selected:
    if ele.text !='杭州':
        ele.click()
    driver.implicitly_wait('10')
    driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
    driver.find_element_by_class_name('p_but').click()
    driver.find_element_by_css_selector('.ush.top_wrap button').click()
    jobs=driver.find_elements_by_css_selector('.t1 span')
    for job in jobs:
        print(job.text)






