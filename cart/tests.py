from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product

class CartAddProductTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.product = Product.objects.create(name='Test Product', price=100, stock=5)

    def test_add_product_to_cart_without_logging_in(self):
        # Ensure the user is logged out
        self.client.logout()

        response = self.client.post(reverse('cart:cart_add', args=[self.product.id]), {'quantity': 1})
        
        # Verify that the user is redirected to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('cart:cart_add', args=[self.product.id]))
