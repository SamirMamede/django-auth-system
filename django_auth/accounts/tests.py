from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

    def test_home_page_access(self):
        response = self.client.get(reverse('accounts:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home.html')

    def test_private_pages_without_login(self):
        response1 = self.client.get(reverse('accounts:private_page_one'))
        response2 = self.client.get(reverse('accounts:private_page_two'))
        
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 302)

    def test_private_pages_with_login(self):
        self.client.login(username='testuser', password='testpass123')
        
        response1 = self.client.get(reverse('accounts:private_page_one'))
        response2 = self.client.get(reverse('accounts:private_page_two'))
        
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_registration_form_display(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_registration_success(self):
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

class UserFormTest(TestCase):
    def test_login_form_validation(self):
        from .forms import LoginUserForm
        
        form_data = {'username': 'testuser', 'password': 'testpass123'}
        form = LoginUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_validation(self):
        from .forms import UserRegistrationForm
        
        form_data = {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())