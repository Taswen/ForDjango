from unittest.case import TestCase
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver          
from selenium.webdriver.common.keys import Keys
import unittest
import time
import os

from selenium.webdriver.firefox.webdriver import WebDriver


# 最长等待时间
MAX_WAIT = 10

# (1) 测试类，可继承自 unittest.TestCase
# 这里使用 Django的测试框架
class NewVisitorTest(StaticLiveServerTestCase):                            # (1)
    def setUp(self):                                                # (3)
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER') # 199.255.98.133
        if staging_server:
            self.live_server_url = 'http://' + staging_server
    def tearDown(self):                                             # (3)
        self.browser.refresh()
        self.browser.quit()
    
    def test_can_start_a_list_for_one_user(self):          # (2)
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)      #  self.live_server_url 是LiveServerTestCase 提供的模拟测试地址

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)                   # (4)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to-do  item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peapcock feathers" into a text book (Edit's hoddy is tying fly-finshing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        # When she hits enter, the page updates, and now the page lists
        # "1.: Buy peacock feathers" as an item in a  to-do lists
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. 
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)


        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name("tr")
        # self.assertTrue(
        #     # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
        #     # 
        #     any(row.text=='1:Buy peacock feathers' for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        # self.assertIn("1: Buy peacock feathers",[row.text for row in rows])
        # self.assertIn("2: Use peacock feathers to make a fly",[row.text for row in rows])

        # The pages updates again, and now shows both items on her list
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        # Edith wonders whether the site will remeber her list. Then she sees 
        # that the site has generated a unique URL for her -- there is some 
        # explanatory text to the effect.  
        # self.fail("Finish the test!")                                   # (5)

        # She visits that URL - her to-do lists is still there.
        
        # Satisfird, she goes back to sleep          

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # She notices that her list has a uniqur URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')

        # Now a new user, Francies, comes along to the sites.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cooies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesing than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make milk', page_text)
        # Satisfied, they both go back to sleep 
    
    
    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return 
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        # She starts a new lsit and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2 ,
            512,
            delta=10
        )


# (2) 测试主体，以test开头的任何方法都是测试方法，
#     将由测试运行器运行。
#     每个类可以有多个test方法。

# (3) setUp和tearDown是在每次测试之前和之后运行的特殊方法。
#     使用它们来启动和停止我们的浏览器 
#     tearDown即使在测试期间出现错误，也会运行。

# (4) 使用self.assertIn代替断言。
#     unittest提供了许多像这样的辅助功能来进行测试，
#     比如assertEqual，assertTrue，assertFalse等等。

# (5) self.fail无论如何都会失败，
#     产生错误信息。 
#     可用它作为完成测试的提醒。

# (6) python文件单独运行时才会执行的部分

# (7) 调用unittest.main（）方法，
#     它启动unittest测试运行器，
#     它将自动在文件中寻找测试类和方法并运行它们。
#     warnings ='ignore'指定打印等级，防止了在撰写本文时爆出多余的ResourceWarning信息。 

# 不使用 unittest.TestCase 而是 LiveServerTestCase 则不需要自己写启动
# if __name__ == '__main__':                                          # (6)
#     unittest.main(warnings='ignore')                                # (7) 