
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ledform.views import product_list_view, product_detail_view, product_create_view

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('product: product-list')
        self.assertEquals(resolve(url).func, product_list_view)

    def test_create_url_is_resolved(self):
        url = reverse('product-create', args=['some-slug'])
        self.assertEquals(resolve(url).func, product_create_view)