from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CustomUser
# Create your tests here.

class CustomUser_Test(TestCase):
    def setUp(self):
        
        self.user = get_user_model().objects.create_user(
            username = 'aghyad',
            email='aghyad.zu@admin.com',
            password = 'aghyad@123456'
        )
        
        self.fake_email = CustomUser.objects.create(
            first_name = 'hadeel',
            last_name = 'hussam',
            email = 'hadeel@gmail.com'        
            
        )
        
        
    def test_login_page_status(self):
        res = self.client.get(reverse('account_login',))
        self.assertEqual(res.status_code,200)
        
    def test_signout_page_status(self):
        res = self.client.get(reverse('account_signup'))
        self.assertEqual(res.status_code, 200)
