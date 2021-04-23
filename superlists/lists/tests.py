from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page   # (2)

# Create your tests here.
class HomePageTest(TestCase):
    '''
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')                    # (1)
        self.assertEqual(found.func,home_page)  # (1)

    def test_home_page_returns_correct_html(self):
        
        request = HttpRequest()                 # (3)
        response = home_page(request)           # (4)
        html = response.content.decode('utf-8') # (5)
        # self.assertTrue(html.startswith("<html>"))# (6)
        # self.assertIn("<title>To-Do lists</title>",html)# (7)
        # self.assertTrue(html.endswith('</html>'))# (8)
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)
        
        # 使用Django Test Client来测试
        response = self.client.get('/')

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>",html)# (7) 
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response,'home.html')
    '''
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post("/",data={'item_text':"A new lsit item"})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response, "home.html")
        



# (1) Django用来解析URL的function，作用是找到URL应该映射到哪个view
#     当用“/”调用时，网站的根目录应该找到一个名为home_page的function

# (2) 导入要测试的方法

# (3) 

# (4)

# (5)

# (6)

# (7)

# (8)

# ()



'''----------------------------------------


Token
Python 的 CSRF 属于 Token


Session


Cookie


'''