from django.urls import resolve
from django.test import TestCase
from lists.views import home_page   # (2)


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')                    # (1)
        self.assertEqual(found.func,home_page)  # (1)


# (1) Django用来解析URL的function，作用是找到URL应该映射到哪个view
#     当用“/”调用时，网站的根目录应该找到一个名为home_page的function

# (2) 