from selenium import webdriver          
from selenium.webdriver.common.keys import Keys
import unittest
import time

# (1) 测试类，继承自 unittest.TestCase
class NewVisitorTest(unittest.TestCase):                            # (1)
    def setUp(self):                                                # (3)
        self.browser = webdriver.Firefox()
    def tearDown(self):                                             # (3)
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):          # (2)
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        print(self.browser.title)
        self.assertIn('To-Do',self.browser.title)                   # (4)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-DO',header_text)

        # She is invited to enter a to-do  item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peapcock feathers" into a text book (Edit's hoddy is tying fly-finshing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        # When she hits enter, the page updates, and now the page lists
        # "1.: Buy peacock feathers" as an item in a  to-do lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting her to add another item. 
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)



        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name("tr")
        # self.assertTrue(
        #     # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
        #     # 
        #     any(row.text=='1:Buy peacock feathers' for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        self.assertIn("1: Buy peacock feathers",[row.text for row in rows])
        self.assertIn("2: Use peacock feathers to make a fly",[row.text for row in rows])

        self.fail("Finish the test!")
        # There is still a text box inviting her to add another item. She 
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        # self.fail("Finish the Test")                                # (5)


    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])


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


if __name__ == '__main__':                                          # (6)
    unittest.main(warnings='ignore')                                # (7) 