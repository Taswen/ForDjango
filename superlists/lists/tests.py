from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, response
from django.template.loader import render_to_string

from lists.views import home_page   # (2)

from lists.models import Item

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
        

    # def test_display_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')

    #     response = self.client.get('/')

    #     self.assertIn('itemey 1',response.content.decode())
    #     self.assertIn('itemey 2',response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        '''测试数据库的存与取'''
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")



        # self.assertIn('A new list Item', response.content.decode())
        # self.assertTemplateUsed(response,"home.html")


class ListViewTest(TestCase):
    
    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')
    
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')



class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new',data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new',data={'item_text':'A new list item'})
        self.assertRedirects(response,'/lists/the-only-list-in-the-world/')    # 测试重定向断言

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