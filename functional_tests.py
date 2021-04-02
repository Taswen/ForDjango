from selenium import webdriver          
import unittest

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
        self.assertIn('To-Do',self.browser.title)                   # (4)
        self.fail("Finish the Test")                                # (5)

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