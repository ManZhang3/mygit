1.frame框架 与iframe
2.切换到frame
driver.switch_to.frame(frame_reference)
括号内为frame的name属性或ID属性
索引值从0 开始
3.frame对应的webelement:driver.find_element_by_tag_name('iframe')
4.切换到html界面：driver.switch_to.default_content()
5.注意那些会变化的ID
css选择器
1.选择器{声明；声明}    h1{color:red;font-size:14px}
css选择器是浏览器用来选择元素的
2.选择元素的方法:
tag;p{color:red;}
id :#food{color:red;}  #加上ID的值
class:  .vegetable{color:red;}   .加上class的值
根据tag名和class组合写:span..vegetable{color:red;}
3.用css选择器选择web元素
find_element_by_css_selector()
find_elements_by_css_selector()
根据tag名：driver.find_elements_by_css_selector('p')
根据ID：driver.find_elements_by_css_selector('#food')
根据clsaa :driver.find_elements_by_css_selector('.vegetable')
4.后代选择器descendant
选择元素内部的元素 driver.find_elements_by_css_selector('#choose_car option')

